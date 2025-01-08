#!/usr/bin/env python3

import numpy as np

"""We're initializing the environment
I'm really not sure how this differs other than
calling the function we just made,
which only calls a different function"""

def q_init(env):
    """env is the FrozenLakeEnv instance"""

    return_array = np.zeros((env.observation_space.n, env.action_space.n))

    return return_array