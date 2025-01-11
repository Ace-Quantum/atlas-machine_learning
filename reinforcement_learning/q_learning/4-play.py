#/usr/bin/env python3

"""This function plays trained an agent """

def play(env, Q, max_steps=100):
    """Plays out the trained agent
    env - the environment in which we play
    Q - the already trained Q-table
    max_steps - Boiyo is not allowed any more steps than this
    
    returns 
    rewards - the toal rewards for the episode
    board_states - list of rendered outputs of the board state"""

    
