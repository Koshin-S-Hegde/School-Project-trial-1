import pygame.key
from pygame import Vector2
from pygame.sprite import AbstractGroup

from src.objects import GravitationalObject


class Player(GravitationalObject):
    __jump_velocity: float
    __is_grounded: bool
    __is_jumping: bool
    __jump_time: float
    __time_since_jump_started: float

    def __init__(self, *groups: AbstractGroup) -> None:
        super().__init__(*groups)
        self.is_grounded = True
        # self._set_gravity(500)
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
        if self.is_grounded and pygame.key.get_pressed()[pygame.key.key_code(" ")]:
            self.__jump()
        # print(self.is_grounded)
        if pygame.key.get_pressed()[pygame.key.key_code("w")]:
            self._translate(Vector2(0, 10 * kwargs["delta_time"]))
        if pygame.key.get_pressed()[pygame.key.key_code("s")]:
            self._translate(Vector2(0, -10 * kwargs["delta_time"]))
        if self.is_grounded:
            if self.is_grounded > 0:
                self._set_gravity(0)
                self._set_velocity(Vector2(self._get_velocity().x, 0))
        else:
            self._set_gravity(10)

    def __jump(self):
        # self.__is
        pass
