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

    def __init__(self, total_shoot_cool_down: float) -> None:
        self.__bullet_group = Group()
        self.__TOTAL_SHOOT_COOL_DOWN = total_shoot_cool_down
        self.__shoot_cool_down_left = self.__TOTAL_SHOOT_COOL_DOWN

    def update(self, delta_time: float) -> None:
        self.__shoot_cool_down_left -= delta_time
        self.__bullet_group.update(delta_time=delta_time)

    def shoot(
            self,
            shooter_position: Vector2,
            target_position: Vector2,
            damage: float
    ) -> None:
        if self.__shoot_cool_down_left <= 0:
            direction: Vector2 = (target_position - shooter_position).normalize()
            self.__bullet_group.add(Bullet(direction, shooter_position, damage=damage))
            self.__shoot_cool_down_left = self.__TOTAL_SHOOT_COOL_DOWN

    def render(self) -> None:
        self.__bullet_group.draw(pygame.display.get_surface())

    @property
    def bullet_group(self) -> Group:
        return self.__bullet_group
