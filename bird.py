"""
This file contains the implememtation of the class Bird.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/11/2020
"""
import pygame

import settings


class Bird:
    def __init__(self):
        self.texture = settings.GAME_TEXTURES['bird']
        self.width = self.texture.get_size()[0]
        self.height = self.texture.get_size()[1]
        self.x = settings.VIRTUAL_WIDTH//2 - self.width//2
        self.y = settings.VIRTUAL_HEIGHT//2 - self.height//2
        self.vy = 0

    def get_collision_rect(self):
        return pygame.Rect(self.x + 4, self.y + 1, 31, 24)

    def collides(self, log):
        return self.get_collision_rect().colliderect(
            log.get_collision_rect()
        )
    
    def update(self, dt):
        self.vy += settings.GRAVITY * dt

        if settings.pressed_keys.get(pygame.K_SPACE):
            settings.GAME_SOUNDS['jump'].play()
            self.vy = -220

        self.y += self.vy * dt

    def render(self, surface):
        surface.blit(self.texture, (self.x, self.y))
