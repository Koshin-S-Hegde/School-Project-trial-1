import pygame.key
from pygame import Vector2
from pygame.sprite import AbstractGroup

from src.application.game.game_objects import game_object_handler
from src.application.game.game_objects.obstacle import Obstacle
from src.application_handling import application_events
from src.event_handling import event_handler
from src.game_objects import KineticObject


class Player(KineticObject):
    __velocity: float

    def __init__(self, velocity: float, *groups: AbstractGroup) -> None:
        super().__init__(*groups)

        self.set_size(Vector2(10, 10))
        self.set_position(Vector2(50, 90))
        self.__velocity = velocity

    def update(self, *args, **kwargs) -> None:
        super(Player, self).update(*args, **kwargs)

        x_velocity: float = (
                -self.__velocity * pygame.key.get_pressed()[pygame.key.key_code("a")] +
                self.__velocity * pygame.key.get_pressed()[pygame.key.key_code("d")]
        )

        if self.get_position().x - self.get_size().x / 2 < 0:
            x_velocity = max(0.0, x_velocity)
        elif self.get_position().x + self.get_size().x / 2 > 100:
            x_velocity = min(0.0, x_velocity)

        self.set_velocity(Vector2(x_velocity, 0))

        for obstacle in game_object_handler.get_object_by_type(Obstacle):
            if obstacle.rect.colliderect(self):
                event_handler.post(application_events.PAUSE_GAME)
                event_handler.post(application_events.START_END_MENU)
