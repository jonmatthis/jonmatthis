# =============================================================================
# ANGULAR VELOCITY COMPUTATION
# =============================================================================
import numpy as np
from numpy.typing import NDArray

from .quaternion_helper import Quaternion


def compute_omega_world(q1: Quaternion, q2: Quaternion, dt: float) -> NDArray[np.float64]:
    """Compute angular velocity in world frame from two quaternions."""
    if dt <= 0:
        raise ValueError(f"dt must be positive, got {dt}")

    delta_q = q2 * q1.inverse()
    if delta_q.w < 0:
        delta_q = Quaternion(w=-delta_q.w, x=-delta_q.x, y=-delta_q.y, z=-delta_q.z)

    axis, angle = delta_q.to_axis_angle()
    return (angle / dt) * axis


def omega_world_to_local(
    omega_world: NDArray[np.float64],
    q: Quaternion,
) -> NDArray[np.float64]:
    """Transform angular velocity from world frame to local (body-attached) frame."""
    return q.inverse().rotate_vector(omega_world)