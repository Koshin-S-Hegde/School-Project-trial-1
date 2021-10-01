import pygame.key
from pygame import Vector2
from pygame.sprite import AbstractGroup

from src.objects import GravitationalObject


class Player(GravitationalObject):
    __jump_velocity: float
    __is_grounded: bool

    def __init__(self, *groups: AbstractGroup) -> None:
        super().__init__(*groups)
        self.__jump_velocity = 100
        self.is_grounded = True
        self._set_size(Vector2(10, 10))
        self._set_image_path("images/player.png")

    @property
    def is_grounded(self) -> bool:
        return self.__is_grounded

    @is_grounded.setter
    def is_grounded(self, is_grounded: bool) -> None:
        self.__is_grounded = is_grounded

    def update(self, *args, **kwargs) -> None:
        super(Player, self).update(*args, **kwargs)
        self.__handle_vertical_movement()

    def __handle_vertical_movement(self) -> None:
        if self.is_grounded:
            self._set_gravity(0)
            self._set_velocity(Vector2(self._get_velocity().x, 0))
        else:
            self._set_gravity(100)
        if self.is_grounded and pygame.key.get_pressed()[pygame.key.key_code(" ")]:
            self._set_velocity(Vector2(0, -self.__jump_velocity))
