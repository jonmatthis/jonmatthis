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
import matplotlib.pyplot as plt
import matplotlib



# =============================================================================
# QUATERNION CLASS (Extended with rotation matrix and Euler conversions)
# =============================================================================

@dataclass
class Quaternion:
    """
    Unit quaternion for rotations. Convention: scalar-first [w, x, y, z].
    """
    w: float
    x: float
    y: float
    z: float

    def __post_init__(self) -> None:
        """Normalize to ensure unit quaternion."""
        norm = np.sqrt(self.w ** 2 + self.x ** 2 + self.y ** 2 + self.z ** 2)
        if norm < 1e-10:
            raise ValueError("Cannot normalize zero quaternion")
        self.w /= norm
        self.x /= norm
        self.y /= norm
        self.z /= norm

    @classmethod
    def identity(cls) -> "Quaternion":
        """Return identity quaternion (no rotation)."""
        return cls(w=1.0, x=0.0, y=0.0, z=0.0)

    @classmethod
    def _from_components_no_normalize(cls, w: float, x: float, y: float, z: float) -> "Quaternion":
        """Create quaternion without normalizing (internal use for pure quaternions)."""
        q = object.__new__(cls)
        q.w = w
        q.x = x
        q.y = y
        q.z = z
        return q

    @classmethod
    def from_rotation_matrix(cls, R: NDArray[np.float64]) -> "Quaternion":
        """
        Convert a 3x3 rotation matrix to quaternion using Shepperd's method.
        
        This is numerically stable for all rotation matrices.
        
        Args:
            R: 3x3 rotation matrix
            
        Returns:
            Equivalent unit quaternion
        """
        R = np.asarray(R, dtype=np.float64)
        
        # Shepperd's method - chooses the largest diagonal element to avoid
        # numerical instability near singularities
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

    @classmethod
    def from_axis_angle(cls, axis: NDArray[np.float64], angle_rad: float) -> "Quaternion":
        """Create quaternion from axis-angle representation."""
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

    def conjugate(self) -> "Quaternion":
        """Return conjugate q* = (w, -x, -y, -z)."""
        return Quaternion(w=self.w, x=-self.x, y=-self.y, z=-self.z)

    def inverse(self) -> "Quaternion":
        """Return inverse (for unit quaternions, same as conjugate)."""
        return self.conjugate()

    def __mul__(self, other: "Quaternion") -> "Quaternion":
        """Quaternion multiplication (Hamilton product)."""
        w1, x1, y1, z1 = self.w, self.x, self.y, self.z
        w2, x2, y2, z2 = other.w, other.x, other.y, other.z
        return Quaternion(
            w=w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
            x=w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
            y=w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
            z=w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2,
        )

    def rotate_vector(self, v: NDArray[np.float64]) -> NDArray[np.float64]:
        """
        Rotate vector v by this quaternion: v' = q * v * q⁻¹
        
        Uses the optimized formula to avoid creating intermediate quaternions
        and preserve vector magnitude.
        """
        v = np.asarray(v, dtype=np.float64)
        
        # Optimized rotation formula (Rodrigues-like)
        # v' = v + 2*w*(u × v) + 2*(u × (u × v))
        # where u = (x, y, z) is the vector part of the quaternion
        u = np.array([self.x, self.y, self.z])
        uv = np.cross(u, v)
        uuv = np.cross(u, uv)
        return v + 2.0 * (self.w * uv + uuv)

    def to_axis_angle(self) -> tuple[NDArray[np.float64], float]:
        """Extract axis-angle representation from quaternion."""
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
        """
        Convert quaternion to Euler angles (XYZ intrinsic / roll-pitch-yaw).
        
        Returns:
            tuple: (roll, pitch, yaw) in radians
            - roll: rotation about X axis
            - pitch: rotation about Y axis  
            - yaw: rotation about Z axis
        """
        # Roll (x-axis rotation)
        sinr_cosp = 2.0 * (self.w * self.x + self.y * self.z)
        cosr_cosp = 1.0 - 2.0 * (self.x * self.x + self.y * self.y)
        roll = np.arctan2(sinr_cosp, cosr_cosp)
        
        # Pitch (y-axis rotation)
        sinp = 2.0 * (self.w * self.y - self.z * self.x)
        sinp = np.clip(sinp, -1.0, 1.0)  # Clamp for numerical stability
        pitch = np.arcsin(sinp)
        
        # Yaw (z-axis rotation)
        siny_cosp = 2.0 * (self.w * self.z + self.x * self.y)
        cosy_cosp = 1.0 - 2.0 * (self.y * self.y + self.z * self.z)
        yaw = np.arctan2(siny_cosp, cosy_cosp)
        
        return roll, pitch, yaw

    def to_rotation_matrix(self) -> NDArray[np.float64]:
        """Convert quaternion to 3x3 rotation matrix."""
        w, x, y, z = self.w, self.x, self.y, self.z
        
        return np.array([
            [1 - 2*(y*y + z*z), 2*(x*y - w*z), 2*(x*z + w*y)],
            [2*(x*y + w*z), 1 - 2*(x*x + z*z), 2*(y*z - w*x)],
            [2*(x*z - w*y), 2*(y*z + w*x), 1 - 2*(x*x + y*y)]
        ], dtype=np.float64)


# =============================================================================
# ANGULAR VELOCITY COMPUTATION
# =============================================================================

def compute_omega_world(q1: Quaternion, q2: Quaternion, dt: float) -> NDArray[np.float64]:
    """
    Compute angular velocity in WORLD frame from two quaternions.
    
    The incremental rotation from q1 to q2 is: Δq = q2 * q1⁻¹
    This represents rotation as seen by a stationary world observer.
    """
    if dt <= 0:
        raise ValueError(f"dt must be positive, got {dt}")
    
    delta_q = q2 * q1.inverse()
    
    # Ensure short path
    if delta_q.w < 0:
        delta_q = Quaternion(w=-delta_q.w, x=-delta_q.x, y=-delta_q.y, z=-delta_q.z)
    
    axis, angle = delta_q.to_axis_angle()
    return (angle / dt) * axis


def omega_world_to_local(omega_world: NDArray[np.float64], q: Quaternion) -> NDArray[np.float64]:
    """
    Transform angular velocity from world frame to body-local frame.
    
    ω_local = q⁻¹ * ω_world
    
    This is what a gyroscope attached to the body would measure!
    """
    return q.inverse().rotate_vector(omega_world)


def omega_local_to_world(omega_local: NDArray[np.float64], q: Quaternion) -> NDArray[np.float64]:
    """
    Transform angular velocity from body-local frame to world frame.
    
    ω_world = q * ω_local
    """
    return q.rotate_vector(omega_local)


# =============================================================================
# LOCAL EULER ANGLES (relative to body frame)
# =============================================================================

def compute_local_euler_rates(
    omega_local: NDArray[np.float64], 
    roll: float, 
    pitch: float
) -> tuple[float, float, float]:
    """
    Convert local angular velocity to Euler angle rates.
    
    The relationship between angular velocity and Euler rates is:
    [ωx]   [1  0        -sin(pitch)     ] [roll_dot ]
    [ωy] = [0  cos(roll)  sin(roll)cos(pitch)] [pitch_dot]
    [ωz]   [0 -sin(roll)  cos(roll)cos(pitch)] [yaw_dot  ]
    
    We invert this to get the rates from omega.
    
    Note: Near gimbal lock (pitch = ±90°), this becomes singular.
    """
    cp = np.cos(pitch)
    sp = np.sin(pitch)
    cr = np.cos(roll)
    sr = np.sin(roll)
    
    # Avoid gimbal lock
    if abs(cp) < 1e-6:
        # At gimbal lock, we can only determine roll_dot + yaw_dot
        roll_dot = omega_local[0]
        pitch_dot = omega_local[1] * cr - omega_local[2] * sr
        yaw_dot = 0.0  # Undefined, set to 0
    else:
        roll_dot = omega_local[0] + sp * omega_local[2] / cp
        pitch_dot = omega_local[1] * cr + omega_local[2] * sr
        yaw_dot = (-omega_local[1] * sr + omega_local[2] * cr) / cp
    
    return roll_dot, pitch_dot, yaw_dot


# =============================================================================
# DATA LOADING
# =============================================================================

def load_rotation_data(filepath: str | Path) -> pd.DataFrame:
    """Load and parse the rotation/translation CSV data."""
    df = pd.read_csv(filepath)
    return df


def extract_rotation_matrix(row: pd.Series) -> NDArray[np.float64]:
    """Extract 3x3 rotation matrix from a DataFrame row."""
    R = np.array([
        [row['rotation_r0_c0'], row['rotation_r0_c1'], row['rotation_r0_c2']],
        [row['rotation_r1_c0'], row['rotation_r1_c1'], row['rotation_r1_c2']],
        [row['rotation_r2_c0'], row['rotation_r2_c1'], row['rotation_r2_c2']],
    ], dtype=np.float64)
    return R


def extract_translation(row: pd.Series) -> NDArray[np.float64]:
    """Extract translation vector from a DataFrame row."""
    return np.array([
        row['translation_x'],
        row['translation_y'],
        row['translation_z'],
    ], dtype=np.float64)


# =============================================================================
# MAIN ANALYSIS
# =============================================================================

def analyze_ferret_head_kinematics(rotation_data_path: str | Path) -> pd.DataFrame:
    """
    Analyze ferret head kinematics from rotation data.
    
    Computes:
    - Quaternion orientation
    - Angular velocity in world frame (global)
    - Angular velocity in local frame (body)
    - Euler angles (roll, pitch, yaw) in world frame
    
    Args:
        rotation_data_path: Path to the rotation_translation_data.csv file
        
    Returns:
        DataFrame with all computed kinematic quantities
    """
    print("Loading rotation data...")
    df = load_rotation_data(rotation_data_path)
    n_frames = len(df)
    
    print(f"Processing {n_frames} frames...")
    
    # Storage arrays
    quaternions: list[Quaternion] = []
    timestamps = df['timestamp'].values
    translations = np.zeros((n_frames, 3))
    
    # Convert all rotation matrices to quaternions
    print("Converting rotation matrices to quaternions...")
    for idx, row in df.iterrows():
        R = extract_rotation_matrix(row)
        q = Quaternion.from_rotation_matrix(R)
        quaternions.append(q)
        translations[idx] = extract_translation(row)
    
    # Ensure quaternion continuity (avoid sign flips)
    print("Ensuring quaternion continuity...")
    for i in range(1, n_frames):
        q_prev = quaternions[i - 1]
        q_curr = quaternions[i]
        dot = q_prev.w * q_curr.w + q_prev.x * q_curr.x + q_prev.y * q_curr.y + q_prev.z * q_curr.z
        if dot < 0:
            quaternions[i] = Quaternion(w=-q_curr.w, x=-q_curr.x, y=-q_curr.y, z=-q_curr.z)
    
    # Compute angular velocities
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
            # Central difference for better accuracy
            dt = timestamps[i + 1] - timestamps[i - 1]
            ow = compute_omega_world(quaternions[i - 1], quaternions[i + 1], dt)
        
        omega_world[i] = ow
        omega_local[i] = omega_world_to_local(ow, quaternions[i])
    
    # Extract Euler angles (world frame)
    print("Extracting Euler angles...")
    euler_world = np.zeros((n_frames, 3))  # roll, pitch, yaw
    
    for i, q in enumerate(quaternions):
        roll, pitch, yaw = q.to_euler_xyz()
        euler_world[i] = [roll, pitch, yaw]
    
    # Compute local Euler angle rates
    euler_local_rates = np.zeros((n_frames, 3))
    for i in range(n_frames):
        roll_dot, pitch_dot, yaw_dot = compute_local_euler_rates(
            omega_local[i],
            euler_world[i, 0],  # roll
            euler_world[i, 1],  # pitch
        )
        euler_local_rates[i] = [roll_dot, pitch_dot, yaw_dot]
    
    # Build output DataFrame
    print("Building output DataFrame...")
    result_df = pd.DataFrame({
        'frame': df['frame'].values,
        'timestamp': timestamps,
        # Translation
        'translation_x': translations[:, 0],
        'translation_y': translations[:, 1],
        'translation_z': translations[:, 2],
        # Quaternion
        'quat_w': [q.w for q in quaternions],
        'quat_x': [q.x for q in quaternions],
        'quat_y': [q.y for q in quaternions],
        'quat_z': [q.z for q in quaternions],
        # World frame angular velocity (rad/s)
        'omega_world_x': omega_world[:, 0],
        'omega_world_y': omega_world[:, 1],
        'omega_world_z': omega_world[:, 2],
        # Local frame angular velocity (rad/s) - what a gyroscope would measure
        'omega_local_x': omega_local[:, 0],
        'omega_local_y': omega_local[:, 1],
        'omega_local_z': omega_local[:, 2],
        # World frame Euler angles (rad)
        'roll_world_rad': euler_world[:, 0],
        'pitch_world_rad': euler_world[:, 1],
        'yaw_world_rad': euler_world[:, 2],
        # World frame Euler angles (degrees) for convenience
        'roll_world_deg': np.degrees(euler_world[:, 0]),
        'pitch_world_deg': np.degrees(euler_world[:, 1]),
        'yaw_world_deg': np.degrees(euler_world[:, 2]),
        # Local Euler angle rates (rad/s)
        'roll_rate_local': euler_local_rates[:, 0],
        'pitch_rate_local': euler_local_rates[:, 1],
        'yaw_rate_local': euler_local_rates[:, 2],
    })
    
    # Also compute angular velocity magnitudes
    result_df['omega_world_magnitude'] = np.linalg.norm(omega_world, axis=1)
    result_df['omega_local_magnitude'] = np.linalg.norm(omega_local, axis=1)
    
    return result_df


# =============================================================================
# VISUALIZATION
# =============================================================================

def create_visualization(result_df: pd.DataFrame, output_path: Path) -> None:
    """
    Create visualization of ferret head kinematics using matplotlib.
    """
    # Convert timestamp to relative time
    t = result_df['timestamp'].values - result_df['timestamp'].values[0]
    
    colors = {'x': '#e74c3c', 'y': '#2ecc71', 'z': '#3498db'}
    
    fig, axes = plt.subplots(4, 2, figsize=(14, 16))
    fig.suptitle('Ferret Head Kinematics Analysis\nAngular velocity in world vs local (body) reference frames', 
                 fontsize=14, fontweight='bold')
    
    # World frame angular velocity
    ax = axes[0, 0]
    ax.plot(t, result_df['omega_world_x'], color=colors['x'], label='ωx', linewidth=0.8)
    ax.plot(t, result_df['omega_world_y'], color=colors['y'], label='ωy', linewidth=0.8)
    ax.plot(t, result_df['omega_world_z'], color=colors['z'], label='ωz', linewidth=0.8)
    ax.set_title('World Frame Angular Velocity (ω_world)')
    ax.set_ylabel('rad/s')
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    
    # Local frame angular velocity
    ax = axes[0, 1]
    ax.plot(t, result_df['omega_local_x'], color=colors['x'], linestyle='--', label='ωx', linewidth=0.8)
    ax.plot(t, result_df['omega_local_y'], color=colors['y'], linestyle='--', label='ωy', linewidth=0.8)
    ax.plot(t, result_df['omega_local_z'], color=colors['z'], linestyle='--', label='ωz', linewidth=0.8)
    ax.set_title('Local Frame Angular Velocity (ω_local)')
    ax.set_ylabel('rad/s')
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    
    # Euler angles (degrees)
    ax = axes[1, 0]
    ax.plot(t, result_df['roll_world_deg'], color=colors['x'], label='Roll', linewidth=0.8)
    ax.plot(t, result_df['pitch_world_deg'], color=colors['y'], label='Pitch', linewidth=0.8)
    ax.plot(t, result_df['yaw_world_deg'], color=colors['z'], label='Yaw', linewidth=0.8)
    ax.set_title('Euler Angles (World Frame)')
    ax.set_ylabel('degrees')
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    
    # Angular velocity magnitude comparison
    ax = axes[1, 1]
    ax.plot(t, result_df['omega_world_magnitude'], color='#9b59b6', label='|ω| world', linewidth=0.8)
    ax.plot(t, result_df['omega_local_magnitude'], color='#f39c12', linestyle='--', label='|ω| local', linewidth=0.8)
    ax.set_title('Angular Velocity Magnitude')
    ax.set_ylabel('rad/s')
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    
    # Local Euler rates
    ax = axes[2, 0]
    ax.plot(t, result_df['roll_rate_local'], color=colors['x'], label='Roll rate', linewidth=0.8)
    ax.plot(t, result_df['pitch_rate_local'], color=colors['y'], label='Pitch rate', linewidth=0.8)
    ax.plot(t, result_df['yaw_rate_local'], color=colors['z'], label='Yaw rate', linewidth=0.8)
    ax.set_title('Roll/Pitch/Yaw Rates (Local Frame)')
    ax.set_ylabel('rad/s')
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    
    # Head position XY
    ax = axes[2, 1]
    scatter = ax.scatter(result_df['translation_x'], result_df['translation_y'], 
                        c=t, cmap='viridis', s=1, alpha=0.7)
    ax.set_title('Head Position (XY plane)')
    ax.set_xlabel('X (mm)')
    ax.set_ylabel('Y (mm)')
    ax.set_aspect('equal', adjustable='box')
    plt.colorbar(scatter, ax=ax, label='Time (s)')
    ax.grid(True, alpha=0.3)
    
    # Position over time
    ax = axes[3, 0]
    ax.plot(t, result_df['translation_x'], color=colors['x'], label='X', linewidth=0.8)
    ax.plot(t, result_df['translation_y'], color=colors['y'], label='Y', linewidth=0.8)
    ax.plot(t, result_df['translation_z'], color=colors['z'], label='Z', linewidth=0.8)
    ax.set_title('Head Position vs Time')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('mm')
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    
    # Unwrapped yaw for tracking total rotation
    ax = axes[3, 1]
    yaw_unwrapped = np.unwrap(result_df['yaw_world_rad'].values)
    ax.plot(t, np.degrees(yaw_unwrapped), color='#8e44ad', linewidth=0.8)
    ax.set_title('Yaw (Unwrapped) - Total Head Rotation')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('degrees')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.show()
    plt.close()


# =============================================================================
# MAIN
# =============================================================================

def main(head_rotation_translation_csv_path:str) -> None:
    """Main entry point."""
    print("=" * 70)
    print("FERRET HEAD KINEMATICS ANALYSIS")
    print("=" * 70)
    
    # Input file
    input_path = Path(head_rotation_translation_csv_path)
    
    # Run analysis
    result_df = analyze_ferret_head_kinematics(input_path)
    
    # Save results
    output_file_name = "ferret_head_kinematics.csv"
    output_csv = input_path.parent / output_file_name
    
    result_df.to_csv(output_csv, index=False)
    print(f"\nSaved kinematic data to: {output_csv}")
    
    # Create visualization
    print("\nCreating visualization...")
    output_png = input_path.parent / "ferret_head_kinematics_visualization.png"
    create_visualization(result_df, output_png)
    print(f"Saved visualization to: {output_png}")
    
    # Print summary statistics
    print("\n" + "=" * 70)
    print("SUMMARY STATISTICS")
    print("=" * 70)
    
    print(f"\nTotal frames: {len(result_df)}")
    duration = result_df['timestamp'].iloc[-1] - result_df['timestamp'].iloc[0]
    print(f"Duration: {duration:.2f} seconds")
    print(f"Average frame rate: {len(result_df) / duration:.2f} Hz")
    
    print("\nAngular Velocity (World Frame):")
    for axis in ['x', 'y', 'z']:
        col = f'omega_world_{axis}'
        print(f"  ω{axis}: mean={result_df[col].mean():.3f}, "
              f"std={result_df[col].std():.3f}, "
              f"range=[{result_df[col].min():.3f}, {result_df[col].max():.3f}] rad/s")
    
    print("\nAngular Velocity (Local Frame):")
    for axis in ['x', 'y', 'z']:
        col = f'omega_local_{axis}'
        print(f"  ω{axis}: mean={result_df[col].mean():.3f}, "
              f"std={result_df[col].std():.3f}, "
              f"range=[{result_df[col].min():.3f}, {result_df[col].max():.3f}] rad/s")
    
    print("\nEuler Angles (World Frame, degrees):")
    for angle in ['roll', 'pitch', 'yaw']:
        col = f'{angle}_world_deg'
        print(f"  {angle.capitalize()}: mean={result_df[col].mean():.1f}°, "
              f"std={result_df[col].std():.1f}°, "
              f"range=[{result_df[col].min():.1f}°, {result_df[col].max():.1f}°]")
    
    print("\n" + "=" * 70)
    print("KEY INSIGHTS")
    print("=" * 70)
    print("""
    WORLD FRAME (omega_world, euler_world):
    - Fixed reference frame (e.g., lab coordinates)
    - Rotation described relative to stationary axes
    - Useful for tracking absolute head orientation
    
    LOCAL FRAME (omega_local):
    - Body-fixed reference frame (moves with the head)
    - What an IMU/gyroscope attached to the skull would measure
    - Components represent rotation about the head's own axes:
      * ωx_local: rotation about head's forward axis (roll)
      * ωy_local: rotation about head's lateral axis (pitch/nod)
      * ωz_local: rotation about head's vertical axis (yaw/shake)
    
    Note: |ω_world| = |ω_local| (magnitudes are equal, just different bases)
    """)


if __name__ == "__main__":
    head_rotation_translation_csv_path = r"D:\bs\ferret_recordings\clips\0m_37s-1m_37s\mocap_data\output_data\solver_output\rotation_translation_data.csv"
    main(head_rotation_translation_csv_path)