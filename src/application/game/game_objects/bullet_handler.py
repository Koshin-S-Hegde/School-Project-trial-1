import pygame.surface
from pygame import Vector2
from pygame.sprite import Group

from src.application.game.game_objects.bullet import Bullet


class BulletHandler:
    __bullet_group: Group
    __TOTAL_SHOOT_COOL_DOWN: float
    __shoot_cool_down_left: float

    def __init__(self) -> None:
        self.__bullet_group = Group()
        self.__TOTAL_SHOOT_COOL_DOWN = 1
        self.__shoot_cool_down_left = 0

    def update(self, delta_time: float, player_position: Vector2) -> None:
        absolute_mouse_position: tuple = pygame.mouse.get_pos()
        mouse_position = Vector2([
            absolute_mouse_position[i] * 100 / pygame.display.get_window_size()[i] for i in range(2)
        ])
        direction: Vector2 = (mouse_position - player_position).normalize()
        if pygame.mouse.get_pressed(3)[0] and self.__shoot_cool_down_left <= 0:
            self.__bullet_group.add(Bullet(direction, player_position))
            self.__shoot_cool_down_left = self.__TOTAL_SHOOT_COOL_DOWN
        self.__shoot_cool_down_left -= delta_time
        self.__bullet_group.update(delta_time=delta_time)

    def render(self) -> None:
        self.__bullet_group.draw(pygame.display.get_surface())
