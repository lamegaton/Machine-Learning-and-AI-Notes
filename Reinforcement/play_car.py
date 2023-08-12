import gymnasium as gym
from gym.utils.play import play
import pygame

# map the actions with actions in mountain car
# https://github.com/openai/gym/wiki/MountainCar-v0
mapping = {(pygame.K_LEFT,): 0, (pygame.K_RIGHT,): 2, (pygame.K_DOWN,): 1}
play(gym.make('MountainCar-v0', render_mode='rgb_array'), keys_to_action=mapping)