"""Acceptance checks for Experiment 03; run this file explicitly with pytest."""

import numpy as np
import pytest
from evaluator import Evaluation, evaluate_joint_action

STAG_HUNT = np.array([[[4, 4], [0, 3]], [[3, 0], [2, 2]]])
PRISONERS_DILEMMA = np.array([[[3, 3], [0, 5]], [[5, 0], [1, 1]]])


@pytest.mark.parametrize(
    ("joint_action", "expected"),
    [
        ((0, 0), Evaluation((4, 4), (0, 0), True, True, 8, 16)),
        ((0, 1), Evaluation((0, 3), (2, 1), False, False, 3, 0)),
        ((1, 0), Evaluation((3, 0), (1, 2), False, False, 3, 0)),
        ((1, 1), Evaluation((2, 2), (0, 0), True, False, 4, 4)),
    ],
)
def test_evaluates_every_stag_hunt_outcome(joint_action, expected):
    assert evaluate_joint_action(STAG_HUNT, joint_action) == expected


def test_generalises_beyond_stag_hunt():
    assert evaluate_joint_action(PRISONERS_DILEMMA, (1, 1)) == Evaluation(
        returns=(1, 1),
        deviation_gains=(0, 0),
        is_nash=True,
        is_pareto_optimal=False,
        welfare=2,
        fairness=1,
    )
