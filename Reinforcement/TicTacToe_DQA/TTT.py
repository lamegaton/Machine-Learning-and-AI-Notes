from TTT_DQA_agent import DQNAgent
from TTT_env import TicTacToe
import numpy as np

EPISODES = 1000
BATCH_SIZE = 32

env = TicTacToe()
agent = DQNAgent()

for e in range(EPISODES):
    state = env.reset()
    state = np.reshape(state, [1, agent.state_size])
    while True:
        action = agent.act(state)
        next_state, reward, done = env.step(action)
        next_state = np.reshape(next_state, [1, agent.state_size])
        agent.remember(state, action, reward, next_state, done)
        state = next_state
        if done:
            print(f"Episode: {e}/{EPISODES}, score: {reward}")
            break

    if len(agent.memory) > BATCH_SIZE:
        agent.replay(BATCH_SIZE)
