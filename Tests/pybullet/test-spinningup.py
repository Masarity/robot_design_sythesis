from spinup import ppo_pytorch as ppo
# from spinup import ppo_tf1 as ppo
import torch
import os
# import tensorflow as tf
import simple_driving
import gym

dir = os.path.dirname(os.path.realpath(__file__))

envName = 'CartPole-v1'
# envName = 'SimpleDriving-v0'
# envName = 'CartPoleBulletEnv-v1'
# envName = 'HumanoidBulletEnv-v0'
# env_fn = lambda : gym.make('SimpleDriving-v0')
env_fn = lambda : gym.make(envName)

# ac_kwargs = dict(hidden_sizes=[64,64], activation=tf.nn.relu)
ac_kwargs = dict(hidden_sizes=[36,36], activation=torch.nn.ReLU)

logger_kwargs = dict(output_dir=dir + '/data/' + envName, exp_name=envName[:-3])

ppo(env_fn=env_fn, ac_kwargs=ac_kwargs, steps_per_epoch=5000, epochs=50, logger_kwargs=logger_kwargs)