from dataclasses import dataclass

import pygame
from pygame.sprite import Group
from pygame import Vector2

from src.application.game.game_objects.platform.platform import Platform


@dataclass
class PlatformConfiguration:
    image: str
    size: Vector2
    position: Vector2

    def __init__(
            self,
            image_path: str = "images/obstacle.png",
            size: Vector2 = Vector2(40, 5),
            position: Vector2 = Vector2(50, 90)
    ) -> None:
        self.image = image_path
        self.size = size
        self.position = position


class PlatformHandler:
    __platform_group: Group

    def __init__(self, platform_configuration: PlatformConfiguration) -> None:
        self.__platform_group = Group()
        self.__platform_group.add(Platform(
            image=platform_configuration.image,
            size=platform_configuration.size,
            position=platform_configuration.position
        ))

    def update(self, delta_time: float) -> None:
        self.__platform_group.update(delta_time=delta_time)

    def render(self) -> None:
        self.__platform_group.draw(pygame.display.get_surface())

    @property
    def platform_group(self) -> Group:
        return self.__platform_group
