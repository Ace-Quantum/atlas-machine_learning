#!/usr/bin/env python3

# Ok so take two on this project, 
# as the last two days were eaten by my WSL being down.
# Fingers crossed the same doesn't happen again.

# Following this tutorial from David:
# https://www.youtube.com/watch?v=2nonlRp3vT0
# I had initially tried to follow one using tensorflow and keras
# But I'm assuming the support from gym with that one was depreciated.

import gym
import numpy as np
from PIL import Image
import torch
from im_stronger_than_ive_been_before import *

# print("ran successfully")

# This is where we might set an os environ
# But honestly I'm leaving it out
# because holy heck is it actually scary

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

environment = DQNBreakout(device=device, render_mode='human')

state = environment.reset()

for _ in range(100):
    action = environment.action_space.sample()

    state, reward, done, info = environment.step(action)

    print(state.shape)
