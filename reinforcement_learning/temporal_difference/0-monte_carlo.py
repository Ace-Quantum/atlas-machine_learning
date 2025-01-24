#!/usr/bin/env python3

"""Tbh I'm not entirely sure what we're doing here
I understand that Monte Carlo is used for Reinforcement Learning
And from what I can tell it does the same thing as Q Learning
But in a different way and a different result.
Monte Carlo First Visit - David
Here's a resource I stole from Jabulani:
https://www.geeksforgeeks.org/monte-carlo-policy-evaluation/"""

import numpy as np


def monte_carlo(env, V, policy, episodes=5000, max_steps=100,
                alpha=0.1, gamma=0.99):
    """
    env - the environment given. 
    In this case it's the 8x8 frozen lake from Gymnasium.
    V - numpy array of shape (s,) containing the value estimate
    (wtf is a value estimate???)
    policy - a function which takes in a state and returns the next action.
    That seems like a fun thing to try and impliment.
    episodes - like epochs or iterations
    max_steps - max number of steps before Boiyo is kicked off the ice
    alpha - learning rate
    gamma - discount rate
    (There's a discount rate now? How does that work?)
    Returns: V, the updated value estimate. Updated from what I'm not sure.
    (From the previously given V, Ace. Don't be dumb.)
    (Ok fair, but I still don't know exactly what a value estimate is)"""

    # The tutorial I'm following calls for a num_state
    # But Idk if we have a num_state
    # So this is what I'm doing instead.
    # V = np.zeros(episodes)
    returns = {state: [] for state in range(episodes)}

    for i in range(episodes):
        state = env.reset()[0]
        episode = []
        terminated = False
        truncated = False
        step_counter = 0

        while not terminated and not truncated:

            action = policy(state)

            new_state, reward, terminated, truncated, _ = env.step(action)

            episode.append((state, reward))
            if terminated:
                break
            state = new_state

        G = 0
        for state, reward in reversed(episode):
            G = gamma * G + reward
            returns[state].append(G)
            V[state] = np.mean(returns[state])

    return V
