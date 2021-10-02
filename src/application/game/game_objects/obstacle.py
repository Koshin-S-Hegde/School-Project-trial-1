from pygame.math import Vector2
from pygame.sprite import AbstractGroup

from src.objects import Object


class Obstacle(Object):
    def __init__(self, *groups: AbstractGroup) -> None:
        super().__init__(*groups)
        self.set_size(Vector2(50, 5))
        self.set_position(Vector2(50, 90))
