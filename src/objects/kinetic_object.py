from pygame.math import Vector2
from pygame.sprite import AbstractGroup
from src.objects.object import Object


class KineticObject(Object):
    __velocity: Vector2
    __acceleration: Vector2

    def __init__(self, *groups: AbstractGroup) -> None:
        super().__init__(*groups)
        self.set_velocity(Vector2(0, 0))
        self.set_acceleration(Vector2(0, 0))

    def _translate(self, displacement: Vector2) -> None:
        self.set_position(self.get_position() + displacement)

    def set_velocity(self, velocity: Vector2) -> None:
        self.__velocity = velocity

    def get_velocity(self) -> Vector2:
        return self.__velocity

    def set_acceleration(self, acceleration: Vector2) -> None:
        self.__acceleration = acceleration

    def get_acceleration(self) -> Vector2:
        return self.__acceleration

    def update(self, *args, **kwargs) -> None:
        super(KineticObject, self).update(*args, **kwargs)
        self._translate(self.get_velocity() * kwargs["delta_time"])
        self.set_velocity(self.get_velocity() + self.get_acceleration() * kwargs["delta_time"])
