"""Experiment NN — <slug>.

Read HYPOTHESIS.md before editing this file. The hypothesis comes first.

The book's reference implementations are importable as `marlbase`
(`uv sync --extra book`). Never edit upstream/ in place — see AGENTS.md P5.
"""

import argparse
import random

import numpy as np
import torch


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    # Report over several seeds — single-seed MARL results are noise.
    parser.add_argument("--seeds", type=int, nargs="+", default=[0, 1, 2, 3, 4])
    args = parser.parse_args()

    for seed in args.seeds:
        set_seed(seed)
        raise NotImplementedError("Write the smallest thing that answers the question.")


if __name__ == "__main__":
    main()
