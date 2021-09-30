import pygame.event
from pygame.sprite import GroupSingle, Group

from src.application.game.game_objects.obstacle import Obstacle
from src.application.game.game_objects.player import Player
from src.application_handling.scenes.scene import Scene


class Game(Scene):
    __player: Player
    __player_group: GroupSingle
    __obstacle_group: Group

    def __init__(self, event: pygame.event.Event = None) -> None:
        super().__init__()
        self.__load_game_objects()

    def __load_game_objects(self) -> None:
        self.__player = Player()
        self.__player_group = GroupSingle(self.__player)
        self.__obstacle_group = Group()
        self.__obstacle_group.add(Obstacle())

    def update(self, delta_time: float) -> None:
        super(Game, self).update(delta_time=delta_time)
        print("Game")
        self.__player.is_grounded = False
        for obstacle in pygame.sprite.spritecollide(self.__player, self.__obstacle_group, False):
            if self.__player.rect.y < obstacle.rect.y:
                self.__player.is_grounded = True
        self.__player_group.update(delta_time=delta_time)
        self.__obstacle_group.update(delta_time=delta_time)

    def render(self) -> None:
        super(Game, self).render()
        self.__player_group.draw(pygame.display.get_surface())
        self.__obstacle_group.draw(pygame.display.get_surface())
