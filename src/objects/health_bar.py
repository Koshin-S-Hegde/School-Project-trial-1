import pygame.display
from pygame import Vector2
from pygame.sprite import Group

from src.objects import Object
from src.objects.living_object import LivingObject


class HealthBar:
    __foreground: Object
    __initial_foreground_size: Vector2
    __health_bar_group: Group
    __living_object: LivingObject
    __initial_health: float
    __initial_position: float

    def __init__(self, living_object: LivingObject) -> None:
        self.__living_object = living_object
        self.__initial_health = living_object.health

        self.__initial_position: Vector2 = Vector2(10, 90)

        background = Object()
        background.set_image_path("images/health_bar_background.png")
        background.set_position(self.__initial_position)
        background.set_size(Vector2(11, 11))

        self.__foreground = Object()
        self.__foreground.set_image_path("images/health_bar_foreground.png")
        self.__foreground.set_position(self.__initial_position)
        self.__initial_foreground_size = Vector2(10, 10)
        self.__foreground.set_size(self.__initial_foreground_size)

        self.__health_bar_group = Group()
        self.__health_bar_group.add(background, self.__foreground)

    def update(self, delta_time: float) -> None:
        if self.__initial_health <= 0:
            return

        health_change_ratio: float = (self.__living_object.health / self.__initial_health)
        current_size_x = self.__initial_foreground_size.x * health_change_ratio
        current_position_x = self.__initial_position.x + (current_size_x - self.__initial_foreground_size.x) / 2

        self.__foreground.set_size(Vector2(
            current_size_x,
            self.__foreground.get_size().y
        ))
        self.__foreground.set_position(Vector2(
            current_position_x,
            self.__foreground.get_position().y
        ))

        self.__health_bar_group.update(delta_time=delta_time)

    def render(self) -> None:
        self.__health_bar_group.draw(pygame.display.get_surface())
