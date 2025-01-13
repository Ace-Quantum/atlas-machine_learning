#!/usr/bin/env python3

import gymnasium as gym
import numpy as np

def run():
    env = gym.make('FrozenLake-v1', map_name='8x8', is_slippery=True, render_mode='human')

    q = np.zeros((env.observation_space.n, env.action_space.n))

    learning_rate_a = 0.9
    discount_factor_g = 0.9

    state = env.reset()[0]
    terminated = False
    truncated = False

    while(not terminated and not truncated):
        action = env.action_space.sample()

        new_state, reward, terminated, truncated, _ = env.step(action)

        q[state, action] = q[state, action]

        state = new_state

        # print(f"Action: ", action)
        # print(f"State: ", state)



    env.close

if __name__ == '__main__':
    run()