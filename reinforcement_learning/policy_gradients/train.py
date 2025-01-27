#!/usr/bin/env python3

"""This is where we're going to train table
so that it becomes less stupid in a more optimal set up."""

import numpy as np

policy_gradient = __import__("policy_gradient").policy_gradient


def train(env, nb_episodes, alpha=0.000045, gamma=0.98):
    """I'm *pretty* sure that we're not training a full model here
    Just filling out the Q table
    Unless it's not the Q table anymore?
    env - initial environment
    nb_episodes - the number of episodes
    alpha - learning rate
    gamma - discount factor"""

    return
