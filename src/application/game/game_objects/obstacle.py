import random

from pygame import Vector2
from pygame.sprite import AbstractGroup

from src.game_objects import GravitationalObject


class Obstacle(GravitationalObject):
    def __init__(
            self,
            velocity: float,
            initial_y_position: float,
            *groups: AbstractGroup
    ) -> None:

        super().__init__(*groups)

        self.set_image_path("images/obstacle.png")
        self.set_size(Vector2(30, 5))
        self.set_velocity(Vector2(0, velocity))
        self.set_position(Vector2(self.generate_x_position(), -100 + initial_y_position))

    def generate_x_position(self) -> float:
        return random.randrange(
            int(self.get_size().x // 2),
            100 - int(self.get_size().x // 2)
        )

    def update(self, *args, **kwargs) -> None:
        super(Obstacle, self).update(*args, **kwargs)

        if self.get_position().y > 100 + self.get_size().y / 2:
            self.set_position(Vector2(self.generate_x_position(), 0 - self.get_size().y / 2))
