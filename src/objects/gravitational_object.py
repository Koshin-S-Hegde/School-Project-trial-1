from pygame.math import Vector2
from pygame.sprite import AbstractGroup

from src.objects.kinetic_object import KineticObject


class GravitationalObject(KineticObject):
    __gravity: float

    def __init__(self, *groups: AbstractGroup) -> None:
        super().__init__(*groups)
        self._set_gravity(0)

    def _set_gravity(self, gravity: float) -> None:
        self.__gravity = gravity

    def _get_gravity(self) -> float:
        return self.__gravity

    def update(self, *args, **kwargs) -> None:
        super(GravitationalObject, self).update(*args, **kwargs)
        self._set_velocity(
            self._get_velocity() + Vector2(0, self.__gravity) * kwargs["delta_time"]
        )
