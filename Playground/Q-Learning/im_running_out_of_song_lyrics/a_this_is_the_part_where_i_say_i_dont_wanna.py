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
from b_im_stronger_than_ive_been_before import *
from c_this_is_the_part_where_i_break_free import NamcoBoi

# print("ran successfully")

# This is where we might set an os environ
# But honestly I'm leaving it out
# because holy heck is it actually scary

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

environment = DQNBreakout(device=device, render_mode='human')

model = NamcoBoi(nb_actions=4)

model.to(device)

model.load_the_model()

state = environment.reset()

print(model.forward(state))

# To be reinstated later?
# for _ in range(100):
#     action = environment.action_space.sample()

#     state, reward, done, info = environment.step(action)

#     print(state.shape)
