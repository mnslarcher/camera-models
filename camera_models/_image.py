from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from ._utils import get_plane_from_three_points


class Image:
    def __init__(self, heigth: int, width: int) -> None:
        self.heigth = heigth
        self.width = width

    def draw(self, color: str = "tab:gray", ax: Optional[plt.Axes] = None) -> plt.Axes:
        if ax is None:
            ax = plt.gca()

        ax.set_xticks(np.arange(0, self.width + 1))
        ax.set_yticks(np.arange(0, self.heigth + 1))
        ax.grid(color=color)
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.heigth)
        ax.set_aspect("equal")
        return ax


class ImagePlane:
    def __init__(
        self,
        origin: np.ndarray,
        dx: np.ndarray,
        dy: np.ndarray,
        heigth: int,
        width: int,
        mx: float = 1.0,
        my: float = 1.0,
    ) -> None:
        self.origin = origin
        self.dx = dx
        self.dy = dy
        self.heigth = heigth
        self.width = width
        self.mx = mx
        self.my = my
        self.pi = get_plane_from_three_points(origin, origin + dx, origin + dy)

    def draw3d(
        self, color: str = "tab:gray", alpha: float = 0.5, ax: Optional[Axes3D] = None
    ) -> Axes3D:
        if ax is None:
            ax = plt.gca(projection="3d")

        xticks = np.arange(self.width + 1).reshape(-1, 1) * self.dx / self.mx
        yticks = np.arange(self.heigth + 1).reshape(-1, 1) * self.dy / self.my
        pts = (self.origin + xticks).reshape(-1, 1, 3) + yticks
        pts = pts.reshape(-1, 3)
        shape = len(xticks), len(yticks)
        X = pts[:, 0].reshape(shape)
        Y = pts[:, 1].reshape(shape)
        Z = pts[:, 2].reshape(shape)
        frame = np.c_[
            self.origin,
            self.origin + self.dx * self.width / self.mx,
            self.origin
            + self.dx * self.width / self.mx
            + self.dy * self.heigth / self.my,
            self.origin + self.dy * self.heigth / self.my,
            self.origin,
        ]
        ax.plot(*frame, color="black")
        ax.plot_wireframe(X, Y, Z, color=color, alpha=alpha)
        return ax
