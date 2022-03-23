import pygame.event
from pygame import Vector2
from pygame.sprite import GroupSingle, Group

from src.application.game.game_objects import game_object_handler
from src.application.game.game_objects.obstacle import Obstacle
from src.application.game.game_objects.player import Player
from src.application_handling import application_events
from src.application_handling.scenes.scene import Scene
from src.event_handling import event_handler


class Game(Scene):
    __player: Player
    __player_group: GroupSingle

    __obstacle_group: Group

    def restart(self, event: pygame.event.Event = None) -> None:
        super().restart()
        self.__load_game_objects()

    def __load_game_objects(self) -> None:
        self.__player = Player(20)
        self.__player_group = GroupSingle(self.__player)
        game_object_handler.add_game_object(self.__player)

        self.__obstacle_group = Group()
        obstacles: list[Obstacle] = [
            Obstacle(velocity=10, initial_y_position=0),
            Obstacle(velocity=10, initial_y_position=50)
        ]
        for obstacle in obstacles:
            self.__obstacle_group.add(obstacle)
            game_object_handler.add_game_object(obstacle)

    def __update_game_objects(self, delta_time: float) -> None:
        self.__player_group.update(delta_time=delta_time)
        self.__obstacle_group.update(delta_time=delta_time)

    def update(self, delta_time: float) -> None:
        super(Game, self).update(delta_time=delta_time)

        self.__update_game_objects(delta_time)

        # pause menu
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.__start_pause_menu()

    def render(self) -> None:
        super(Game, self).render()
        self.__player_group.draw(pygame.display.get_surface())
        self.__obstacle_group.draw(pygame.display.get_surface())

    @staticmethod
    def __start_pause_menu():
        event_handler.post(application_events.PAUSE_GAME)
        event_handler.post(application_events.START_PAUSE_MENU)
