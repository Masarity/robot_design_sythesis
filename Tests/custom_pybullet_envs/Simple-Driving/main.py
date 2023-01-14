import gym
import torch
from agent import TRPOAgent
import simple_driving
import time
import os


def main():
    nn = torch.nn.Sequential(torch.nn.Linear(8, 64), torch.nn.Tanh(),
                             torch.nn.Linear(64, 2))
    agent = TRPOAgent(policy=nn)

    dir = os.path.dirname(os.path.realpath(__file__))
    agent.load_model(dir + "/agent.pth")
    # agent.train("SimpleDriving-v0", seed=0, batch_size=5000, iterations=100,
    #             max_episode_length=250, verbose=True)
    # agent.save_model("agent.pth")

    env = gym.make('SimpleDriving-v0')
    ob = env.reset()
    i = 100
    while i > 0:
        action = agent(ob)
        ob, _, done, _ = env.step(action)
        env.render()
        i-=1
        if done:
            ob = env.reset()
            time.sleep(1/30)
    env.close()


if __name__ == '__main__':
    main()