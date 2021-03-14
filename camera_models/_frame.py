from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from ._utils import draw3d_arrow


class ReferenceFrame:
    def __init__(
        self,
        origin: np.ndarray,
        dx: np.ndarray,
        dy: np.ndarray,
        dz: np.ndarray,
        name: str,
    ) -> None:
        self.origin = origin
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.name = name

    def draw3d(
        self,
        head_length: float = 0.3,
        color: str = "tab:blue",
        ax: Optional[Axes3D] = None,
    ) -> Axes3D:
        if ax is None:
            ax = plt.gca(projection="3d")

        ax.text(*self.origin + 0.5, f"({self.name})")
        ax = draw3d_arrow(
            ax=ax,
            arrow_location=self.origin,
            arrow_vector=self.dx,
            head_length=head_length,
            color=color,
            name="x",
        )
        ax = draw3d_arrow(
            ax=ax,
            arrow_location=self.origin,
            arrow_vector=self.dy,
            head_length=head_length,
            color=color,
            name="y",
        )
        ax = draw3d_arrow(
            ax=ax,
            arrow_location=self.origin,
            arrow_vector=self.dz,
            head_length=head_length,
            color=color,
            name="z",
        )
        return ax
