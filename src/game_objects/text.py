import pygame.font
from pygame import Vector2
from pygame.sprite import AbstractGroup

from src.game_objects import GameObject


class Text(GameObject):
    __text_style: str
    __text_quality: int
    __text_color: tuple
    text_position: Vector2
    __font: pygame.font.Font

    def __init__(self, custom_text: str, text_style: str,
                 text_color: tuple, text_quality: int, *groups: AbstractGroup) -> None:
        super().__init__(*groups)
        self.__custom_text = custom_text
        self.__text_style = text_style
        self.__text_color = text_color
        self.__text_quality = text_quality
        self.__font = pygame.font.Font(self.__text_style, self.__text_quality)
        self.set_image_surface(self.__font.render(self.__custom_text, True, self.__text_color))

    def set_custom_text(self, custom_text: str) -> None:
        self.__custom_text = custom_text
        self.set_image_surface(self.__font.render(self.__custom_text, True, self.__text_color))

    def set_text_color(self, color_tuple: tuple) -> None:
        self.__text_color = color_tuple
        self.set_image_surface(self.__font.render(self.__custom_text, True, self.__text_color))

    def set_text_style(self, font_style: str) -> None:
        self.__text_style = font_style
        self.__font = pygame.font.Font(self.__text_style, self.__text_quality)

    def set_text_quality(self, text_quality: int) -> None:
        self.__text_quality = text_quality
        self.__font = pygame.font.Font(self.__text_style, self.__text_quality)

    def update(self, *args, **kwargs) -> None:
        super(Text, self).update(*args, **kwargs)
