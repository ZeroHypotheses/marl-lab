"""Independent Q-learning baseline copied unchanged from Experiment 01.

Source: ``experiments/01-tabular-iql/iql.py`` at commit
``d379f3b0d296830d29db5fc00d0388cfa7a34126``.
"""

from collections import defaultdict
import random
from typing import List, DefaultDict

import numpy as np
from gymnasium.spaces import Space
from gymnasium.spaces.utils import flatdim


class IQL:
    """Agent using the Independent Q-Learning algorithm"""

    def __init__(
        self,
        num_agents: int,
        action_spaces: List[Space],
        gamma: float,
        learning_rate: float = 0.5,
        epsilon: float = 1.0,
        **kwargs,
    ):
        """Constructor of IQL

        Initializes variables for independent Q-learning agents

        :param num_agents (int): number of agents
        :param action_spaces (List[Space]): action spaces of the environment for each agent
        :param gamma (float): discount factor (gamma)
        :param learning_rate (float): learning rate for Q-learning updates
        :param epsilon (float): epsilon value for all agents

        :attr n_acts (List[int]): number of actions for each agent
        :attr q_tables (List[DefaultDict]): tables for Q-values mapping actions ACTs
            to respective Q-values for all agents
        """
        self.num_agents = num_agents
        self.action_spaces = action_spaces
        self.n_acts = [flatdim(action_space) for action_space in action_spaces]

        self.gamma: float = gamma
        self.learning_rate = learning_rate
        self.epsilon = epsilon

        # initialise Q-tables for all agents
        # access value of Q_i(o, a) with self.q_tables[i][str((o, a))] (str conversion for hashable obs)
        self.q_tables: List[DefaultDict] = [
            defaultdict(lambda: 0) for _ in range(self.num_agents)
        ]

    def act(self, obss) -> List[int]:
        """Implement the epsilon-greedy action selection here for stateless task

        **IMPLEMENT THIS FUNCTION**

        :param obss (List): list of observations for each agent
        :return (List[int]): index of selected action for each agent
        """
        actions = []
        ### PUT YOUR CODE HERE ###
        for i, obs in enumerate(obss):
            n_acts_i = range(self.n_acts[i])
            if np.random.uniform() < self.epsilon:
                a = np.random.choice(len(n_acts_i))
            else:
                q_values = [self.q_tables[i][str((obs, a))] for a in n_acts_i]
                a = int(np.argmax(q_values))
            actions.append(a)
        return actions

    def learn(
        self,
        obss: List[np.ndarray],
        actions: List[int],
        rewards: List[float],
        n_obss: List[np.ndarray],
        done: bool,
    ):
        """Updates the Q-tables based on agents' experience

        **IMPLEMENT THIS FUNCTION**

        :param obss (List[np.ndarray]): list of observations for each agent
        :param action (List[int]): index of applied action of each agent
        :param rewards (List[float]): received reward for each agent
        :param n_obss (List[np.ndarray]): list of observations after taking the action for each agent
        :param done (bool): flag indicating whether a terminal state has been reached
        :return (List[float]): updated Q-values for current actions of each agent
        """
        ### PUT YOUR CODE HERE ###
        for i, (obs, action, reward, new_obs) in enumerate(
            zip(obss, actions, rewards, n_obss)
        ):
            if not done:
                target_q_values = [
                    self.q_tables[i][str((new_obs, action_candidate))]
                    for action_candidate in range(self.n_acts[i])
                ]
                target = reward + self.gamma * np.max(target_q_values)
            else:
                target = reward

            self.q_tables[i][str((obs, action))] += self.learning_rate * (
                target - self.q_tables[i][str((obs, action))]
            )
        return [q[str((o, a))] for q, o, a in zip(self.q_tables, obss, actions)]

    def schedule_hyperparameters(self, timestep: int, max_timestep: int):
        """Updates the hyperparameters

        This function is called before every episode and allows you to schedule your
        hyperparameters.

        :param timestep (int): current timestep at the beginning of the episode
        :param max_timestep (int): maximum timesteps that the training loop will run for
        """
        self.epsilon = 1.0 - (min(1.0, timestep / (0.8 * max_timestep))) * 0.99
