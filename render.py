"""
This file contains an utility function to render text.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/12/2020
"""
import settings


def _render_text(surface, text, font, color, x, y, center=False):
    font_obj = settings.GAME_FONTS[font]
    text_obj = font_obj.render(text, True, color)
    text_rect = text_obj.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.x = x
        text_rect.y = y
    surface.blit(text_obj, text_rect)


def render_text(surface, text, font, x, y, center=False):
    _render_text(surface, text, font, (34, 34, 34), x+2, y+2, center=center)
    _render_text(surface, text, font, (255, 255, 255), x, y, center=center)
