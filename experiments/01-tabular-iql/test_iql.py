"""Behavioral tests for the tabular independent Q-learning exercise.

The tests exercise the public ``IQL.act`` and ``IQL.learn`` methods. They use
small, deliberately chosen Q-values and rewards so that each expected result
can be calculated by hand; they do not simulate a complete matrix game.
"""

import numpy as np
from gymnasium.spaces import Discrete
from iql import IQL


def test_act_selects_each_agents_highest_valued_action_without_exploration():
    """Each agent greedily selects its own highest-valued action at epsilon zero.

    The Q-tables prefer action 1 for agent 0 and action 0 for agent 1. This also
    checks that independent learners do not accidentally share their values or
    select a joint action from one combined table.
    """
    agents = IQL(
        num_agents=2,
        action_spaces=[Discrete(2), Discrete(2)],
        gamma=0.99,
        epsilon=0.0,
    )
    agents.q_tables[0][str((0, 0))] = 1.0
    agents.q_tables[0][str((0, 1))] = 5.0
    agents.q_tables[1][str((0, 0))] = 4.0
    agents.q_tables[1][str((0, 1))] = 2.0

    assert agents.act([0, 0]) == [1, 0]


def test_act_explores_each_agents_entire_action_space():
    """Pure exploration samples every valid action in each agent's own space.

    The agents intentionally have different action-space sizes. This catches an
    implementation that hard-codes the two actions used by Prisoner's Dilemma.
    The fixed NumPy seed makes the finite sampling check reproducible.
    """
    np.random.seed(0)
    agents = IQL(
        num_agents=2,
        action_spaces=[Discrete(2), Discrete(3)],
        gamma=0.99,
        epsilon=1.0,
    )

    sampled_actions = [agents.act([0, 0]) for _ in range(200)]

    assert {actions[0] for actions in sampled_actions} == {0, 1}
    assert {actions[1] for actions in sampled_actions} == {0, 1, 2}


def test_learn_moves_selected_q_values_toward_terminal_rewards():
    """A terminal update moves each selected Q-value toward its immediate reward.

    The rewards are synthetic and are not entries from the Prisoner's Dilemma
    payoff matrix; this test isolates the Q-learning arithmetic. Since ``done``
    is true, there is no bootstrap term. With learning rate 0.5, the expected
    updates are ``2 + 0.5 * (6 - 2) = 4`` and
    ``4 + 0.5 * (2 - 4) = 3``.
    """
    agents = IQL(
        num_agents=2,
        action_spaces=[Discrete(2), Discrete(2)],
        gamma=0.99,
        learning_rate=0.5,
    )
    agents.q_tables[0][str((0, 1))] = 2.0
    agents.q_tables[1][str((0, 0))] = 4.0

    agents.learn(
        obss=[0, 0],
        actions=[1, 0],
        rewards=[6.0, 2.0],
        n_obss=[0, 0],
        done=True,
    )

    assert agents.q_tables[0][str((0, 1))] == 4.0
    assert agents.q_tables[1][str((0, 0))] == 3.0
