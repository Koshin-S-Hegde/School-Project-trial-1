import pygame.event

from src.application.game.game_objects.platform.platform_handler import PlatformHandler
from src.application.game.game_objects.enemy.enemy_handler import EnemyHandler
from src.application.game.game_objects.player.player_handler import PlayerHandler
from src.application_handling import application_events
from src.application_handling.scenes.scene import Scene
from src.event_handling import event_handler


class Game(Scene):
    __platform_handler: PlatformHandler
    __enemy_handler: EnemyHandler
    __player_handler: PlayerHandler

    def restart(self, event: pygame.event.Event = None) -> None:
        super().restart()
        self.__load_game_objects()

    def __load_game_objects(self) -> None:
        self.__player_handler = PlayerHandler()
        self.__platform_handler = PlatformHandler()
        self.__enemy_handler = EnemyHandler()

    def update(self, delta_time: float) -> None:
        super(Game, self).update(delta_time=delta_time)
        self.__player_handler.update(
            delta_time,
            self.__platform_handler.platform_group,
            self.__enemy_handler.bullet_group
        )
        self.__enemy_handler.update(delta_time, self.__player_handler.player, self.__player_handler.bullet_group)
        self.__platform_handler.update(delta_time)
        pygame.sprite.groupcollide(self.__platform_handler.platform_group, self.__player_handler.bullet_group, False,
                                   True)
        pygame.sprite.groupcollide(self.__platform_handler.platform_group, self.__enemy_handler.bullet_group, False,
                                   True)
        # pause menu
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.__start_pause_menu()

    def render(self) -> None:
        super(Game, self).render()
        self.__enemy_handler.render()
        self.__player_handler.render()
        self.__platform_handler.render()

    @staticmethod
    def __start_pause_menu():
        event_handler.post(application_events.PAUSE_GAME)
        event_handler.post(application_events.START_PAUSE_MENU)
