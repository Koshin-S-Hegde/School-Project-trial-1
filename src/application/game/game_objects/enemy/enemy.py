from pygame import Vector2
from pygame.sprite import AbstractGroup

from src.objects import Object
from src.objects.living_object import LivingObject


class Enemy(LivingObject, Object):
    def __init__(self, *groups: AbstractGroup) -> None:
        super().__init__(10, *groups)
        self.set_size(Vector2(10, 10))
        self.set_position(Vector2(10, 10))
