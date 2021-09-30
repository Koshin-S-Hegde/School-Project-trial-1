import pygame

from src.application_handling import application_events
from src.application_handling.scenes.scene import Scene
from src.event_handling import event_handler


class LevelMenu(Scene):
    def __init__(self) -> None:
        super().__init__()
        self._add_to_pause_event_callback(pygame.MOUSEBUTTONDOWN, self.start_game)

    def update(self, delta_time: float) -> None:
        print("Level Menu")

    @staticmethod
    def start_game() -> None:
        event_handler.post(application_events.START_GAME, level_name="level_1")
        event_handler.post(application_events.STOP_LEVEL_MENU)
