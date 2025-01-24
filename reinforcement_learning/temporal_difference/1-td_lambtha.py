#!/usr/bin/env python3

import numpy as np

"""I'm honestly still not sure what we're doing here
I'm frustrated I waited so long
And I'm frustrated office hours aren't available this week
And I'm frustrated that there's not further info about which
method to use for monte carlo
Which is theorhetically (sp?) what we're going to have to use
in the next project."""


def td_lambtha(
    env, V, policy, lambtha, episodes=5000,
    max_steps=100, alpha=0.1, gamma=0.99
):
    """Here's some variables I guess.
    env - the environment
    V - shape (s, ) containing value estimates
    policy - function that takes in a state and returns the next action
    lambtha - eligibility trace factor.
    What does that mean? Don't ask me, I don't know.
    episodes - like epochs
    max_steps - the amount of steps Boiyo is allowed to take
    alpha - learning rate
    gamma - discount rate
    returns an updated value estimate."""
    return
