import pygame.display
from pygame import Vector2
from pygame.sprite import Group

from src.application.game.game_objects.bullet.bullet_handler import BulletHandler
from src.application.game.game_objects.enemy.enemy import Enemy
from src.application.game.game_objects.player.player import Player


class EnemyHandler:
    __enemy_group: Group
    __bullet_handler: BulletHandler

    def __init__(self) -> None:
        self.__enemy_group = Group()
        self.__enemy_group.add(Enemy(
            health=10,
            position=Vector2(10, 10),
            size=Vector2(10, 10),
            image_path="images/default_object.png"
        ))
        self.__bullet_handler = BulletHandler(1)

    def update(self, delta_time: float, player: Player, player_bullet_group: Group) -> None:
        self.__enemy_group.update(delta_time=delta_time)
        for enemy in self.enemies:
            for bullet in pygame.sprite.spritecollide(enemy, player_bullet_group, True):
                enemy.do_damage(bullet.damage)  # TODO:- Fix this
            self.__bullet_handler.shoot(enemy.get_position(), player.get_position(), damage=0.1)
        self.__bullet_handler.update(delta_time)

    def render(self) -> None:
        self.__enemy_group.draw(pygame.display.get_surface())
        self.__bullet_handler.render()

    @property
    def enemies(self) -> list[Enemy]:
        return self.__enemy_group.sprites()  # TODO:- Fix this

    @property
    def bullet_group(self) -> Group:
        return self.__bullet_handler.bullet_group
