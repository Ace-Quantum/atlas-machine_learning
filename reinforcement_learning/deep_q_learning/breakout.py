#!/usr/bin/env python3
# Honestly this is kind of where I struggle the most with this project
# I wish I could write more documentation off the top of my head 
# but I'll need to watch the tutorial again instead

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
        
        # Pull out the Breakout environment from gymnasium
        env = gym.make("BreakoutNoFrameskip-v4", render_mode=render_mode)

        # call the class we inherited from to initiate our environment
        super(DQNBreakout, self).__init__(env)

        # Set up our variables
        self.image_shape = (84, 84)
        self.repeat = repeat
        self.lives = env.ale.lives()
        self.frame_buffer = []
        self.device = device

    def step(self, action):
        # From what I can tell, this is a singular step in the Q-Table
        # Which will be called multiple times in the Agent's training.

        total_reward = 0
        done = False

        for i in range(self.repeat):
            observation, reward, done, truncated, info = self.env.step(action)

            total_reward += reward

            # print(info, total_reward)

            current_lives = info['lives']

            if current_lives < self.lives:
                # Negative reward for losing a life
                total_reward = total_reward - 1
                self.lives = current_lives

            # print(f"Lives: {self.lives} Total Reward: {total_reward}")

            self.frame_buffer.append(observation)

            if done:
                break

        max_frame = np.max(self.frame_buffer[-2:], axis=0)

        max_frame = self.process_observation(max_frame)
        max_frame = max_frame.to(self.device)

        total_reward = torch.tensor(total_reward).view(1, -1).float()
        total_reward = total_reward.to(self.device)

        done = torch.tensor(done).view(1, -1)
        done = done.to(self.device)

        return max_frame, total_reward, done, info

    def reset(self):
        self.frame_buffer = []

        observation, _ = self.env.reset()

        self.lives = self.env.ale.lives()

        observation = self.process_observation(observation)

        return observation

    def process_observation(self, observation):

        img = Image.fromarray(observation)
        img = img.resize(self.image_shape)
        img = img.convert("L")
        img = np.array(img)
        img = torch.from_numpy(img)
        img = img.unsqueeze(0)
        img = img.unsqueeze(0)
        img = img / 255.0

        img = img.to(self.device)

        return img
