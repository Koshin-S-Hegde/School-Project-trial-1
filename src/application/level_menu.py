import pygame
from pygame import Vector2
from pygame.sprite import Group

from src.application_handling import application_events
from src.application_handling.scenes.scene import Scene
from src.event_handling import event_handler
from src.objects import Button


class LevelMenu(Scene):
    __level_button: Button
    __button_group: Group

    def __init__(self) -> None:
        super().__init__()
        self.__level_button = Button()
        self.__level_button.set_image_path('images/button_images/menu_bar_level_one.png')
        self.__level_button.set_size(Vector2(35, 15))
        self.__level_button.set_position(Vector2(50, 50))
        self.__button_group = Group(self.__level_button)

    def update(self, delta_time: float) -> None:
        self.__button_group.update(delta_time=delta_time)
        if self.__level_button.is_pressed(pygame.BUTTON_LEFT):
            self.__start_game()

    @staticmethod
    def __start_game() -> None:
        event_handler.post(application_events.START_GAME, level_name="level_1")
        event_handler.post(application_events.STOP_LEVEL_MENU)

    def render(self) -> None:
        self.__button_group.draw(pygame.display.get_surface())
