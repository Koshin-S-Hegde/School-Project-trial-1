from typing import Type

from pygame import Vector2
from pygame.sprite import AbstractGroup

from src.objects import KineticObject, Object


class Bullet(KineticObject):
    __shooter: Type[Object]

    def __init__(self, direction: Vector2, position: Vector2, *groups: AbstractGroup, shooter: Type[Object]) -> None:
        super().__init__(*groups)
        self.set_size(Vector2(1, 1))
        self.set_position(Vector2(50, 50))
        self.set_velocity(direction * 100)
        self.set_position(position)
        self.__shooter = shooter

    @property
    def shooter(self) -> Type[Object]:
        return self.__shooter
