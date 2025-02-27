#!/usr/bin/env python3

# Note for future Ace: 
# consider changing the model to a smaller structure 
# to save on some training time

# Very simple model building, surprisingly easy for a library I hadn't worked much with.
# Not too terribly much to say in the documentation, it's all architecture

import torch
import torch.nn as nn
import os

class NamcoBoi(nn.Module):

    def __init__(self, nb_actions=4):
        super(NamcoBoi, self).__init__()

        self.relu = nn.ReLU()

        self.conv1 = nn.Conv2d(1, 32, kernel_size=(8,8), stride=(4,4))
        self.conv2 = nn.Conv2d(32, 64, kernel_size=(4,4), stride=(2,2))
        self.conv3 = nn.Conv2d(64, 64, kernel_size=(3,3), stride=(1,1))

        self.flatten = nn.Flatten()

        self.dropout = nn.Dropout(p=0.2)

        self.action_value1 = nn.Linear(3136, 1024)
        self.action_value2 = nn.Linear(1024, 1024)
        self.action_value3 = nn.Linear(1024, nb_actions)

        self.state_value1 = nn.Linear(3136, 1024)
        self.state_value2 = nn.Linear(1024, 1024)
        self.state_value3 = nn.Linear(1024, 1)

    def forward(self, x):
        x = torch.Tensor(x)
        x = self.relu(self.conv1(x))
        x = self.relu(self.conv2(x))
        x = self.relu(self.conv3(x))
        x = self.flatten(x)

        state_value = self.relu(self.state_value1(x))
        state_value = self.dropout(state_value)
        state_value = self.relu(self.state_value2(state_value))
        state_value = self.dropout(state_value)
        state_value = self.relu(self.state_value3(state_value))

        action_value = self.relu(self.action_value1(x))
        action_value = self.dropout(action_value)
        # I'm not sure if this next line is correct
        # The tutorial references "action_value1" here
        # But in that case there's no reference to action_value2
        action_value = self.relu(self.action_value2(action_value))
        action_value = self.dropout(action_value)
        action_value = self.action_value3(action_value)

        output = state_value + (action_value - action_value.mean())

        return output

    def save_the_model(self, weights_filename='models/latest.pt'):
        # This is going to need to be an H5 file for the final piece
        # Unsure if it works the same way
        # This is just the weights
        # But I think h5 files are the same
        #   I'm gonna leave it as is
        #   Because I know that it works
        if not os.path.exists("models"):
            print("making path")
            os.makedirs("models")

        torch.save(self.state_dict(), weights_filename)

    def load_the_model(self, weights_filename='models/latest.pt'):
        try:
            self.load_state_dict(torch.load(weights_filename))
            print(f"Successfully loaded weights file {weights_filename}")
        except:
            print(f"Ur Ducked")
