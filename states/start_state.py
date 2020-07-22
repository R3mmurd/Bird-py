"""
This file contains the implementation of the class StartState.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/12/2020
"""
import pygame

import settings

from states.base_state import BaseState
from render import render_text


class StartState(BaseState):
    def update(self, dt):   
        if settings.pressed_keys.get(pygame.K_RETURN):
            self.state_machine.change('count')

    def render(self, surface):
        render_text(
            surface, 'Bird', 'large',
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//2 - 30,
            center=True
        )
        render_text(
            surface, 'Press Enter', 'medium',
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//2 + 10,
            center=True
        )
