"""Experiment 02 — IQL equilibrium selection in one-step Stag Hunt.

Read HYPOTHESIS.md before implementing this runner. Keep the IQL algorithm and
preregistered configuration fixed; this file should contain only the Stag Hunt
environment, multi-seed orchestration, and result classification.
"""

import argparse
import random
from collections import Counter
from enum import IntEnum

import numpy as np
from tabular_iql import IQL, MatrixGame

DEFAULT_SEEDS = tuple(range(20))
TOTAL_EPISODES = 20_000
GAMMA = 0.99
LEARNING_RATE = 0.05


class Action(IntEnum):
    """Stag Hunt actions with readable output and integer compatibility."""

    STAG = 0
    HARE = 1

    def __str__(self) -> str:
        return self.name.lower()

    def __repr__(self) -> str:
        return str(self)


def classify(joint_action: tuple[Action, ...]) -> str:
    """Classify a final greedy joint action by equilibrium outcome."""
    if joint_action == (Action.STAG, Action.STAG):
        return "stag/stag"
    if joint_action == (Action.HARE, Action.HARE):
        return "hare/hare"
    return "mismatched"


def format_q_values(q_tables) -> str:
    """Format both agents' final action values without defaultdict internals."""
    formatted_agents = []
    for agent, q_table in enumerate(q_tables):
        stag = float(q_table[str((0, int(Action.STAG)))])
        hare = float(q_table[str((0, int(Action.HARE)))])
        formatted_agents.append(f"agent{agent}=[stag={stag:.6f}, hare={hare:.6f}]")
    return " ".join(formatted_agents)


def set_seed(seed: int) -> None:
    """Seed every random-number source used by the tabular experiment."""
    random.seed(seed)
    np.random.seed(seed)


def main() -> None:
    """Run all preregistered seeds and report final greedy joint actions."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", type=int, nargs="+", default=DEFAULT_SEEDS)
    args = parser.parse_args()

    staghunt_payoff_matrix = np.array([[[4, 4], [0, 3]], [[3, 0], [2, 2]]])

    counts: Counter[str] = Counter()

    for seed in args.seeds:
        set_seed(seed)

        env = MatrixGame(staghunt_payoff_matrix, ep_length=1)

        agents = IQL(
            num_agents=env.n_agents,
            action_spaces=env.action_space,
            gamma=GAMMA,
            learning_rate=LEARNING_RATE,
        )

        for episode in range(TOTAL_EPISODES):
            obss, _ = env.reset()

            agents.schedule_hyperparameters(
                timestep=episode,
                max_timestep=TOTAL_EPISODES,
            )

            actions = agents.act(obss)
            next_obss, rewards, terminated, truncated, _ = env.step(actions)

            agents.learn(
                obss,
                actions,
                rewards,
                next_obss,
                terminated or truncated,
            )

        # Evaluate the learned policy without exploration.
        agents.epsilon = 0.0
        obss, _ = env.reset()
        greedy_joint_action = tuple(Action(action) for action in agents.act(obss))
        outcome = classify(greedy_joint_action)
        counts[outcome] += 1

        print(
            f"seed={seed:02d} action={greedy_joint_action} outcome={outcome} "
            f"{format_q_values(agents.q_tables)}"
        )

    print("\nAggregate:")
    for outcome in ("stag/stag", "hare/hare", "mismatched"):
        print(f"  {outcome}: {counts[outcome]}")


if __name__ == "__main__":
    main()
