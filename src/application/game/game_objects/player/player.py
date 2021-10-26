import pygame.key
from pygame import Vector2
from pygame.sprite import AbstractGroup

from src.objects import GravitationalObject
from src.objects.living_object import LivingObject


class Player(LivingObject, GravitationalObject):
    __JUMP_VELOCITY: float
    __is_grounded: bool
    __PLAYER_GRAVITY: float

    def __init__(
            self,
            *groups: AbstractGroup,
            jump_velocity: float,
            gravity: float,
            position: Vector2,
            size: Vector2
    ) -> None:
        super().__init__(health=1, *groups)
        self.__JUMP_VELOCITY = jump_velocity
        self.__PLAYER_GRAVITY = gravity
        self.set_position(position)
        self.set_size(size)
        self.set_image_path("images/square_face_1.png")
        self.is_grounded = True

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
            self.set_gravity(0)
            self.set_velocity(Vector2(self.get_velocity().x, 0))
        else:
            self.set_gravity(self.__PLAYER_GRAVITY)
        if self.is_grounded and pygame.key.get_pressed()[pygame.key.key_code(" ")]:
            self.set_velocity(Vector2(0, -self.__JUMP_VELOCITY))
