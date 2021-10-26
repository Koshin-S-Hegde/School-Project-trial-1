from pygame import Vector2
from pygame.sprite import AbstractGroup

from src.objects import Object
from src.objects.living_object import LivingObject


class Enemy(LivingObject, Object):
    def __init__(
            self,
            health: float,
            size: Vector2,
            position: Vector2,
            image_path: str,
            *groups: AbstractGroup
    ) -> None:
        super().__init__(health, *groups)
        self.set_size(size)
        self.set_image_path(image_path)
        self.set_position(position)
