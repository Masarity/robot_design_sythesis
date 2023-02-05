from spinup import ppo_pytorch as ppo
# from spinup import dqn_ref_pytorch as dqn_ref
# from spinup import dqn_tf1 as dqn
from spinup import dqn_simple_pytorch as dqn
import torch
import os
import tensorflow as tf
import simple_driving
import gym

dir = os.path.dirname(os.path.realpath(__file__))

# envName = 'Acrobot-v1'
# envName = 'BipedalWalker-v3'
# envName = 'LunarLander-v2'
envName = 'CartPole-v1'
# envName = 'SimpleDriving-v0'
# envName = 'CartPoleBulletEnv-v1'
# envName = 'HumanoidBulletEnv-v0'
# env_fn = lambda : gym.make('SimpleDriving-v0')
env_fn = lambda : gym.make(envName)

# ac_kwargs = dict(hidden_sizes=[24,24], activation=tf.nn.relu)
ac_kwargs = dict(hidden_sizes=[24, 24], activation=torch.nn.ReLU)
# ac_kwargs = dict()

logger_kwargs = dict(output_dir=dir + '/data/' + envName[:-3] + 'server', exp_name='dpn')

# ppo(env_fn=env_fn, ac_kwargs=ac_kwargs, steps_per_epoch=5000, epochs=50, logger_kwargs=logger_kwargs)
dqn(
  env_fn=env_fn, 
  ac_kwargs=ac_kwargs, 
  seed=0,
  steps_per_epoch=500, 
  epochs=6000, 
  replay_size=int(1e6),
  gamma=0.99,
  epsilon_start=1,
  epsilon_decay=1e-5,
  epsilon_end=0.1,
  q_lr=1e-4,
  batch_size=int(100),
  start_steps=1000,
  max_ep_len=500,
  logger_kwargs=logger_kwargs,
  update_freq=1000,
  save_freq=int(1)
  )
