import pygame
from pygame.sprite import Group

from application.game.game_objects.platform.platform import Platform


class PlatformHandler:
    __platform_group: Group

    def __init__(self) -> None:
        self.__platform_group = Group()
        self.__platform_group.add(Platform())

    def update(self, delta_time: float) -> None:
        self.__platform_group.update(delta_time=delta_time)

    def render(self) -> None:
        self.__platform_group.draw(pygame.display.get_surface())

    @property
    def platform_group(self) -> Group:
        return self.__platform_group
