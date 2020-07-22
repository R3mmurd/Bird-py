"""
This file contains the implementation of the class ScoreState.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/12/2020
"""
import pygame

import settings

from states.base_state import BaseState
from render import render_text


class ScoreState(BaseState):
    def enter(self, score):
        self.score = score

    def update(self, dt):
        if settings.pressed_keys.get(pygame.K_RETURN):
            self.state_machine.change('count')

    def render(self, surface):
        render_text(
            surface, 'Oops! You lost!', 'large',
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//2 - 30,
            center=True
        )
        render_text(
            surface, f'Score: {self.score}', 'medium',
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//2 + 10,
            center=True
        )
        render_text(
            surface, 'Press Enter to Play Again!', 'medium',
            settings.VIRTUAL_WIDTH//2, settings.VIRTUAL_HEIGHT//2 + 80,
            center=True
        )
