"""
This file contains the implememtation of the class Log.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/11/2020
"""
import pygame

import settings


class Log:
    def __init__(self, x, y, position):
        if position == 'lower':
            self.texture = settings.GAME_TEXTURES['log']
        else:
            self.texture = pygame.transform.flip(
                settings.GAME_TEXTURES['log'], False, True
            )
        self.x = x
        self.y = y
        self.width = self.texture.get_size()[0]
        self.height = self.texture.get_size()[1]
        self.position = position

    def get_collision_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, dt):
        pass

    def render(self, surface):
        surface.blit(self.texture, (self.x, self.y))
