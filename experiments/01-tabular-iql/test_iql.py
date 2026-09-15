import numpy as np
from gymnasium.spaces import Discrete

from iql import IQL


def test_act_selects_each_agents_highest_valued_action_without_exploration():
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
