#!/usr/bin/env python3

"""This might be the only thing I find a how-to on
And I don't actually think it's a how to."""


def sarsa_lambtha(
    env,
    G,
    lambtha,
    epissodes=5000,
    max_steps=100,
    alpha=0.1,
    gamma=0.99,
    epsilon=1,
    min_epsilon=0.1,
):
    """env - the environment
    Q - numpy aray of shape (s,a) containing the Q table
    This is the first time we get a Q table in this assignment
    lambtha - eligibility trace factor
    episodes - total epochs/episodes/iterations/whatever
    max_steps - steps before we mercy kill boiyo
    alpha - learning rate
    gamma - discount rate
    epsilon - initial threshold for epsilon greedy
    min_epsilon - value of garunteed random
    epsilon decay - how fast we'll let epsilon decay
    returns an updated q table."""
    return
