import pygame
from pygame.sprite import AbstractGroup

from src.objects.object import Object


class Text(Object):
    def __init__(
            self,
            *groups: AbstractGroup,
            back_ground_color: tuple[int, int, int],
            text_color: tuple[int, int, int],
            size: list[float],
            position: list[float],
            text: str,
            quality: int = 200
    ):
        super().__init__(*groups)
        font = pygame.font.SysFont("ariel", quality)
        font_surface = font.render(text, True, text_color, back_ground_color)

        self._set_image_surface(font_surface)
        self._set_size(size)
        self._set_position(position)
