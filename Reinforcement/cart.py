import gymnasium as gym
import pygame
from gymnasium.utils.play import play
mapping = {(pygame.K_LEFT,): 0, (pygame.K_RIGHT,): 1}
play(gym.make("CartPole-v1", render_mode='rgb_array_list'), keys_to_action=mapping)