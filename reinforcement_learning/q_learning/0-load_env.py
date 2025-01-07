#!/usr/bin/env python3

"""We're loading a frozen lake
What does that mean?
No idea."""

import gymnasium as gym


def load_frozen_lake(desc=None, map_name=None, is_slippery=False):
    """Loading a frozen lake
    desc - a list containing the
    description of the map for the environment
    map_name - string that is the map
    ---(????????? The assignemnt determines it to contain the map?
    ---"map_name is either None
    ------or a string containing the pre-made map to load"
    ---That's literally what it says.
    ---I'm assuming the string itself doesn't contain the map.)
    You can ignore all of that I think I got my answer
    is_slippery - is the ice slippery?


    Returns the environment
    """

    env = gym.make("FrozenLake",
                   desc=desc,
                   map_name=map_name,
                   is_slippery=is_slippery)

    return env

    """Ok well the problem is that I'm just returning an entire module"""
