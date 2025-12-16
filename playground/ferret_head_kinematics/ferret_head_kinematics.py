"""
Ferret Head Kinematics Analysis
================================

This script analyzes the ferret skull motion data to compute:
1. Angular velocity in world (global) frame
2. Angular velocity in local (head) frame
3. Angular velocity in body-relative frame
4. Euler angles (pitch, roll, yaw) in world and body-relative frames

Uses quaternion mathematics for robust rotation handling.
Body frame is constructed from spine markers with zero-roll assumption.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from numpy.typing import NDArray

from playground.ferret_head_kinematics.angular_velocity_helpers import (
    compute_omega_world,
    omega_world_to_local,
)
from playground.ferret_head_kinematics.ferret_head_kinematics_visualization import (
    load_trajectory_data,
    run_visualization,
)
from playground.ferret_head_kinematics.quaternion_helper import Quaternion


# =============================================================================
# BODY FRAME CONSTRUCTION
# =============================================================================
def construct_body_frame_from_spine(
    sacrum: NDArray[np.float64],
    spine_t1: NDArray[np.float64],
    world_up: NDArray[np.float64],
) -> NDArray[np.float64]:
    """
    Construct body coordinate frame from spine markers with zero-roll assumption.

    The body frame is defined as:
    - X-axis: pointing right (lateral)
    - Y-axis: pointing forward along spine (cranial direction)
    - Z-axis: pointing up (dorsal direction)

    Zero-roll assumption: body "up" is derived from world up projected
    perpendicular to the spine direction.

    Returns:
        3x3 rotation matrix where columns are the body frame axes in world coordinates.
    """
    # Spine direction: sacrum -> spine_t1 (caudal to cranial = forward)
    spine_vec = spine_t1 - sacrum
    spine_norm = np.linalg.norm(spine_vec)
    if spine_norm < 1e-10:
        raise ValueError("Spine markers are coincident")
    body_forward = spine_vec / spine_norm

    # Body right = forward × up (then normalize)
    # This gives us the lateral direction perpendicular to both
    body_right = np.cross(body_forward, world_up)
    right_norm = np.linalg.norm(body_right)

    if right_norm < 1e-10:
        # Spine is pointing straight up/down - degenerate case
        # Fall back to arbitrary perpendicular
        if abs(body_forward[0]) < 0.9:
            body_right = np.cross(body_forward, np.array([1.0, 0.0, 0.0]))
        else:
            body_right = np.cross(body_forward, np.array([0.0, 1.0, 0.0]))
        right_norm = np.linalg.norm(body_right)

    body_right = body_right / right_norm

    # Body up = right × forward (completing right-handed system)
    body_up = np.cross(body_right, body_forward)

    # Rotation matrix: columns are body axes expressed in world frame
    R_body: NDArray[np.float64] = np.column_stack([body_right, body_forward, body_up])

    return R_body


# =============================================================================
# DATA LOADING
# =============================================================================
def extract_rotation_matrix(row: pd.Series) -> NDArray[np.float64]:
    """Extract 3x3 rotation matrix from a DataFrame row."""
    return np.array(
        [
            [row["rotation_r0_c0"], row["rotation_r0_c1"], row["rotation_r0_c2"]],
            [row["rotation_r1_c0"], row["rotation_r1_c1"], row["rotation_r1_c2"]],
            [row["rotation_r2_c0"], row["rotation_r2_c1"], row["rotation_r2_c2"]],
        ],
        dtype=np.float64,
    )


def load_spine_markers(
    marker_csv_path: Path,
    data_type: str,
) -> pd.DataFrame:
    """
    Load spine marker data from CSV.

    Returns DataFrame with columns: frame, timestamp, sacrum_x/y/z, spine_t1_x/y/z
    """
    df = pd.read_csv(marker_csv_path)

    # Filter to requested data type
    df = df[df["data_type"] == data_type].copy()

    # Pivot to get one row per frame with marker positions as columns
    sacrum_df = df[df["marker"] == "sacrum"][
        ["frame", "timestamp", "x", "y", "z"]
    ].copy()
    sacrum_df = sacrum_df.rename(
        columns={"x": "sacrum_x", "y": "sacrum_y", "z": "sacrum_z"}
    )

    spine_t1_df = df[df["marker"] == "spine_t1"][["frame", "x", "y", "z"]].copy()
    spine_t1_df = spine_t1_df.rename(
        columns={"x": "spine_t1_x", "y": "spine_t1_y", "z": "spine_t1_z"}
    )

    result = sacrum_df.merge(spine_t1_df, on="frame")

    if len(result) == 0:
        raise ValueError(f"No matching spine markers found for data_type='{data_type}'")

    return result


# =============================================================================
# QUATERNION CONTINUITY
# =============================================================================
def ensure_quaternion_continuity(quaternions: list[Quaternion]) -> None:
    """Ensure quaternion continuity by flipping signs to avoid discontinuities."""
    for i in range(1, len(quaternions)):
        q_prev = quaternions[i - 1]
        q_curr = quaternions[i]
        dot = (
            q_prev.w * q_curr.w
            + q_prev.x * q_curr.x
            + q_prev.y * q_curr.y
            + q_prev.z * q_curr.z
        )
        if dot < 0:
            quaternions[i] = Quaternion(
                w=-q_curr.w, x=-q_curr.x, y=-q_curr.y, z=-q_curr.z
            )


# =============================================================================
# MAIN ANALYSIS
# =============================================================================
def analyze_ferret_head_kinematics(
    head_rotation_csv_path: Path,
    trajectory_data_csv: Path,
    spine_data_type: str,
    world_up: NDArray[np.float64],
) -> pd.DataFrame:
    """
    Analyze ferret head kinematics from rotation and spine marker data.

    Args:
        head_rotation_csv_path: Path to CSV with head rotation matrices
        trajectory_data_csv: Path to CSV with spine markers
        spine_data_type: Which data type to use from spine markers ('optimized' or 'noisy')
        world_up: World "up" direction for zero-roll body frame assumption

    Returns:
        DataFrame with timestamps, angular velocities, and Euler angles
    """
    print("Loading head rotation data...")
    head_df = pd.read_csv(head_rotation_csv_path)
    n_frames = len(head_df)
    print(f"  {n_frames} frames")

    # Load spine data
    print("Loading spine marker data...")
    spine_df = load_spine_markers(
        marker_csv_path=trajectory_data_csv, data_type=spine_data_type
    )
    print(f"  {len(spine_df)} frames with spine markers")

    # Verify timestamp alignment
    if not np.allclose(
        head_df["timestamp"].values, spine_df["timestamp"].values, rtol=1e-6
    ):
        raise ValueError(
            "Timestamp mismatch between head rotation and spine marker data. "
            "Interpolation not yet implemented."
        )

    timestamps: NDArray[np.float64] = head_df["timestamp"].values

    # Convert head rotations to quaternions
    print("Converting head rotation matrices to quaternions...")
    head_quaternions: list[Quaternion] = []
    for _, row in head_df.iterrows():
        R = extract_rotation_matrix(row)
        q = Quaternion.from_rotation_matrix(R)
        head_quaternions.append(q)

    # Ensure quaternion continuity (avoid sign flips)
    print("Ensuring quaternion continuity...")
    ensure_quaternion_continuity(head_quaternions)

    # Compute body frame quaternions from spine data
    print("Computing body frame from spine markers...")
    body_quaternions: list[Quaternion] = []
    for i in range(n_frames):
        sacrum = np.array(
            [
                spine_df.iloc[i]["sacrum_x"],
                spine_df.iloc[i]["sacrum_y"],
                spine_df.iloc[i]["sacrum_z"],
            ]
        )
        spine_t1 = np.array(
            [
                spine_df.iloc[i]["spine_t1_x"],
                spine_df.iloc[i]["spine_t1_y"],
                spine_df.iloc[i]["spine_t1_z"],
            ]
        )
        R_body = construct_body_frame_from_spine(
            sacrum=sacrum, spine_t1=spine_t1, world_up=world_up
        )
        q_body = Quaternion.from_rotation_matrix(R_body)
        body_quaternions.append(q_body)

    # Ensure body quaternion continuity
    ensure_quaternion_continuity(body_quaternions)

    # Compute head-relative-to-body quaternions
    print("Computing head orientation relative to body...")
    head_body_relative_quaternions: list[Quaternion] = []
    for i in range(n_frames):
        # Q_head_body = Q_body^-1 * Q_head_world
        q_rel = body_quaternions[i].inverse() * head_quaternions[i]
        head_body_relative_quaternions.append(q_rel)

    # Ensure continuity
    ensure_quaternion_continuity(head_body_relative_quaternions)

    # Compute angular velocities
    print("Computing angular velocities...")
    omega_world = np.zeros((n_frames, 3))
    omega_head_local = np.zeros((n_frames, 3))
    omega_body_relative = np.zeros((n_frames, 3))

    for i in range(n_frames):
        # Central difference for interior points, forward/backward at boundaries
        if i == 0:
            dt = timestamps[1] - timestamps[0]
            ow = compute_omega_world(
                q1=head_quaternions[0], q2=head_quaternions[1], dt=dt
            )
        elif i == n_frames - 1:
            dt = timestamps[-1] - timestamps[-2]
            ow = compute_omega_world(
                q1=head_quaternions[-2], q2=head_quaternions[-1], dt=dt
            )
        else:
            dt = timestamps[i + 1] - timestamps[i - 1]
            ow = compute_omega_world(
                q1=head_quaternions[i - 1], q2=head_quaternions[i + 1], dt=dt
            )

        omega_world[i] = ow
        omega_head_local[i] = omega_world_to_local(
            omega_world=ow, q=head_quaternions[i]
        )

        # Body-relative angular velocity
        if i == 0:
            dt = timestamps[1] - timestamps[0]
            ow_rel = compute_omega_world(
                q1=head_body_relative_quaternions[0],
                q2=head_body_relative_quaternions[1],
                dt=dt,
            )
        elif i == n_frames - 1:
            dt = timestamps[-1] - timestamps[-2]
            ow_rel = compute_omega_world(
                q1=head_body_relative_quaternions[-2],
                q2=head_body_relative_quaternions[-1],
                dt=dt,
            )
        else:
            dt = timestamps[i + 1] - timestamps[i - 1]
            ow_rel = compute_omega_world(
                q1=head_body_relative_quaternions[i - 1],
                q2=head_body_relative_quaternions[i + 1],
                dt=dt,
            )
        omega_body_relative[i] = ow_rel

    # Extract Euler angles
    print("Extracting Euler angles...")
    euler_world = np.zeros((n_frames, 3))
    euler_body_relative = np.zeros((n_frames, 3))

    for i in range(n_frames):
        euler_world[i] = head_quaternions[i].to_euler_xyz()
        euler_body_relative[i] = head_body_relative_quaternions[i].to_euler_xyz()

    # Unwrap world Euler angles to remove discontinuities at ±π
    # (only world frame - body-relative angles should stay bounded since
    # the head can't physically rotate 360° relative to the body)
    print("Unwrapping world-frame Euler angles...")
    for axis in range(3):
        euler_world[:, axis] = np.unwrap(euler_world[:, axis])

    # Build result DataFrame
    result = pd.DataFrame(
        {
            "timestamp": timestamps,
            "omega_world_x": omega_world[:, 0],
            "omega_world_y": omega_world[:, 1],
            "omega_world_z": omega_world[:, 2],
            "omega_head_local_x": omega_head_local[:, 0],
            "omega_head_local_y": omega_head_local[:, 1],
            "omega_head_local_z": omega_head_local[:, 2],
            "euler_world_roll_rad": euler_world[:, 0],
            "euler_world_pitch_rad": euler_world[:, 1],
            "euler_world_yaw_rad": euler_world[:, 2],
            "omega_body_relative_x": omega_body_relative[:, 0],
            "omega_body_relative_y": omega_body_relative[:, 1],
            "omega_body_relative_z": omega_body_relative[:, 2],
            "euler_body_relative_roll_rad": euler_body_relative[:, 0],
            "euler_body_relative_pitch_rad": euler_body_relative[:, 1],
            "euler_body_relative_yaw_rad": euler_body_relative[:, 2],
        }
    )

    return result


# =============================================================================
# MAIN
# =============================================================================
def main(
    head_rotation_csv_path: str,
    trajectory_data_csv: str,
    spawn_viewer: bool = True,
) -> None:
    """
    Run ferret head kinematics analysis and launch Rerun visualization.

    Args:
        head_rotation_csv_path: Path to CSV with head rotation matrices
        trajectory_data_csv: Path to CSV with spine markers
        spawn_viewer: Whether to spawn the Rerun viewer window
    """
    input_path = Path(head_rotation_csv_path)
    trajectory_path = Path(trajectory_data_csv)

    for thing_path in [
        input_path,
        trajectory_path,]:
        if not thing_path.exists():
            raise FileNotFoundError(f"File not found: {thing_path}")

    result_df = analyze_ferret_head_kinematics(
        head_rotation_csv_path=input_path,
        trajectory_data_csv=trajectory_path,
        spine_data_type="optimized",
        world_up=np.array([0.0, 0.0, 1.0]),
    )

    output_csv = input_path.parent / "ferret_head_kinematics.csv"
    result_df.to_csv(output_csv, index=False)
    print(f"Saved results: {output_csv}")

    # Load trajectory data for visualization
    trajectory_data = load_trajectory_data(trajectory_path)

    run_visualization(
        result_df=result_df,
        trajectory_data=trajectory_data,
        spawn=spawn_viewer,
    )


if __name__ == "__main__":
    # Example usage - update paths as needed
    head_rotation_csv = r"D:\bs\ferret_recordings\2025-07-11_ferret_757_EyeCameras_P43_E15__1\clips\0m_37s-1m_37s\mocap_data\output_data\solver_output\rotation_translation_data.csv"
    trajectory_data_csv = r"D:\bs\ferret_recordings\2025-07-11_ferret_757_EyeCameras_P43_E15__1\clips\0m_37s-1m_37s\mocap_data\output_data\solver_output\tidy_trajectory_data.csv"

    main(
        head_rotation_csv_path=head_rotation_csv,
        trajectory_data_csv=trajectory_data_csv,
    )