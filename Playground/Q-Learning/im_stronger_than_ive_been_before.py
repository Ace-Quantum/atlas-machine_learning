#!/usr/bin/env python3

import collections
import cv2
import gym
import numpy as np
from PIL import Image
import torch

# print("ran successfully")

class DQNBreakout(gym.Wrapper):

    def __init__(self,
        render_mode='rgb_array',
        repeat=4, device='cpu'):
        
        env = gym.make("BreakoutNoFrameskip-v4", render_mode=render_mode)

        super(DQNBreakout, self).__init__(env)

        self.repeat = repeat
        self.lives = env.ale.lives()
        self.frame_buffer = []
        self.device = device

    def step(self, action):

        total_reward = 0
        done = False

        for i in range(self.repeat):
            observation, reward, done, truncated, info = self.env.step(action)

            total_reward += reward

            print(info, total_reward)

            self.frame_buffer.append(observation)

            if done:
                break

        max_frame = np.max(self.frame_buffer[-2:], axis=0)
        # max_frame = max_frame.to(self.device)
        # Commented out due to the need for future processing

        return max_frame, total_reward, done, info
