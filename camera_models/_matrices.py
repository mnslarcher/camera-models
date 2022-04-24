from typing import Sequence

import numpy as np

from ._homogeneus import to_homogeneus


def get_plucker_matrix(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    A = to_homogeneus(A)
    B = to_homogeneus(B)
    L = A.reshape(-1, 1) * B.reshape(1, -1) - B.reshape(-1, 1) * A.reshape(1, -1)
    return L


def _get_roll_matrix(theta_x: float = 0.0) -> np.ndarray:
    Rx = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, np.cos(theta_x), -np.sin(theta_x)],
            [0.0, np.sin(theta_x), np.cos(theta_x)],
        ]
    )
    return Rx


def _get_pitch_matrix(theta_y: float = 0.0) -> np.ndarray:
    Ry = np.array(
        [
            [np.cos(theta_y), 0.0, np.sin(theta_y)],
            [0.0, 1.0, 0.0],
            [-np.sin(theta_y), 0.0, np.cos(theta_y)],
        ]
    )
    return Ry


def _get_yaw_matrix(theta_z: float = 0.0) -> np.ndarray:
    Rz = np.array(
        [
            [np.cos(theta_z), -np.sin(theta_z), 0.0],
            [np.sin(theta_z), np.cos(theta_z), 0.0],
            [0.0, 0.0, 1.0],
        ]
    )
    return Rz


def get_rotation_matrix(
    theta_x: float = 0.0, theta_y: float = 0.0, theta_z: float = 0.0
) -> np.ndarray:
    # Roll
    Rx = _get_roll_matrix(theta_x)
    # Pitch
    Ry = _get_pitch_matrix(theta_y)
    # Yaw
    Rz = _get_yaw_matrix(theta_z)
    return Rz @ Ry @ Rx


def get_calibration_matrix(
    f: float,
    px: float = 0.0,
    py: float = 0.0,
    mx: float = 1.0,
    my: float = 1.0,
) -> np.ndarray:
    K = np.diag([mx, my, 1]) @ np.array([[f, 0.0, px], [0.0, f, py], [0.0, 0.0, 1.0]])
    return K


def get_projection_matrix(
    f: float,
    px: float = 0.0,
    py: float = 0.0,
    C: Sequence[float] = (0.0, 0.0, 0.0),
    theta_x: float = 0.0,
    theta_y: float = 0.0,
    theta_z: float = 0.0,
    mx: float = 1.0,
    my: float = 1.0,
) -> np.ndarray:
    K = get_calibration_matrix(f=f, px=px, py=py, mx=mx, my=my)
    R = get_rotation_matrix(theta_x=theta_x, theta_y=theta_y, theta_z=theta_z).T
    P = K @ R @ np.c_[np.eye(3), -np.asarray(C)]
    return P
