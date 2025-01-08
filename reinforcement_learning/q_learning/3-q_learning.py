#!/usr/bin/env python3

"""This script holds a function that performs Q learning"""

import numpy as np
import gymnasium as gym
epsilon_greedy = __import__('2-epsilon_greedy').epsilon_greedy

def train(env, Q, episodes=5000, max_steps=100,
          alpha=0.1, gamma=0.99, epsilon=1, min_epsilon=0.1,
          epsilon_decay=0.05):
    """It all comes down to this
    Only it actually doesn't because there's another task after this one
    Anyway here's the variables
    env - frozen lake environment
    q - the q table
    episodes - basically epochs
    max_steps - the truncation cutoff. 
    ---Boiyo isn't allowed any more steps than this to reach the end
    alpha - learning rate
    gamma - discount rate
    epsilon - init. threshold for epsilon greedy
    min_epsilon - the minimum value that epsilon should decay to.
    epsilon_decay - decay rate of epsilon
    
    falling through hole updates the q-table to -1
    import the epsilon greedy function we made
    ---mine is currently not passing all the checks---
    returns: Q, total rewards
    Q - updated Q Table
    total_rewards - list of rewards per episode"""

    rewards_per_episode = np.zeros(episodes)
    step_counter = 0

    for i in range(episodes):
        # print(f"for loop iteration: ", i)
        state = env.reset()[0]
        terminated = False
        truncated = False

        # debug_counter = 0
        while(not terminated and not truncated):
            # print(f"while iterator: ", debug_counter)
            action = epsilon_greedy(Q, state, epsilon)

            new_state, reward, terminated, truncated, _ = env.step(action)

            Q[state, action] = Q[state, action] + alpha * (
                reward + gamma * np.max(Q[new_state,:]) - Q[state, action]
            )

            step_counter += 1
            state = new_state
    
        epsilon = max(epsilon - epsilon_decay, 0)

        if(epsilon==0):
            alpha = 0.0001

        if reward == 1:
            rewards_per_episode[i] = 1

        # print(f"steps taken: ", step_counter)
        if step_counter >= max_steps:
            break

        # print(f"epsilon: ", epsilon)
        if epsilon <= min_epsilon:
            break

    return Q, rewards_per_episode