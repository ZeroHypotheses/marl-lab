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
    a0, a1 = joint_action
    selected_returns = payoff_matrix[a0, a1]
    returns = (float(selected_returns[0]), float(selected_returns[1]))

    deviation_gains = (
        float(np.max(payoff_matrix[:, a1, 0]) - returns[0]),
        float(np.max(payoff_matrix[a0, :, 1]) - returns[1]),
    )

    candidate_returns = payoff_matrix.reshape(-1, 2)
    weakly_better = np.all(candidate_returns >= selected_returns, axis=1)
    strictly_better = np.any(candidate_returns > selected_returns, axis=1)
    is_pareto_dominated = bool(np.any(weakly_better & strictly_better))

    return Evaluation(
        returns=returns,
        welfare=sum(returns),
        fairness=returns[0] * returns[1],
        deviation_gains=deviation_gains,
        is_nash=all(gain == 0 for gain in deviation_gains),
        is_pareto_optimal=not is_pareto_dominated,
    )
