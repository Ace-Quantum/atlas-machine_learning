#!/usr/bin/env python3

import copy
import random
import torch
import torch.optim as optim
import torch.nn.functional as F
from plot import LivePlot
import numpy as np
import time

class ReplayMemory:

    def __init__(self, capacity, device='cpu'):
        self.capacity = capacity
        self.memory = []
        self.position = 0
        self.device = device
        self.memory_max_report = 0

    def insert(self, transition):
        """This could be done better
        The tutorial even states so
        But with 2 days lost to a WSL crash
        I've not the time to find a solution"""
        transition = [item.to('cpu') for item in transition]

        if len(self.memory) < self.capacity:
            self.memory.append(transition)
        else:
            self.memory.remove(self.memory[0])
            self.memory.append(transition)

    def sample(self, batch_size=32):
        assert self.can_sample(batch_size)

        batch = random.sample(self.memory, batch_size)
        batch = zip(*batch)
        return [torch.cat(items).to(self.device) for items in batch]

    def can_sample(self, batch_size):
        return len(self.memory) >= batch_size * 10

    def __len__(self):
        return len(self.memory)

class Agent:
    
    def __init__(self, model, device='cpu',
        epsilon=1.0, min_epsilon=0.1, nb_warmup=10000,
        nb_actions=None, memory_capacity=10000,
        batch_size=32, learning_rate=0.00025):

        self.memory = ReplayMemory(device=device, capacity=memory_capacity)
        self.model = model
        self.target_model = copy.deepcopy(model).eval()
        # Not sure exactly what this does tbh

        self.epsilon = epsilon
        self.min_epsilon = min_epsilon

        # Time for big scary equation!!!
        # Oh shit there's other formulas for epsilon decay
        # I mean it makes sense but still
        self.epsilon_decay = 1 - (((epsilon - min_epsilon) / nb_warmup) * 2)

        self.batch_size = batch_size
        self.model.to(device)
        self.target_model.to(device)
        self.gamma = 0.99
        self.nb_actions = nb_actions

        self.optimizer = optim.Adam(model.parameters(), lr = learning_rate)

        print(f"Starting epsilon is {self.epsilon}")
        print(f"Epsilon decay is {self.epsilon_decay}")

    def get_action(self, state):
        if torch.rand(1) < self.epsilon:
            return torch.randint(self.nb_actions, (1, 1))
        else:
            av = self.model(state).detach()
            return torch.argmax(av, dim=1, keepdim=True)

    def train(self, env, epochs):
        stats = {'Returns': [], 'AvgReturns': [], 'EpsilonCheckpoint': []}

        plotter = LivePlot()

        for epoch in range(1, epochs + 1):
            state = env.reset()
            done = False
            ep_return = 0
            print(f"Epoch: {epoch}")

            while not done:
                action = self.get_action(state)

                next_state, reward, done, info = env.step(action)

                self.memory.insert([state, action, reward, done, next_state])

                if self.memory.can_sample(self.batch_size):
                    state_b, action_b, reward_b, done_b, next_state_b = self.memory.sample(self.batch_size)
                    # ^^^ batches of states and whatnot

                    qsa_b = self.model(state_b).gather(1, action_b)
                    next_qsa_b = self.target_model(next_state_b)
                    next_qsa_b = torch.max(next_qsa_b, dim=-1, keepdim=True)[0]

                    # The tilda does a thing I don't fully get
                    target_b = reward_b + ~done_b * self.gamma * next_qsa_b

                    loss = F.mse_loss(qsa_b, target_b)

                    self.model.zero_grad()
                    loss.backward()

                    self.optimizer.step()

                state = next_state
                ep_return += reward.item()

            stats['Returns'].append(ep_return)

            if self.epsilon > self.min_epsilon:
                self.epsilon = self.epsilon * self.epsilon_decay

            if epoch % 10 == 0:
                self.model.save_the_model()
                print(" ")

                average_returns = np.mean(stats['Returns'][-100:])

                stats['AvgReturns'].append(average_returns)
                stats['EpsilonCheckpoint'].append(self.epsilon)

                if (len(stats['Returns'])) > 100:
                    print(f"Epoch: {epoch} - Average Return: {average_returns} - Epsilon: {self.epsilon}")
                else:
                    print(f"Epoch: {epoch} - Episode Return: {np.mean(stats['Returns'][-1:])} - Epsilon: {self.epsilon}")
                
            if epoch % 100 == 0:
                self.target_model.load_state_dict(self.model.state_dict())

                plotter.update_plot(stats)

            if epoch % 1000 == 0:
                self.model.save_the_model(f"models/model_iter_{epoch}.pt")

        return stats

    def test(self, env):
        
        for epoch in range(1, 3):
            state = env.reset()

            done = False

            for _ in range(1000):
                time.sleep(0.01)
                action = self.get_action(state)
                state, reward, done, info = env.step(action)
                if done:
                    break
