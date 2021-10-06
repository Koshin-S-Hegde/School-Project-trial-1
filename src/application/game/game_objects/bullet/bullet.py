from typing import Type

from pygame import Vector2
from pygame.sprite import AbstractGroup

from src.objects import KineticObject, Object


class Bullet(KineticObject):
    __damage: float

    def __init__(self, direction: Vector2, position: Vector2, damage: float, *groups: AbstractGroup) -> None:
        super().__init__(*groups)
        self.set_size(Vector2(1, 1))
        self.set_position(Vector2(50, 50))
        self.set_velocity(direction * 100)
        self.set_position(position)
        self.__damage = damage

    @property
    def damage(self) -> float:
        return self.__damage
