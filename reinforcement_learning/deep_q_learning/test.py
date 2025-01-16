#!/usr/bin/env python3

# tbh the tutorial talks about how this could've just been done in the main file
# But this is exactly the hack and slash that I live for
# I know it's not optimized
# But neither am I

import gym
import numpy as np
from PIL import Image
import torch
from breakout import *
from model import NamcoBoi
from agent import Agent

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

environment = DQNBreakout(device=device, render_mode='human')

model = NamcoBoi(nb_actions=4)

model.to(device)

model.load_the_model()

agent = Agent(model=model, device=device, epsilon=1.0, nb_warmup=5000,
                nb_actions=4, learning_rate=0.00001, memory_capacity=1000000,
                batch_size=64)

agent.test(env=environment)
