"""
Ferret Head Kinematics Analysis
================================

This script analyzes the ferret skull motion data to compute:
1. Angular velocity in world (global) frame
2. Angular velocity in local (body) frame  
3. Euler angles (pitch, roll, yaw) in both frames

Uses quaternion mathematics for robust rotation handling.
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
    """Unit quaternion for rotations. Convention: scalar-first [w, x, y, z]."""
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
    def from_rotation_matrix(cls, R: NDArray[np.float64]) -> "Quaternion":
        R = np.asarray(R, dtype=np.float64)
        trace = R[0, 0] + R[1, 1] + R[2, 2]
        
        if trace > 0:
            s = 0.5 / np.sqrt(trace + 1.0)
            w = 0.25 / s
            x = (R[2, 1] - R[1, 2]) * s
            y = (R[0, 2] - R[2, 0]) * s
            z = (R[1, 0] - R[0, 1]) * s
        elif R[0, 0] > R[1, 1] and R[0, 0] > R[2, 2]:
            s = 2.0 * np.sqrt(1.0 + R[0, 0] - R[1, 1] - R[2, 2])
            w = (R[2, 1] - R[1, 2]) / s
            x = 0.25 * s
            y = (R[0, 1] + R[1, 0]) / s
            z = (R[0, 2] + R[2, 0]) / s
        elif R[1, 1] > R[2, 2]:
            s = 2.0 * np.sqrt(1.0 + R[1, 1] - R[0, 0] - R[2, 2])
            w = (R[0, 2] - R[2, 0]) / s
            x = (R[0, 1] + R[1, 0]) / s
            y = 0.25 * s
            z = (R[1, 2] + R[2, 1]) / s
        else:
            s = 2.0 * np.sqrt(1.0 + R[2, 2] - R[0, 0] - R[1, 1])
            w = (R[1, 0] - R[0, 1]) / s
            x = (R[0, 2] + R[2, 0]) / s
            y = (R[1, 2] + R[2, 1]) / s
            z = 0.25 * s
            
        return cls(w=w, x=x, y=y, z=z)

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
        v = np.asarray(v, dtype=np.float64)
        u = np.array([self.x, self.y, self.z])
        uv = np.cross(u, v)
        uuv = np.cross(u, uv)
        return v + 2.0 * (self.w * uv + uuv)

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

    def to_euler_xyz(self) -> tuple[float, float, float]:
        sinr_cosp = 2.0 * (self.w * self.x + self.y * self.z)
        cosr_cosp = 1.0 - 2.0 * (self.x * self.x + self.y * self.y)
        roll = np.arctan2(sinr_cosp, cosr_cosp)
        
        sinp = 2.0 * (self.w * self.y - self.z * self.x)
        sinp = np.clip(sinp, -1.0, 1.0)
        pitch = np.arcsin(sinp)
        
        siny_cosp = 2.0 * (self.w * self.z + self.x * self.y)
        cosy_cosp = 1.0 - 2.0 * (self.y * self.y + self.z * self.z)
        yaw = np.arctan2(siny_cosp, cosy_cosp)
        
        return roll, pitch, yaw


# =============================================================================
# ANGULAR VELOCITY COMPUTATION
# =============================================================================

def compute_omega_world(q1: Quaternion, q2: Quaternion, dt: float) -> NDArray[np.float64]:
    if dt <= 0:
        raise ValueError(f"dt must be positive, got {dt}")
    
    delta_q = q2 * q1.inverse()
    if delta_q.w < 0:
        delta_q = Quaternion(w=-delta_q.w, x=-delta_q.x, y=-delta_q.y, z=-delta_q.z)
    
    axis, angle = delta_q.to_axis_angle()
    return (angle / dt) * axis


def omega_world_to_local(omega_world: NDArray[np.float64], q: Quaternion) -> NDArray[np.float64]:
    return q.inverse().rotate_vector(omega_world)


# =============================================================================
# DATA LOADING
# =============================================================================


def extract_rotation_matrix(row: pd.Series) -> NDArray[np.float64]:
    return np.array([
        [row['rotation_r0_c0'], row['rotation_r0_c1'], row['rotation_r0_c2']],
        [row['rotation_r1_c0'], row['rotation_r1_c1'], row['rotation_r1_c2']],
        [row['rotation_r2_c0'], row['rotation_r2_c1'], row['rotation_r2_c2']],
    ], dtype=np.float64)


# =============================================================================
# MAIN ANALYSIS
# =============================================================================

def analyze_ferret_head_kinematics(rotation_data_path: str | Path) -> pd.DataFrame:
    print("Loading rotation data...")
    df = pd.read_csv(rotation_data_path)
    n_frames = len(df)
    print(f"Processing {n_frames} frames...")
    
    quaternions: list[Quaternion] = []
    timestamps = df['timestamp'].values
    
    print("Converting rotation matrices to quaternions...")
    for _, row in df.iterrows():
        R = extract_rotation_matrix(row)
        q = Quaternion.from_rotation_matrix(R)
        quaternions.append(q)
    
    print("Ensuring quaternion continuity...")
    for i in range(1, n_frames):
        q_prev = quaternions[i - 1]
        q_curr = quaternions[i]
        dot = q_prev.w * q_curr.w + q_prev.x * q_curr.x + q_prev.y * q_curr.y + q_prev.z * q_curr.z
        if dot < 0:
            quaternions[i] = Quaternion(w=-q_curr.w, x=-q_curr.x, y=-q_curr.y, z=-q_curr.z)
    
    print("Computing angular velocities...")
    omega_world = np.zeros((n_frames, 3))
    omega_local = np.zeros((n_frames, 3))
    
    for i in range(n_frames):
        if i == 0:
            dt = timestamps[1] - timestamps[0]
            ow = compute_omega_world(quaternions[0], quaternions[1], dt)
        elif i == n_frames - 1:
            dt = timestamps[-1] - timestamps[-2]
            ow = compute_omega_world(quaternions[-2], quaternions[-1], dt)
        else:
            dt = timestamps[i + 1] - timestamps[i - 1]
            ow = compute_omega_world(quaternions[i - 1], quaternions[i + 1], dt)
        
        omega_world[i] = ow
        omega_local[i] = omega_world_to_local(ow, quaternions[i])
    
    print("Extracting Euler angles...")
    euler_world = np.zeros((n_frames, 3))
    for i, q in enumerate(quaternions):
        euler_world[i] = q.to_euler_xyz()
    
    return pd.DataFrame({
        'timestamp': timestamps,
        'omega_world_x': omega_world[:, 0],
        'omega_world_y': omega_world[:, 1],
        'omega_world_z': omega_world[:, 2],
        'omega_local_x': omega_local[:, 0],
        'omega_local_y': omega_local[:, 1],
        'omega_local_z': omega_local[:, 2],
        'euler_world_x_roll_rad': euler_world[:, 0],
        'euler_world_y_pitch_rad': euler_world[:, 1],
        'euler_world_z_yaw_rad': euler_world[:, 2],
    })


# =============================================================================
# VISUALIZATION
# =============================================================================

def create_visualization(result_df: pd.DataFrame, output_path: Path) -> None:
    t = result_df['timestamp'].values - result_df['timestamp'].values[0]
    colors = {'x': '#e74c3c', 'y': '#2ecc71', 'z': '#3498db'}
    
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.08,
                        subplot_titles=('Euler Angles (Global)', 'Angular Velocity (Global)', 'Angular Velocity (Local)'))
    
    # Euler angles
    fig.add_trace(go.Scatter(x=t, y=result_df['roll_deg'], name='Roll', mode='lines+markers', line=dict(color=colors['x'], width=1), marker=dict(size=2)), row=1, col=1)
    fig.add_trace(go.Scatter(x=t, y=result_df['pitch_deg'], name='Pitch', mode='lines+markers', line=dict(color=colors['y'], width=1), marker=dict(size=2)), row=1, col=1)
    fig.add_trace(go.Scatter(x=t, y=result_df['yaw_deg'], name='Yaw', mode='lines+markers', line=dict(color=colors['z'], width=1), marker=dict(size=2)), row=1, col=1)
    
    # Global angular velocity
    fig.add_trace(go.Scatter(x=t, y=result_df['omega_world_x'], name='ωx', mode='lines+markers', line=dict(color=colors['x'], width=1), marker=dict(size=2), showlegend=False), row=2, col=1)
    fig.add_trace(go.Scatter(x=t, y=result_df['omega_world_y'], name='ωy', mode='lines+markers', line=dict(color=colors['y'], width=1), marker=dict(size=2), showlegend=False), row=2, col=1)
    fig.add_trace(go.Scatter(x=t, y=result_df['omega_world_z'], name='ωz', mode='lines+markers', line=dict(color=colors['z'], width=1), marker=dict(size=2), showlegend=False), row=2, col=1)
    
    # Local angular velocity
    fig.add_trace(go.Scatter(x=t, y=result_df['omega_local_x'], name='ωx', mode='lines+markers', line=dict(color=colors['x'], width=1), marker=dict(size=2), showlegend=False), row=3, col=1)
    fig.add_trace(go.Scatter(x=t, y=result_df['omega_local_y'], name='ωy', mode='lines+markers', line=dict(color=colors['y'], width=1), marker=dict(size=2), showlegend=False), row=3, col=1)
    fig.add_trace(go.Scatter(x=t, y=result_df['omega_local_z'], name='ωz', mode='lines+markers', line=dict(color=colors['z'], width=1), marker=dict(size=2), showlegend=False), row=3, col=1)
    
    fig.update_yaxes(title_text='degrees', row=1, col=1)
    fig.update_yaxes(title_text='rad/s', row=2, col=1)
    fig.update_yaxes(title_text='rad/s', row=3, col=1)
    fig.update_xaxes(title_text='Time (s)', row=3, col=1)
    
    fig.update_layout(title='Ferret Head Kinematics', height=800, template='plotly_white')
    
    output_html = output_path.with_suffix('.html')
    fig.write_html(str(output_html))
    print(f"Saved: {output_html}")

# =============================================================================
# MAIN
# =============================================================================

def main(head_rotation_translation_csv_path: str) -> None:
    input_path = Path(head_rotation_translation_csv_path)
    result_df = analyze_ferret_head_kinematics(input_path)
    
    output_csv = input_path.parent / "ferret_head_kinematics.csv"
    result_df.to_csv(output_csv, index=False)
    print(f"Saved: {output_csv}")
    
    create_visualization(result_df, input_path.parent / "ferret_head_kinematics_visualization")


if __name__ == "__main__":
    head_rotation_translation_csv_path = r"D:\bs\ferret_recordings\clips\0m_37s-1m_37s\mocap_data\output_data\solver_output\rotation_translation_data.csv"
    main(head_rotation_translation_csv_path)