import pygame.display
from pygame.sprite import Group

from src.application.game.game_objects.bullet.bullet_handler import BulletHandler
from src.application.game.game_objects.enemy import Enemy
from src.application.game.game_objects.player.player import Player


class EnemyHandler:
    __enemy_group: Group
    __bullet_handler: BulletHandler

    def __init__(self) -> None:
        self.__enemy_group = Group()
        self.__enemy_group.add(Enemy())
        self.__bullet_handler = BulletHandler(1)

    def update(self, delta_time: float, player: Player) -> None:
        self.__enemy_group.update(delta_time=delta_time)
        for enemy in self.enemies:
            self.__bullet_handler.update(delta_time)
            self.__bullet_handler.shoot(enemy.get_position(), player.get_position(), Enemy)

    def render(self) -> None:
        self.__enemy_group.draw(pygame.display.get_surface())
        self.__bullet_handler.render()

    @property
    def enemies(self) -> list[Enemy]:
        return self.__enemy_group.sprites()  # TODO:- Fix this
