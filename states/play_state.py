"""
This file contains the implementation of the class StatePlay.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/12/2020
"""
import random

import pygame

import settings

from bird import Bird
from log_pair import LogPair

from states.base_state import BaseState
from render import render_text


class PlayState(BaseState):
    def enter(self):
        self.score = 0
        self.bird = Bird()

        self.logs = []

        # The first log will be generated to seconds after the beginning.
        self.logs_time = 2
        # Time counter to generate logs
        self.logs_timer = 0

        # Assume a fake last generated log and store the y value
        self.last_log_y = random.randint(100, settings.VIRTUAL_HEIGHT-20)

    def update(self, dt):
        if settings.pressed_keys.get(pygame.K_p):
            settings.GAME_SOUNDS['pause'].play()
            settings.paused = not settings.paused
            if settings.paused:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()

        if settings.paused:
            return

        self.logs_timer += dt
        if self.logs_timer >= self.logs_time:
            # The next log will have, as maximum, 20 pixels
            # of height difference with the last one. This is
            # to grant a smooth height change between logs.
            next_y = self.last_log_y + random.randint(-20, 20)

            # Ensure that next_y is neither less than 100 nor
            # greater than VIRTUAL_HEIGHT - 20
            next_y = max(100, min(next_y, settings.VIRTUAL_HEIGHT - 20))

            # Update the value of last_log_y
            self.last_log_y = next_y

            self.logs.append(LogPair(settings.VIRTUAL_WIDTH, next_y))
            self.logs_timer %= self.logs_time

            # Generate a new time for the next log.
            # It needs at least 70/60 seconds to generate the next log
            # without overlap.
            self.logs_time = random.uniform(1.2, 2.5)

        self.bird.update(dt)

        if (self.bird.get_collision_rect().bottom >
                settings.VIRTUAL_HEIGHT - settings.GROUND_HEIGHT):
            settings.GAME_SOUNDS['death'].play()
            self.state_machine.change('score', score=self.score)

        for log in self.logs:
            log.update(dt)
            if log.collides(self.bird):
                settings.GAME_SOUNDS['death'].play()
                self.state_machine.change('score', score=self.score)
            if self.bird.x > log.x + settings.LOG_WIDTH and not log.scored:
                settings.GAME_SOUNDS['score'].play()
                log.scored = True
                self.score += 1

        self.logs = [log for log in self.logs if not log.remove]

    def render(self, surface):
        for log in self.logs:
            log.render(surface)

        self.bird.render(surface)
        render_text(surface, f'Score: {self.score}', 'large', 5, 5)
