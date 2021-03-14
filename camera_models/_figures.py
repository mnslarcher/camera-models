from typing import Optional, Sequence

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from ._homogeneus import to_homogeneus, to_inhomogeneus
from ._matrices import get_plucker_matrix, get_projection_matrix


class GenericPoint:
    def __init__(self, X: np.ndarray, name: Optional[str] = None) -> None:
        self.values = X
        self.name = name

    def draw(
        self,
        f: float,
        px: float = 0.0,
        py: float = 0.0,
        C: Sequence[float] = (0.0, 0.0, 0.0),
        theta_x: float = 0.0,
        theta_y: float = 0.0,
        theta_z: float = 0.0,
        mx: float = 1.0,
        my: float = 1.0,
        s: float = 20.0,
        color: str = "tab:green",
        closed: bool = True,
        ax: Optional[plt.Axes] = None,
    ) -> plt.Axes:
        if ax is None:
            ax = plt.gca()

        P = get_projection_matrix(
            f,
            px=px,
            py=py,
            mx=mx,
            my=my,
            theta_x=theta_x,
            theta_y=theta_y,
            theta_z=theta_z,
            C=C,
        )

        x = to_inhomogeneus(P @ to_homogeneus(self.values))
        ax.scatter(*x, s=s, color=color)
        if self.name is not None:
            ax.text(*x, self.name)

        return ax

    def draw3d(
        self,
        pi: np.ndarray,
        C: Sequence[float] = (0.0, 0.0, 0.0),
        s: float = 20.0,
        color: str = "tab:green",
        closed=True,
        ax: Optional[Axes3D] = None,
    ) -> Axes3D:
        if ax is None:
            ax = plt.gca(projection="3d")

        L = get_plucker_matrix(np.asarray(C), self.values)
        x = to_inhomogeneus(L @ pi)
        ax.scatter3D(*self.values, s=s, color=color)
        ax.scatter3D(*x, s=s, color=color)
        ax.plot(*np.c_[C, self.values], color="tab:gray", alpha=0.5, ls="--")
        if self.name is not None:
            ax.text(*self.values, self.name)
            ax.text(*x, self.name.lower())

        return ax


class Polygon:
    def __init__(self, xyz: np.ndarray) -> None:
        self.values = xyz

    def draw(
        self,
        f: float,
        px: float = 0.0,
        py: float = 0.0,
        C: Sequence[float] = (0.0, 0.0, 0.0),
        theta_x: float = 0.0,
        theta_y: float = 0.0,
        theta_z: float = 0.0,
        mx: float = 1.0,
        my: float = 1.0,
        s: float = 20.0,
        color: str = "tab:green",
        closed: bool = True,
        ax: Optional[plt.Axes] = None,
    ) -> plt.Axes:
        if ax is None:
            ax = plt.gca()

        P = get_projection_matrix(
            f,
            px=px,
            py=py,
            mx=mx,
            my=my,
            theta_x=theta_x,
            theta_y=theta_y,
            theta_z=theta_z,
            C=C,
        )
        x_list = []
        for i, X in enumerate(self.values, 1):
            x = to_inhomogeneus(P @ to_homogeneus(X))
            ax.scatter(*x, s=s, color=color)
            ax.text(*x, f"x{i}")
            x_list.append(x)

        if closed:
            x_list.append(x_list[0])

        ax.plot(*np.vstack(x_list).T, color=color)
        return ax

    def draw3d(
        self,
        pi: np.ndarray,
        C: Sequence[float] = (0.0, 0.0, 0.0),
        s: float = 20.0,
        color: str = "tab:green",
        closed=True,
        ax: Optional[Axes3D] = None,
    ) -> Axes3D:
        if ax is None:
            ax = plt.gca(projection="3d")

        xyz = self.values.copy()
        x_list = []
        for i, X in enumerate(xyz, 1):
            L = get_plucker_matrix(np.asarray(C), X)
            x = to_inhomogeneus(L @ pi)
            ax.scatter3D(*X, s=s, color=color)
            ax.scatter3D(*x, s=s, color=color)
            ax.plot(*np.c_[C, X], color="tab:gray", alpha=0.5, ls="--")
            ax.text(*X, f"X{i}")
            ax.text(*x, f"x{i}")
            x_list.append(x)

        if closed:
            xyz = np.vstack([xyz, xyz[0, :]])
            x_list.append(x_list[0])

        ax.plot(*xyz.T, color=color)
        ax.plot(*np.vstack(x_list).T, color=color)
        return ax
