#!/usr/bin/env python3

"""This is where we're going to train table
so that it becomes less stupid in a more optimal set up.
Honestly I'm thinking of just following this tutorial
and saying F it? I'm not sure how I'll impliment the policy gradient.
https://www.janisklaise.com/post/rl-policy-gradients/"""

import numpy as np
policy_gradient = __import__('policy_gradient').policy_gradient


def train(env, nb_episodes, alpha=0.000045, gamma=0.98):
    """I'm *pretty* sure that we're not training a full model here
    Just filling out the Q table
    Unless it's not the Q table anymore?
    env - initial environment
    nb_episodes - the number of episodes
    alpha - learning rate
    gamma - discount factor"""

    episode_rewards = []

    for i in range(nb_episodes):

        # Running a single episode
        observation = env.reset()
        totalreward = 0

        observations = []
        actions = []
        rewards = []
        probs = []

        done = False

        while not done:

            observations.append(observation)
            action, prob = policy_gradient(observation)
            observation, reward, done, info = env.step(action)

            totalreward += reward
            rewards.append(reward)
            actions.append(action)
            probs.append(prob)

        rewards = np.array(rewards)
        observations = np.array(observations)
        actions = np.array(actions)
        probs = np.array(probs)

        episode_rewards.append(totalreward)

        # Update the policy
        # This is what makes this robot less stupid 
        # than one that just uses Q learning.
        # In my understanding
        # Status update
        # How the FRICK do I update a policy???
        # Do I just maybe run and print?? 
        # The worst that happens is that it doesn't work I guess
        print(f"Episode: {i} Score: {totalreward}")

    return totalreward
