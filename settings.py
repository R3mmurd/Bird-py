"""Game settings

This file contains all game settings such window dimensions, resolution,
default objects values, textures, sounds, fonts, etc.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/11/2020
"""
import pygame

pygame.init()

# Physical screen dimensions
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Virtual resolution dimensions
VIRTUAL_WIDTH = 512
VIRTUAL_HEIGHT = 288

# Point where the background image is repeated
BACKGROUND_LOOP_POINT = 1157

# Height of the ground image
GROUND_HEIGHT = 16

GROUND_SPEED = 60
# Log speed is the same as the ground
LOG_SPEED = 60
# Background speed is lower to give the feeling that it is the horizon
BACKGROUND_SPEED = 30

# Log dimensions
LOG_WIDTH = 70
LOG_HEIGHT = 288

# The gap between the upper and lower log
LOG_GAP = 80

# GRAVITY is an acceleration value
GRAVITY = 980

# Dictionary of sound effects
GAME_SOUNDS = {
    'jump': pygame.mixer.Sound('sounds/jump.wav'),
    'score': pygame.mixer.Sound('sounds/score.wav'),
    'death': pygame.mixer.Sound('sounds/death.wav'),
    'pause': pygame.mixer.Sound('sounds/pause.wav'),
}

# Dictionary of different sizes for fonts
GAME_FONTS = {
    'medium': pygame.font.Font('fonts/flappy.ttf', 18),
    'large': pygame.font.Font('fonts/flappy.ttf', 30),
    'huge': pygame.font.Font('fonts/flappy.ttf', 60),
}

# Dictionary of game images
GAME_TEXTURES = {
    'background': pygame.image.load('graphics/background.png'),
    'ground': pygame.image.load('graphics/ground.png'),
    'bird': pygame.image.load('graphics/bird.png'),
    'log': pygame.image.load('graphics/log.png'),
}

# This dictionary is initialized empty.
# When a key is pressed (detected by the KEYDOWN event),
# it will be added to this dictionary associating it the value True.
#
# Usage:
# To check whether the key "return" has been pressed
#
# if pressed_keys.get(pygame.K_RETURN):
#    # Action for RETURN key presed
pressed_keys = {}

# Global variable to indicate that the game is paused
paused = False
