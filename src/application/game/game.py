import pygame.event

from src.application_handling import application_events
from src.application_handling.scenes.scene import Scene
from src.event_handling import event_handler


class Game(Scene):
    def restart(self, event: pygame.event.Event = None) -> None:
        super().restart()
        self.__load_game_objects()

    def __load_game_objects(self) -> None:
        pass

    def update(self, delta_time: float) -> None:
        super(Game, self).update(delta_time=delta_time)
        # pause menu
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.__start_pause_menu()

    def render(self) -> None:
        super(Game, self).render()

    @staticmethod
    def __start_pause_menu():
        event_handler.post(application_events.PAUSE_GAME)
        event_handler.post(application_events.START_PAUSE_MENU)
