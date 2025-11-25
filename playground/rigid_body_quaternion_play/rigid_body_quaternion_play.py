"""
Rigid Body Transforms: World vs Local Frame Angular Velocity
=============================================================

This script demonstrates:
1. Computing angular velocity from quaternion sequences
2. The difference between world-frame and body-local-frame angular velocity
3. Why this distinction matters for sensors attached to the body

Run with: python rigid_body_frames.py
"""

import numpy as np
from numpy.typing import NDArray
from dataclasses import dataclass
from pathlib import Path
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# =============================================================================
# QUATERNION CLASS
# =============================================================================

@dataclass
class Quaternion:
    """
    Unit quaternion for rotations. Convention: scalar-first [w, x, y, z].

    Key formulas:
    - Rotation of vector v: v' = q * v * q⁻¹
    - Composition: q_total = q2 * q1 (apply q1 first, then q2)
    - Inverse (for unit quat): q⁻¹ = q* = (w, -x, -y, -z)
    """
    w: float
    x: float
    y: float
    z: float

    def __post_init__(self) -> None:
        norm = np.sqrt(self.w ** 2 + self.x ** 2 + self.y ** 2 + self.z ** 2)
        if norm < 1e-10:
            raise ValueError("Cannot normalize zero quaternion")
        self.w /= norm
        self.x /= norm
        self.y /= norm
        self.z /= norm

    @classmethod
    def identity(cls) -> "Quaternion":
        return cls(w=1.0, x=0.0, y=0.0, z=0.0)

    @classmethod
    def from_axis_angle(cls, axis: NDArray[np.float64], angle_rad: float) -> "Quaternion":
        axis = np.asarray(axis, dtype=np.float64)
        axis_norm = np.linalg.norm(axis)
        if axis_norm < 1e-10:
            return cls.identity()
        axis = axis / axis_norm
        half_angle = angle_rad / 2.0
        return cls(
            w=np.cos(half_angle),
            x=np.sin(half_angle) * axis[0],
            y=np.sin(half_angle) * axis[1],
            z=np.sin(half_angle) * axis[2],
        )

    @classmethod
    def from_euler_xyz(cls, roll: float, pitch: float, yaw: float) -> "Quaternion":
        qx = cls.from_axis_angle(axis=np.array([1, 0, 0]), angle_rad=roll)
        qy = cls.from_axis_angle(axis=np.array([0, 1, 0]), angle_rad=pitch)
        qz = cls.from_axis_angle(axis=np.array([0, 0, 1]), angle_rad=yaw)
        return qz * qy * qx

    def conjugate(self) -> "Quaternion":
        return Quaternion(w=self.w, x=-self.x, y=-self.y, z=-self.z)

    def inverse(self) -> "Quaternion":
        return self.conjugate()

    def __mul__(self, other: "Quaternion") -> "Quaternion":
        w1, x1, y1, z1 = self.w, self.x, self.y, self.z
        w2, x2, y2, z2 = other.w, other.x, other.y, other.z
        return Quaternion(
            w=w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
            x=w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
            y=w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
            z=w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2,
        )

    def rotate_vector(self, v: NDArray[np.float64]) -> NDArray[np.float64]:
        """Rotate vector v by this quaternion: v' = q * v * q⁻¹"""
        v = np.asarray(v, dtype=np.float64)
        v_quat = Quaternion(w=0.0, x=v[0], y=v[1], z=v[2])
        rotated = self * v_quat * self.conjugate()
        return np.array([rotated.x, rotated.y, rotated.z])

    def to_axis_angle(self) -> tuple[NDArray[np.float64], float]:
        w_clamped = np.clip(self.w, -1.0, 1.0)
        angle = 2.0 * np.arccos(abs(w_clamped))
        sin_half = np.sqrt(1.0 - w_clamped ** 2)
        if sin_half < 1e-10:
            return np.array([1.0, 0.0, 0.0]), 0.0
        axis = np.array([self.x, self.y, self.z]) / sin_half
        if self.w < 0:
            axis = -axis
        return axis, angle


def slerp(q1: Quaternion, q2: Quaternion, t: float) -> Quaternion:
    """Spherical linear interpolation - constant angular velocity interpolation."""
    dot = q1.w * q2.w + q1.x * q2.x + q1.y * q2.y + q1.z * q2.z

    q2_adj = q2
    if dot < 0:
        q2_adj = Quaternion(w=-q2.w, x=-q2.x, y=-q2.y, z=-q2.z)
        dot = -dot

    if dot > 0.9995:
        return Quaternion(
            w=q1.w + t * (q2_adj.w - q1.w),
            x=q1.x + t * (q2_adj.x - q1.x),
            y=q1.y + t * (q2_adj.y - q1.y),
            z=q1.z + t * (q2_adj.z - q1.z),
        )

    theta = np.arccos(dot)
    sin_theta = np.sin(theta)
    s1 = np.sin((1 - t) * theta) / sin_theta
    s2 = np.sin(t * theta) / sin_theta

    return Quaternion(
        w=s1 * q1.w + s2 * q2_adj.w,
        x=s1 * q1.x + s2 * q2_adj.x,
        y=s1 * q1.y + s2 * q2_adj.y,
        z=s1 * q1.z + s2 * q2_adj.z,
    )


# =============================================================================
# ANGULAR VELOCITY COMPUTATION
# =============================================================================

def compute_omega_world(q1: Quaternion, q2: Quaternion, dt: float) -> NDArray[np.float64]:
    """
    Compute angular velocity in WORLD frame from two quaternions.

    ω_world = (2/dt) * axis * angle, where Δq = q2 * q1⁻¹
    """
    if dt <= 0:
        raise ValueError(f"dt must be positive, got {dt}")

    delta_q = q2 * q1.inverse()
    if delta_q.w < 0:
        delta_q = Quaternion(w=-delta_q.w, x=-delta_q.x, y=-delta_q.y, z=-delta_q.z)

    axis, angle = delta_q.to_axis_angle()
    return (angle / dt) * axis


def omega_world_to_local(omega_world: NDArray[np.float64], q: Quaternion) -> NDArray[np.float64]:
    """
    Transform angular velocity from world frame to body-local frame.

    ω_local = q⁻¹ * ω_world (rotate by inverse orientation)

    This is what a sensor attached to the body would measure.
    """
    return q.inverse().rotate_vector(omega_world)


def omega_local_to_world(omega_local: NDArray[np.float64], q: Quaternion) -> NDArray[np.float64]:
    """
    Transform angular velocity from body-local frame to world frame.

    ω_world = q * ω_local (rotate by orientation)
    """
    return q.rotate_vector(omega_local)


# =============================================================================
# TRAJECTORY GENERATION
# =============================================================================

@dataclass
class Transform:
    translation: NDArray[np.float64]
    rotation: Quaternion
    time: float


def generate_trajectory(n_frames: int = 200, duration: float = 8.0) -> list[Transform]:
    """Generate a trajectory with interesting rotation to show frame differences."""
    transforms = []

    for i in range(n_frames):
        t = duration * i / (n_frames - 1)
        theta = 2 * np.pi * t / duration  # One full loop

        # Circular path
        translation = np.array([
            3 * np.cos(theta),
            3 * np.sin(theta),
            0.5 * np.sin(2 * theta),
        ])

        # Rotation: body tilts AND spins
        # This makes world vs local frame clearly different
        rotation = Quaternion.from_euler_xyz(
            roll=0.4 * np.sin(theta),  # Tilting side to side
            pitch=0.3 * np.cos(theta),  # Nodding
            yaw=theta,  # Spinning around
        )

        transforms.append(Transform(translation=translation, rotation=rotation, time=t))

    return transforms


# =============================================================================
# RIGID BODY
# =============================================================================

def create_cube_with_spike(size: float = 1.0, spike_length: float = 0.5) -> tuple[NDArray, list]:
    h = size / 2
    vertices = np.array([
        [-h, -h, -h], [h, -h, -h], [h, h, -h], [-h, h, -h],
        [-h, -h, h], [h, -h, h], [h, h, h], [-h, h, h],
        [0, 0, h], [0, 0, h + spike_length],
    ], dtype=np.float64)

    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7),
        (8, 9),
    ]
    return vertices, edges


def transform_vertices(vertices: NDArray, translation: NDArray, rotation: Quaternion) -> NDArray:
    result = np.zeros_like(vertices)
    for i, v in enumerate(vertices):
        result[i] = rotation.rotate_vector(v) + translation
    return result


# =============================================================================
# MAIN
# =============================================================================

def main() -> None:
    print("Generating trajectory...")
    transforms = generate_trajectory(n_frames=200, duration=8.0)

    # Compute angular velocities
    print("Computing angular velocities (world and local frames)...")
    n = len(transforms)
    timestamps = np.array([tf.time for tf in transforms])
    omega_world = np.zeros((n, 3))
    omega_local = np.zeros((n, 3))

    for i in range(n):
        if i == 0:
            dt = timestamps[1] - timestamps[0]
            ow = compute_omega_world(transforms[0].rotation, transforms[1].rotation, dt)
        elif i == n - 1:
            dt = timestamps[-1] - timestamps[-2]
            ow = compute_omega_world(transforms[-2].rotation, transforms[-1].rotation, dt)
        else:
            dt = timestamps[i + 1] - timestamps[i - 1]
            ow = compute_omega_world(transforms[i - 1].rotation, transforms[i + 1].rotation, dt)

        omega_world[i] = ow
        omega_local[i] = omega_world_to_local(ow, transforms[i].rotation)

    # Create visualization
    print("Creating plotly visualization...")

    fig = make_subplots(
        rows=2, cols=2,
        specs=[
            [{"type": "scene"}, {"type": "scene"}],
            [{"type": "xy"}, {"type": "xy"}],
        ],
        subplot_titles=(
            "3D Trajectory",
            "Body Local Axes Over Time",
            "Angular Velocity (WORLD Frame)",
            "Angular Velocity (LOCAL Frame)",
        ),
        vertical_spacing=0.12,
        horizontal_spacing=0.08,
    )

    # --- 3D Trajectory (top-left) ---
    translations = np.array([tf.translation for tf in transforms])
    fig.add_trace(
        go.Scatter3d(
            x=translations[:, 0], y=translations[:, 1], z=translations[:, 2],
            mode="lines", line=dict(color="blue", width=3),
            name="Path",
        ),
        row=1, col=1,
    )

    # Draw cube at a few snapshots
    vertices, edges = create_cube_with_spike()
    snapshot_idx = [0, 50, 100, 150, 199]
    colors = ["red", "orange", "green", "cyan", "purple"]

    for idx, color in zip(snapshot_idx, colors):
        tf = transforms[idx]
        verts_world = transform_vertices(vertices, tf.translation, tf.rotation)

        for edge in edges:
            v1, v2 = verts_world[edge[0]], verts_world[edge[1]]
            fig.add_trace(
                go.Scatter3d(
                    x=[v1[0], v2[0]], y=[v1[1], v2[1]], z=[v1[2], v2[2]],
                    mode="lines",
                    line=dict(color=color, width=4 if edge == (8, 9) else 2),
                    showlegend=False,
                ),
                row=1, col=1,
            )

    # --- Local Axes Visualization (top-right) ---
    # Show how the body's local XYZ axes move in world space
    axis_length = 1.5
    axis_colors = ["red", "green", "blue"]
    axis_names = ["Body X", "Body Y", "Body Z"]

    for ax_idx in range(3):
        local_axis = np.zeros(3)
        local_axis[ax_idx] = axis_length

        xs, ys, zs = [], [], []
        for i in range(0, n, 10):  # Sample every 10th frame
            tf = transforms[i]
            origin = tf.translation
            tip = origin + tf.rotation.rotate_vector(local_axis)
            xs.extend([origin[0], tip[0], None])
            ys.extend([origin[1], tip[1], None])
            zs.extend([origin[2], tip[2], None])

        fig.add_trace(
            go.Scatter3d(
                x=xs, y=ys, z=zs,
                mode="lines",
                line=dict(color=axis_colors[ax_idx], width=3),
                name=axis_names[ax_idx],
            ),
            row=1, col=2,
        )

    # --- Angular Velocity WORLD frame (bottom-left) ---
    for i, (label, color) in enumerate([("ωx", "red"), ("ωy", "green"), ("ωz", "blue")]):
        fig.add_trace(
            go.Scatter(
                x=timestamps, y=omega_world[:, i],
                mode="lines", line=dict(color=color, width=2),
                name=f"{label} (world)",
            ),
            row=2, col=1,
        )

    # --- Angular Velocity LOCAL frame (bottom-right) ---
    for i, (label, color) in enumerate([("ωx", "red"), ("ωy", "green"), ("ωz", "blue")]):
        fig.add_trace(
            go.Scatter(
                x=timestamps, y=omega_local[:, i],
                mode="lines", line=dict(color=color, width=2),
                name=f"{label} (local)",
                showlegend=False,
            ),
            row=2, col=2,
        )

    # Layout
    fig.update_layout(
        title="World vs Local Frame Angular Velocity",
        height=900,
        showlegend=True,
    )

    fig.update_xaxes(title_text="Time (s)", row=2, col=1)
    fig.update_xaxes(title_text="Time (s)", row=2, col=2)
    fig.update_yaxes(title_text="ω (rad/s)", row=2, col=1)
    fig.update_yaxes(title_text="ω (rad/s)", row=2, col=2)

    # Save
    output_path = Path("world_vs_local_omega.html")
    fig.write_html(str(output_path))
    print(f"Saved to: {output_path}")

    # Also save CSV
    df = pd.DataFrame({
        "time": timestamps,
        "omega_world_x": omega_world[:, 0],
        "omega_world_y": omega_world[:, 1],
        "omega_world_z": omega_world[:, 2],
        "omega_local_x": omega_local[:, 0],
        "omega_local_y": omega_local[:, 1],
        "omega_local_z": omega_local[:, 2],
    })
    csv_path = Path("angular_velocity_frames.csv")
    df.to_csv(csv_path, index=False)
    print(f"Saved to: {csv_path}")

    print("\nKey insight:")
    print("  - World frame ω: rotation expressed in fixed world axes")
    print("  - Local frame ω: rotation as experienced BY the body")
    print("  - When body is tilted, these differ!")
    print("  - Sensors attached to the body measure LOCAL frame")


if __name__ == "__main__":
    main()