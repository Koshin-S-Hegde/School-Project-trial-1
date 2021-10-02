from pygame.math import Vector2
from pygame.sprite import AbstractGroup

from src.objects.kinetic_object import KineticObject


class GravitationalObject(KineticObject):
    __gravity: float

    def __init__(self, *groups: AbstractGroup) -> None:
        super().__init__(*groups)
        self.set_gravity(0)

    def set_gravity(self, gravity: float) -> None:
        self.__gravity = gravity

    def get_gravity(self) -> float:
        return self.__gravity

    def update(self, *args, **kwargs) -> None:
        super(GravitationalObject, self).update(*args, **kwargs)
        self.set_velocity(
            self.get_velocity() + Vector2(0, self.__gravity) * kwargs["delta_time"]
        )
