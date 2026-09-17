"""Post-hoc solution-concept evaluation for two-agent matrix games."""

from dataclasses import dataclass

import numpy as np

JointAction = tuple[int, int]


@dataclass(frozen=True)
class Evaluation:
    """Evaluation of one deterministic joint action."""

    returns: tuple[float, float]
    deviation_gains: tuple[float, float]
    is_nash: bool
    is_pareto_optimal: bool
    welfare: float
    fairness: float


def evaluate_joint_action(
    payoff_matrix: np.ndarray,
    joint_action: JointAction,
) -> Evaluation:
    """Evaluate one joint action under several Chapter 4 criteria.

    The payoff matrix has shape ``(actions_agent_0, actions_agent_1, 2)``.
    Compare Pareto optimality only against deterministic joint actions in that
    matrix.
    """
    raise NotImplementedError("Implement the solution-concept evaluator")
