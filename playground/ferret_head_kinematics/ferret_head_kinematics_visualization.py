# =============================================================================
# FERRET HEAD KINEMATICS VISUALIZATION (RERUN) - COLUMNAR API VERSION
# =============================================================================
"""
Interactive visualization with Rerun using columnar data loading:
- 3D skeleton viewer with animation
- Time series plots (Euler angles, angular velocities)
- Timeline scrubbing and playback controls

Uses send_columns API for much faster data ingestion.
"""
from pathlib import Path

import numpy as np
import pandas as pd
import rerun as rr
from numpy.typing import NDArray

# =============================================================================
# TOPOLOGY DEFINITION
# =============================================================================
MARKER_NAMES: list[str] = [
    "nose",
    "left_eye",
    "right_eye",
    "left_ear",
    "right_ear",
    "base",
    "left_cam_tip",
    "right_cam_tip",
    "spine_t1",
    "sacrum",
    "tail_tip",
]

DISPLAY_EDGES: list[tuple[int, int]] = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 4),
    (3, 4),
    (3, 5),
    (4, 5),
    (5, 6),
    (5, 7),
    (3, 8),
    (4, 8),
    (8, 9),
    (9, 10),
]

# RGB colors (0-255)
MARKER_COLORS: dict[str, tuple[int, int, int]] = {
    "nose": (255, 107, 107),
    "left_eye": (78, 205, 196),
    "right_eye": (78, 205, 196),
    "left_ear": (149, 225, 211),
    "right_ear": (149, 225, 211),
    "base": (255, 230, 109),
    "left_cam_tip": (168, 230, 207),
    "right_cam_tip": (168, 230, 207),
    "spine_t1": (221, 160, 221),
    "sacrum": (221, 160, 221),
    "tail_tip": (221, 160, 221),
}

AXIS_COLORS: dict[str, tuple[int, int, int]] = {
    "x": (255, 107, 107),  # red
    "y": (78, 205, 196),  # cyan
    "z": (255, 230, 109),  # yellow
}


# =============================================================================
# DATA LOADING
# =============================================================================
def load_trajectory_data(
        trajectory_csv_path: Path,
) -> dict[int, dict[str, NDArray[np.float64]]]:
    """Load trajectory data from CSV and organize by frame."""
    df = pd.read_csv(trajectory_csv_path)

    frames: dict[int, dict[str, NDArray[np.float64]]] = {}

    for frame_idx in df["frame"].unique():
        frame_data = df[df["frame"] == frame_idx]
        frames[int(frame_idx)] = {}

        for _, row in frame_data.iterrows():
            marker = str(row["marker"])
            data_type = str(row["data_type"])
            # Use optimized data if available, otherwise noisy
            if data_type == "optimized":
                frames[int(frame_idx)][marker] = np.array(
                    [row["x"], row["y"], row["z"]], dtype=np.float64
                )
            elif marker not in frames[int(frame_idx)]:
                frames[int(frame_idx)][marker] = np.array(
                    [row["x"], row["y"], row["z"]], dtype=np.float64
                )

    return frames


# =============================================================================
# COLUMNAR DATA PREPARATION
# =============================================================================
def prepare_skeleton_columns(
        trajectory_data: dict[int, dict[str, NDArray[np.float64]]],
        timestamps: NDArray[np.float64],
        t0: float,
        marker_names: list[str],
        display_edges: list[tuple[int, int]],
) -> tuple[
    list[float],  # times for markers
    list[NDArray[np.float64]],  # all marker positions flattened
    list[int],  # partition lengths for markers
    list[NDArray[np.uint8]],  # all marker colors flattened
    list[str],  # all marker labels flattened
    list[float],  # times for edges
    list[NDArray[np.float64]],  # all edge strips flattened
    list[int],  # partition lengths for edges (strips per timestep)
]:
    """
    Prepare skeleton data in columnar format for send_columns.

    Returns data structures needed for efficient columnar logging.
    """
    available_traj_frames = sorted(trajectory_data.keys())

    # Collect all data across all timesteps
    marker_times: list[float] = []
    all_positions: list[NDArray[np.float64]] = []
    marker_partition_lengths: list[int] = []
    all_colors: list[NDArray[np.uint8]] = []
    all_labels: list[str] = []

    edge_times: list[float] = []
    all_edge_strips: list[NDArray[np.float64]] = []
    edge_partition_lengths: list[int] = []

    for i, ts in enumerate(timestamps):
        time_val = float(ts - t0)

        # Find closest trajectory frame
        closest_traj_frames = [f for f in available_traj_frames if f <= i]
        if closest_traj_frames:
            closest_traj_frame = max(closest_traj_frames)
        else:
            closest_traj_frame = available_traj_frames[0]

        frame_data = trajectory_data[closest_traj_frame]

        # Collect marker data for this frame
        frame_positions: list[NDArray[np.float64]] = []
        frame_colors: list[NDArray[np.uint8]] = []
        frame_labels: list[str] = []

        for name in marker_names:
            if name in frame_data:
                pos = frame_data[name]
                if not np.any(np.isnan(pos)):
                    frame_positions.append(pos)
                    color = MARKER_COLORS.get(name, (255, 255, 255))
                    frame_colors.append(np.array(color, dtype=np.uint8))
                    frame_labels.append(name)

        if frame_positions:
            marker_times.append(time_val)
            all_positions.extend(frame_positions)
            all_colors.extend(frame_colors)
            all_labels.extend(frame_labels)
            marker_partition_lengths.append(len(frame_positions))

        # Collect edge data for this frame
        frame_strips: list[NDArray[np.float64]] = []

        for idx_i, idx_j in display_edges:
            name_i = marker_names[idx_i]
            name_j = marker_names[idx_j]
            if name_i in frame_data and name_j in frame_data:
                pos_i = frame_data[name_i]
                pos_j = frame_data[name_j]
                if not np.any(np.isnan(pos_i)) and not np.any(np.isnan(pos_j)):
                    # Each strip is a 2-point line segment
                    strip = np.array([pos_i, pos_j], dtype=np.float64)
                    frame_strips.append(strip)

        if frame_strips:
            edge_times.append(time_val)
            all_edge_strips.extend(frame_strips)
            edge_partition_lengths.append(len(frame_strips))

    return (
        marker_times,
        all_positions,
        marker_partition_lengths,
        all_colors,
        all_labels,
        edge_times,
        all_edge_strips,
        edge_partition_lengths,
    )


def send_skeleton_columns(
        trajectory_data: dict[int, dict[str, NDArray[np.float64]]],
        timestamps: NDArray[np.float64],
        t0: float,
        marker_names: list[str],
        display_edges: list[tuple[int, int]],
) -> None:
    """Send skeleton data using columnar API."""
    (
        marker_times,
        all_positions,
        marker_partition_lengths,
        all_colors,
        all_labels,
        edge_times,
        all_edge_strips,
        edge_partition_lengths,
    ) = prepare_skeleton_columns(
        trajectory_data=trajectory_data,
        timestamps=timestamps,
        t0=t0,
        marker_names=marker_names,
        display_edges=display_edges,
    )

    # Send marker points using columnar API
    if marker_times and all_positions:
        positions_array = np.array(all_positions)
        colors_array = np.array(all_colors)

        rr.send_columns(
            "skeleton/markers",
            indexes=[rr.TimeColumn("time", duration=marker_times)],
            columns=[
                *rr.Points3D.columns(positions=positions_array).partition(
                    lengths=marker_partition_lengths
                ),
                *rr.Points3D.columns(
                    colors=colors_array,
                    radii=[8.0] * len(all_positions),
                    labels=all_labels,
                ).partition(lengths=marker_partition_lengths),
            ],
        )

    # Send edge line strips using columnar API
    if edge_times and all_edge_strips:
        rr.send_columns(
            "skeleton/edges",
            indexes=[rr.TimeColumn("time", duration=edge_times)],
            columns=[
                *rr.LineStrips3D.columns(
                    strips=all_edge_strips,
                    colors=[(0, 255, 200)] * len(all_edge_strips),
                    radii=[2.0] * len(all_edge_strips),
                ).partition(lengths=edge_partition_lengths),
            ],
        )


def send_time_series_columns(
        result_df: pd.DataFrame,
        has_body_relative: bool,
) -> None:
    """Send all time series data at once using columnar API."""
    timestamps = result_df["timestamp"].values
    t0 = timestamps[0]
    times = timestamps - t0
    n_frames = len(times)

    # Convert Euler angles to degrees
    euler_world_roll_deg = np.rad2deg(result_df["euler_world_roll_rad"].values)
    euler_world_pitch_deg = np.rad2deg(result_df["euler_world_pitch_rad"].values)
    euler_world_yaw_deg = np.rad2deg(result_df["euler_world_yaw_rad"].values)

    # Send Euler angles (world) using columnar API
    rr.send_columns(
        "euler_world/roll_deg",
        indexes=[rr.TimeColumn("time", duration=times)],
        columns=rr.Scalars.columns(scalars=euler_world_roll_deg),
    )
    rr.send_columns(
        "euler_world/pitch_deg",
        indexes=[rr.TimeColumn("time", duration=times)],
        columns=rr.Scalars.columns(scalars=euler_world_pitch_deg),
    )
    rr.send_columns(
        "euler_world/yaw_deg",
        indexes=[rr.TimeColumn("time", duration=times)],
        columns=rr.Scalars.columns(scalars=euler_world_yaw_deg),
    )

    # Send angular velocity (world)
    rr.send_columns(
        "omega_world/x",
        indexes=[rr.TimeColumn("time", duration=times)],
        columns=rr.Scalars.columns(scalars=result_df["omega_world_x"].values),
    )
    rr.send_columns(
        "omega_world/y",
        indexes=[rr.TimeColumn("time", duration=times)],
        columns=rr.Scalars.columns(scalars=result_df["omega_world_y"].values),
    )
    rr.send_columns(
        "omega_world/z",
        indexes=[rr.TimeColumn("time", duration=times)],
        columns=rr.Scalars.columns(scalars=result_df["omega_world_z"].values),
    )

    if has_body_relative:
        # Euler angles (body-relative)
        euler_body_roll_deg = np.rad2deg(
            result_df["euler_body_relative_roll_rad"].values
        )
        euler_body_pitch_deg = np.rad2deg(
            result_df["euler_body_relative_pitch_rad"].values
        )
        euler_body_yaw_deg = np.rad2deg(
            result_df["euler_body_relative_yaw_rad"].values
        )

        rr.send_columns(
            "euler_body/roll_deg",
            indexes=[rr.TimeColumn("time", duration=times)],
            columns=rr.Scalars.columns(scalars=euler_body_roll_deg),
        )
        rr.send_columns(
            "euler_body/pitch_deg",
            indexes=[rr.TimeColumn("time", duration=times)],
            columns=rr.Scalars.columns(scalars=euler_body_pitch_deg),
        )
        rr.send_columns(
            "euler_body/yaw_deg",
            indexes=[rr.TimeColumn("time", duration=times)],
            columns=rr.Scalars.columns(scalars=euler_body_yaw_deg),
        )

        # Angular velocity (body-relative)
        rr.send_columns(
            "omega_body/x",
            indexes=[rr.TimeColumn("time", duration=times)],
            columns=rr.Scalars.columns(
                scalars=result_df["omega_body_relative_x"].values
            ),
        )
        rr.send_columns(
            "omega_body/y",
            indexes=[rr.TimeColumn("time", duration=times)],
            columns=rr.Scalars.columns(
                scalars=result_df["omega_body_relative_y"].values
            ),
        )
        rr.send_columns(
            "omega_body/z",
            indexes=[rr.TimeColumn("time", duration=times)],
            columns=rr.Scalars.columns(
                scalars=result_df["omega_body_relative_z"].values
            ),
        )
    else:
        # Angular velocity (head-local)
        rr.send_columns(
            "omega_local/x",
            indexes=[rr.TimeColumn("time", duration=times)],
            columns=rr.Scalars.columns(
                scalars=result_df["omega_head_local_x"].values
            ),
        )
        rr.send_columns(
            "omega_local/y",
            indexes=[rr.TimeColumn("time", duration=times)],
            columns=rr.Scalars.columns(
                scalars=result_df["omega_head_local_y"].values
            ),
        )
        rr.send_columns(
            "omega_local/z",
            indexes=[rr.TimeColumn("time", duration=times)],
            columns=rr.Scalars.columns(
                scalars=result_df["omega_head_local_z"].values
            ),
        )


# =============================================================================
# RERUN STYLING AND BLUEPRINT
# =============================================================================
def setup_plot_styling(has_body_relative: bool) -> None:
    """Configure plot colors and styling using blueprints."""
    # Set up series line colors
    rr.log(
        "euler_world/roll_deg",
        rr.SeriesLines(colors=AXIS_COLORS["x"], names="Roll"),
        static=True,
    )
    rr.log(
        "euler_world/pitch_deg",
        rr.SeriesLines(colors=AXIS_COLORS["y"], names="Pitch"),
        static=True,
    )
    rr.log(
        "euler_world/yaw_deg",
        rr.SeriesLines(colors=AXIS_COLORS["z"], names="Yaw"),
        static=True,
    )

    rr.log(
        "omega_world/x",
        rr.SeriesLines(colors=AXIS_COLORS["x"], names="ωx"),
        static=True,
    )
    rr.log(
        "omega_world/y",
        rr.SeriesLines(colors=AXIS_COLORS["y"], names="ωy"),
        static=True,
    )
    rr.log(
        "omega_world/z",
        rr.SeriesLines(colors=AXIS_COLORS["z"], names="ωz"),
        static=True,
    )

    if has_body_relative:
        rr.log(
            "euler_body/roll_deg",
            rr.SeriesLines(colors=AXIS_COLORS["x"], names="Roll"),
            static=True,
        )
        rr.log(
            "euler_body/pitch_deg",
            rr.SeriesLines(colors=AXIS_COLORS["y"], names="Pitch"),
            static=True,
        )
        rr.log(
            "euler_body/yaw_deg",
            rr.SeriesLines(colors=AXIS_COLORS["z"], names="Yaw"),
            static=True,
        )

        rr.log(
            "omega_body/x",
            rr.SeriesLines(colors=AXIS_COLORS["x"], names="ωx"),
            static=True,
        )
        rr.log(
            "omega_body/y",
            rr.SeriesLines(colors=AXIS_COLORS["y"], names="ωy"),
            static=True,
        )
        rr.log(
            "omega_body/z",
            rr.SeriesLines(colors=AXIS_COLORS["z"], names="ωz"),
            static=True,
        )
    else:
        rr.log(
            "omega_local/x",
            rr.SeriesLines(colors=AXIS_COLORS["x"], names="ωx"),
            static=True,
        )
        rr.log(
            "omega_local/y",
            rr.SeriesLines(colors=AXIS_COLORS["y"], names="ωy"),
            static=True,
        )
        rr.log(
            "omega_local/z",
            rr.SeriesLines(colors=AXIS_COLORS["z"], names="ωz"),
            static=True,
        )


def create_blueprint(has_body_relative: bool) -> rr.blueprint.Blueprint:
    """Create a Rerun blueprint for the visualization layout."""
    time_series_panels: list[rr.blueprint.TimeSeriesView] = [
        rr.blueprint.TimeSeriesView(
            name="Euler Angles (World, deg)",
            origin="euler_world",
        ),
    ]

    if has_body_relative:
        time_series_panels.append(
            rr.blueprint.TimeSeriesView(
                name="Euler Angles (Body-Relative, deg)",
                origin="euler_body",
            )
        )
        time_series_panels.append(
            rr.blueprint.TimeSeriesView(
                name="Angular Velocity (World, rad/s)",
                origin="omega_world",
            )
        )
        time_series_panels.append(
            rr.blueprint.TimeSeriesView(
                name="Angular Velocity (Body-Relative, rad/s)",
                origin="omega_body",
            )
        )
    else:
        time_series_panels.append(
            rr.blueprint.TimeSeriesView(
                name="Angular Velocity (World, rad/s)",
                origin="omega_world",
            )
        )
        time_series_panels.append(
            rr.blueprint.TimeSeriesView(
                name="Angular Velocity (Head-Local, rad/s)",
                origin="omega_local",
            )
        )

    # Configure the 3D view for mm-scale data (~1m³ cube = 1000mm)
    # Camera positioned to view the whole scene
    spatial_3d_view = rr.blueprint.Spatial3DView(
        name="3D Skeleton",
        origin="skeleton",
        # Background color (dark gray)
        background=[30, 30, 30],
        # Configure eye/camera to view ~1m³ scene (data in mm)
        eye_controls=rr.blueprint.EyeControls3D(
            # Position camera ~2m back to see 1m³ cube
            position=(0.0, -2000.0, 500.0),
            # Look at center of scene
            look_target=(0.0, 0.0, 0.0),
            # Z-up coordinate system
            eye_up=(0.0, 0.0, 1.0),
        ),
        # Configure grid for mm-scale (100mm = 10cm spacing)
        line_grid=rr.blueprint.LineGrid3D(
            visible=True,
            spacing=100.0,  # 100mm = 10cm grid lines
            plane=rr.components.Plane3D.XY,
            color=[100, 100, 100, 128],
        ),
        # Show axes and bounding box for reference
        spatial_information=rr.blueprint.SpatialInformation(
            show_axes=True,
            show_bounding_box=True,
        ),
    )

    return rr.blueprint.Blueprint(
        rr.blueprint.Horizontal(
            spatial_3d_view,
            rr.blueprint.Vertical(*time_series_panels),
            column_shares=[1, 1],
        ),
        collapse_panels=True,
    )


# =============================================================================
# MAIN VISUALIZATION FUNCTION
# =============================================================================
def run_visualization(
        result_df: pd.DataFrame,
        has_body_relative: bool,
        trajectory_data: dict[int, dict[str, NDArray[np.float64]]] | None,
        application_id: str = "ferret_head_kinematics",
        spawn: bool = True,
) -> None:
    """
    Run the Rerun visualization using columnar data loading.

    Args:
        result_df: DataFrame with kinematics data
        has_body_relative: Whether body-relative data is present
        trajectory_data: Optional trajectory data for 3D skeleton
        application_id: Rerun application ID
        spawn: Whether to spawn the Rerun viewer
    """
    rr.init(application_id)

    blueprint = create_blueprint(has_body_relative)

    if spawn:
        rr.spawn()

    rr.send_blueprint(blueprint)

    # Set up styling (static data)
    setup_plot_styling(has_body_relative)

    timestamps = result_df["timestamp"].values
    t0 = timestamps[0]
    n_frames = len(timestamps)

    print(f"Logging {n_frames} frames using columnar API...")

    # Send all time series data at once using columnar API
    print("  Sending time series data...")
    send_time_series_columns(
        result_df=result_df,
        has_body_relative=has_body_relative,
    )

    # Send skeleton data if available
    if trajectory_data is not None:
        print("  Sending skeleton data...")
        send_skeleton_columns(
            trajectory_data=trajectory_data,
            timestamps=timestamps,
            t0=t0,
            marker_names=MARKER_NAMES,
            display_edges=DISPLAY_EDGES,
        )

    print("Done!")


def run_visualization_from_files(
        kinematics_csv_path: Path,
        trajectory_csv_path: Path | None,
        application_id: str = "ferret_head_kinematics",
        spawn: bool = True,
) -> None:
    """Run visualization from CSV files."""
    result_df = pd.read_csv(kinematics_csv_path)

    trajectory_data: dict[int, dict[str, NDArray[np.float64]]] | None = None
    if trajectory_csv_path is not None and trajectory_csv_path.exists():
        trajectory_data = load_trajectory_data(trajectory_csv_path)

    has_body_relative = "euler_body_relative_roll_rad" in result_df.columns

    run_visualization(
        result_df=result_df,
        has_body_relative=has_body_relative,
        trajectory_data=trajectory_data,
        application_id=application_id,
        spawn=spawn,
    )