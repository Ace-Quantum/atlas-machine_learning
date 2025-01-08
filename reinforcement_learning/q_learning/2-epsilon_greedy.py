#!/usr/bin/env python3

"""This function will determine the next action"""

import numpy as np
import gymnasium as gym

def epsilon_greedy(Q, state, epsilon):
    """chosing where the state goes from here
    Q contains the q-table
    state is where the boiyo is
    epsilon is the epsilon to use for calculations
    
    It says we need to sample p to determine if we explore or exploit
    It does not give us a p to sample
    Regardless we are to use numpy.random.uniform

    exploring should be done with numpy.random.randint
    
    returns the next action index 
    (I assume that's the index of the new state but I could be wrong.)
        I was wrong, this is just determining explore or exploit
            Nope!!!! This is the direction our boiyo is going.
            I think."""

    """HOW DO I GET THE ACTION WITHOUT THE ENVIRONMENT"""

    if np.random.random() < epsilon:
        action = np.random.randint(0, 3)
    else:
        action = np.argmax(Q[state, :])

    return action
