"""Main

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/11/2020
"""
import sys
import random

import pygame

import settings

from state_machine import StateMachine
import states


class BirdGame:
    def __init__(self):
        # Setting the screen
        self.screen = pygame.display.set_mode(
            (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
        )
        pygame.display.set_caption('Bird')

        # Creating the virtual screen
        self.surface = pygame.Surface(
            (settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT)
        )

        self.background_x = 0
        self.ground_x = 0

        self.clock = pygame.time.Clock()

        self.state_machine = StateMachine({
            'start': states.StartState,
            'count': states.CountState,
            'play': states.PlayState,
            'score': states.ScoreState,
        })
        self.state_machine.change('start')
        pygame.mixer.music.load('sounds/choco_birds_run.mp3')
        pygame.mixer.music.play(loops=-1)

        settings.GAME_SOUNDS['jump'].set_volume(0.5)
        settings.GAME_SOUNDS['death'].set_volume(0.5)

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
                    else:
                        settings.pressed_keys[event.key] = True
            
            dt = self.clock.tick() / 1000
            self.update(dt)
            self.render()
            settings.pressed_keys = {}
    
    def update(self, dt):
        if not settings.paused:
            self.background_x = (
                (self.background_x + settings.BACKGROUND_SPEED * dt)
                % settings.BACKGROUND_LOOP_POINT
            )
            self.ground_x = (
                (self.ground_x + settings.GROUND_SPEED * dt)
                % settings.VIRTUAL_WIDTH
                )
        self.state_machine.update(dt)

    def render(self):
        self.surface.fill((0, 0, 0))

        self.surface.blit(
            settings.GAME_TEXTURES['background'],
            (int(-self.background_x), 0)
        )
        
        self.state_machine.render(self.surface)

        self.surface.blit(
            settings.GAME_TEXTURES['ground'],
            (
                int(-self.ground_x),
                settings.VIRTUAL_HEIGHT - settings.GROUND_HEIGHT
            )
        )

        self.screen.blit(
            pygame.transform.scale(self.surface, self.screen.get_size()),
            (0, 0)
        )
        pygame.display.update()


if __name__ == '__main__':
    game = BirdGame()
    game.loop()
