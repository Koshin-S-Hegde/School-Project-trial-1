from typing import Type

import pygame.surface
from pygame import Vector2
from pygame.sprite import Group

from src.application.game.game_objects.bullet.bullet import Bullet
from src.objects import Object


class BulletHandler:
    __bullet_group: Group
    __TOTAL_SHOOT_COOL_DOWN: float
    __shoot_cool_down_left: float

    def __init__(self) -> None:
        self.__bullet_group = Group()
        self.__TOTAL_SHOOT_COOL_DOWN = 1
        self.__shoot_cool_down_left = self.__TOTAL_SHOOT_COOL_DOWN

    def update(
            self,
            delta_time: float,
            shooter_position: Vector2,
            absolute_target_position: tuple,
            shooter: Type[Object]
    ) -> None:
        target_position = Vector2([
            absolute_target_position[i] * 100 / pygame.display.get_window_size()[i] for i in range(2)
        ])
        direction: Vector2 = (target_position - shooter_position).normalize()
        if pygame.mouse.get_pressed(3)[0] and self.__shoot_cool_down_left <= 0:
            self.__bullet_group.add(Bullet(direction, shooter_position, shooter=shooter))
            self.__shoot_cool_down_left = self.__TOTAL_SHOOT_COOL_DOWN
        self.__shoot_cool_down_left -= delta_time
        self.__bullet_group.update(delta_time=delta_time)

    def render(self) -> None:
        self.__bullet_group.draw(pygame.display.get_surface())

    @property
    def bullet_group(self) -> Group:
        return self.__bullet_group
