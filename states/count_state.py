"""
This file contains the implementation of the class CountState.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/12/2020
"""
import pygame

import settings

from states.base_state import BaseState
from render import render_text


class CountState(BaseState):
    def enter(self):
        self.current_time = 3
        self.timer = 0

    def update(self, dt):
        self.timer += dt
        if self.timer >= 1:
            self.current_time -= 1
            self.timer %= 1

            if self.current_time == 0:
                self.state_machine.change('play')

    def render(self, surface):
        render_text(
            surface, f'{self.current_time}', 'huge',
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//2 - 20,
            center=True
        )
