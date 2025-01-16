#!/usr/bin/env python3

# Ok so take two on this project, 
# as the last two days were eaten by my WSL being down.
# Fingers crossed the same doesn't happen again.
#   To be clear, this code is copy and pasted from the files in my playground
#   It ran decently in playground, so it should be ok here.
#   It does run (at least locally)
#   But I haven't actually trained the model itself yet
#   I'll be doing so throughout tonight and tomorrow

# Following this tutorial from David:
# https://www.youtube.com/watch?v=2nonlRp3vT0
# I had initially tried to follow one using tensorflow and keras
# But I'm assuming the support from gym with that one was depreciated.

import gym
import numpy as np
from PIL import Image
import torch
from breakout import *
from model import NamcoBoi
from agent import Agent

# print("ran successfully")

# This is where we might set an os environ
# But honestly I'm leaving it out
# because holy heck is it actually scary
# Looks like we didn't need to do so, 
# So we're sitting pretty there

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

# calling to build the environment
environment = DQNBreakout(device=device)

# building the model
model = NamcoBoi(nb_actions=4)

# Tbh I actually don't know what model.to does.
# I'm guessing it just like... makes the thing go.
# Another thing to recheck with the tutorial
model.to(device)

# If a model exists load it
model.load_the_model()

# Will probably choose to increase the learning rate for the
# sake of time and processing power
# Might not change model architecture like previously noted
# It's fairly small and simple
agent = Agent(model=model, device=device, epsilon=1.0, nb_warmup=5000,
                nb_actions=4, learning_rate=0.00001, memory_capacity=1000000,
                batch_size=64)

# This is a MASSIVE amount of epochs.
# Might change it when I actually run it.
agent.train(env=environment, epochs=2000000)

# To be reinstated later?
# for _ in range(100):
#     action = environment.action_space.sample()

#     state, reward, done, info = environment.step(action)

#     print(state.shape)
