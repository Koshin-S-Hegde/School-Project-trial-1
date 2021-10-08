from copy import deepcopy

import pygame.display
from pygame import Vector2
from pygame.sprite import Group

from src.objects import Object


class HealthBar:
    __background: Object
    __foreground: Object
    __health_bar_group: Group
    __position: Vector2
    __foreground_position: Vector2
    __default_foreground_size: Vector2

    def __init__(self) -> None:
        self.__position = Vector2(10, 90)
        self.__foreground_position = deepcopy(self.__position)

        self.__background = Object()
        self.__background.set_image_path("images/health_bar_background.png")
        self.__background.set_size(Vector2(10, 10))
        self.__background.set_position(self.__position)

        self.__foreground = Object()
        self.__foreground.set_image_path("images/health_bar_foreground.png")
        self.__default_foreground_size = Vector2(9, 9)
        self.__foreground.set_size(self.__default_foreground_size)
        self.__foreground.set_position(self.__position)

        self.__health_bar_group = Group(self.__background)
        self.__health_bar_group.add(self.__foreground)

    def update(self, delta_time: float, health: float) -> None:
        self.__health_bar_group.update(delta_time=delta_time)
        if health <= 0:
            return

        current_foreground_x: float = self.__default_foreground_size.x * health
        self.__foreground.set_size(Vector2(current_foreground_x, self.__foreground.get_size().y))

        self.__foreground_position.x = \
            self.__position.x + \
            self.__foreground.get_size().x / 2 - \
            self.__default_foreground_size.x / 2

        self.__foreground.set_position(self.__foreground_position)

    def render(self) -> None:
        self.__health_bar_group.draw(pygame.display.get_surface())
