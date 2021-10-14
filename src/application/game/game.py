import pygame.event
from pygame.sprite import Group

from src.application.game.game_objects.enemy.enemy_handler import EnemyHandler
from src.application.game.game_objects.obstacle import Obstacle
from src.application.game.game_objects.player.player_handler import PlayerHandler
from src.application_handling.scenes.scene import Scene
from src.event_handling import event_handler
from src.application_handling import application_events


class Game(Scene):
    __obstacle_group: Group
    __enemy_handler: EnemyHandler
    __player_handler: PlayerHandler

    def __init__(self, event: pygame.event.Event = None) -> None:
        super().__init__()
        self.__load_game_objects()

    def __load_game_objects(self) -> None:
        self.__player_handler = PlayerHandler()
        self.__obstacle_group = Group()
        self.__obstacle_group.add(Obstacle())
        self.__enemy_handler = EnemyHandler()

    def update(self, delta_time: float) -> None:
        super(Game, self).update(delta_time=delta_time)
        self.__player_handler.update(delta_time, self.__obstacle_group, self.__enemy_handler.bullet_group)
        self.__enemy_handler.update(delta_time, self.__player_handler.player, self.__player_handler.bullet_group)
        self.__obstacle_group.update(delta_time=delta_time)
        pygame.sprite.groupcollide(self.__obstacle_group, self.__player_handler.bullet_group, False, True)
        pygame.sprite.groupcollide(self.__obstacle_group, self.__enemy_handler.bullet_group, False, True)
        # pause menu
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.__start_pause_menu()

    def render(self) -> None:
        super(Game, self).render()
        self.__enemy_handler.render()
        self.__player_handler.render()
        self.__obstacle_group.draw(pygame.display.get_surface())

    @staticmethod
    def __start_pause_menu():
        event_handler.post(application_events.PAUSE_GAME)
        event_handler.post(application_events.START_PAUSE_MENU)
