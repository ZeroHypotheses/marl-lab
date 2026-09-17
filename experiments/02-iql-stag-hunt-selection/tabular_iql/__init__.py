"""Frozen tabular-IQL baseline used by Experiment 02.

Copied from ``experiments/01-tabular-iql`` at commit
``d379f3b0d296830d29db5fc00d0388cfa7a34126``.
"""

from .iql import IQL
from .matrix_game import MatrixGame

__all__ = ["IQL", "MatrixGame"]
