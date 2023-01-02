"""
This file contains the implememtation of the class Log.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/11/2020
"""
import random

import pygame

import settings

from log import Log


class LogPair:
    def __init__(self, x, y):
        self.x = x
        self.lower_log = Log(x, y, 'lower')
        gap = settings.LOG_GAP + random.randint(-10, 15)
        self.upper_log = Log(x, y - settings.LOG_HEIGHT - gap, 'upper')
        self.remove = False
        self.scored = False

    def collides(self, bird):
        return (
            bird.collides(self.lower_log) or bird.collides(self.upper_log)
        )

    def update(self, dt):
        if self.x < -settings.LOG_WIDTH:
            self.remove = True
        else:
            self.x += -settings.LOG_SPEED * dt
            self.lower_log.x = self.x
            self.upper_log.x = self.x

    def render(self, surface):
        self.lower_log.render(surface)
        self.upper_log.render(surface)
