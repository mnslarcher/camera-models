from typing import List, Optional

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def draw3d_arrow(
    arrow_location: np.ndarray,
    arrow_vector: np.ndarray,
    head_length: float = 0.3,
    color: Optional[str] = None,
    name: Optional[str] = None,
    ax: Optional[Axes3D] = None,
) -> Axes3D:
    if ax is None:
        ax = plt.gca(projection="3d")

    ax.quiver(
        *arrow_location,
        *arrow_vector,
        arrow_length_ratio=head_length / np.linalg.norm(arrow_vector),
        color=color,
    )
    if name is not None:
        ax.text(*(arrow_location + arrow_vector), name)

    return ax


def get_plane_from_three_points(
    X1: np.ndarray, X2: np.ndarray, X3: np.ndarray
) -> np.ndarray:
    pi = np.hstack([np.cross(X1 - X3, X2 - X3), -X3 @ np.cross(X1, X2)])
    return pi


def set_xyzlim3d(
    left: Optional[float] = None,
    right: Optional[float] = None,
    ax: Optional[Axes3D] = None,
) -> Axes3D:
    if ax is None:
        ax = plt.gca(projection="3d")

    ax.set_xlim3d(left, right)
    ax.set_ylim3d(left, right)
    ax.set_zlim3d(left, right)
    return ax


def set_xyzticks(ticks: List[float], ax: Optional[Axes3D] = None) -> Axes3D:
    if ax is None:
        ax = plt.gca(projection="3d")

    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_zticks(ticks)
    return ax
