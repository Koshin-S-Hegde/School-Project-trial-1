import pygame
from pygame.sprite import GroupSingle, Group

from src.application.game.game_objects.bullet.bullet_handler import BulletHandler
from src.application.game.game_objects.player.player import Player


class PlayerHandler:
    __player: Player
    __player_group: GroupSingle
    __bullet_handler: BulletHandler

    def __init__(self) -> None:
        self.__player = Player()
        self.__player_group = GroupSingle(self.__player)
        self.__bullet_handler = BulletHandler(1)

    def update(self, delta_time: float, obstacle_group: Group) -> None:
        self.__player_group.sprite.is_grounded = False
        for obstacle in pygame.sprite.spritecollide(self.__player_group.sprite, obstacle_group, False):
            if self.__player_group.sprite.rect.y < obstacle.rect.y:
                self.__player_group.sprite.is_grounded = True
        self.__player_group.update(delta_time=delta_time)
        mouse_position = pygame.Vector2([
            pygame.mouse.get_pos()[i] * 100 / pygame.display.get_window_size()[i] for i in range(2)
        ])
        self.__bullet_handler.update(delta_time)
        if pygame.mouse.get_pressed(3)[0]:
            self.__bullet_handler.shoot(self.__player.get_position(), mouse_position, Player)

    def render(self) -> None:
        self.__player_group.draw(pygame.display.get_surface())
        self.__bullet_handler.render()

    @property
    def player(self) -> Player:
        return self.__player
