from pygame.math import Vector2
from pygame.sprite import AbstractGroup
from src.objects.object import Object


class KineticObject(Object):
    __velocity: Vector2
    __acceleration: Vector2

    def __init__(self, *groups: AbstractGroup) -> None:
        super().__init__(*groups)
        self._set_velocity(Vector2(0, 0))
        self._set_acceleration(Vector2(0, 0))

    def _translate(self, displacement: Vector2) -> None:
        self._set_position(self._get_position() + displacement)

    def _set_velocity(self, velocity: Vector2) -> None:
        self.__velocity = velocity

    def _get_velocity(self) -> Vector2:
        return self.__velocity

    def _set_acceleration(self, acceleration: Vector2) -> None:
        self.__acceleration = acceleration

    def _get_acceleration(self) -> Vector2:
        return self.__acceleration

    def update(self, *args, **kwargs) -> None:
        super(KineticObject, self).update(*args, **kwargs)
        self._translate(self._get_velocity() * kwargs["delta_time"])
        self._set_velocity(self._get_velocity() + self._get_acceleration() * kwargs["delta_time"])
