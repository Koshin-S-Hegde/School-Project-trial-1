from pygame.math import Vector2
from pygame.sprite import AbstractGroup

from src.objects import Object


class Platform(Object):
    def __init__(
            self,
            image: str,
            size: Vector2,
            position: Vector2,
            *groups: AbstractGroup
    ) -> None:
        super().__init__(*groups)
        self.set_image_path(image)
        self.set_size(size)
        self.set_position(position)
