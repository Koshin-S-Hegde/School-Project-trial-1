import sys
import pygame
from pygame import Vector2, BUTTON_LEFT
from pygame.sprite import Group
from src.application_handling.scenes.scene import Scene
from src.objects import Button
from src.application_handling import application_events
from src.event_handling import event_handler


class PauseMenu(Scene):
    __start_button: Button
    __level_select_button: Button
    __button_group: Group

    def __init__(self) -> None:
        super().__init__()
        self.__start_button_config()
        self.__level_select_button_config()
        self.__button_list = [self.__start_button, self.__level_select_button]
        self.__button_group = Group(self.__button_list)

    def __start_button_config(self) -> None:
        self.__start_button = Button()
        self.__start_button.set_image_path('images/menu_bar_start.png')
        self.__start_button.set_size(Vector2(35, 15))
        self.__start_button.set_position(Vector2(50, 30))

    def __level_select_button_config(self) -> None:
        self.__level_select_button = Button()
        self.__level_select_button.set_image_path('images/menu_bar_level.png')
        self.__level_select_button.set_size(Vector2(35, 15))
        self.__level_select_button.set_position((Vector2(50, 50)))

    def update(self, delta_time: float) -> None:
        self.__button_group.update(delta_time=delta_time)
        if pygame.key.get_pressed()[pygame.key.key_code('K')]:
            event_handler.post(application_events.END_GAME)
            event_handler.post(application_events.START_PAUSE_MENU)
        if self.__start_button.is_pressed(BUTTON_LEFT):
            self.__start_game()
        if self.__level_select_button.is_pressed(BUTTON_LEFT):
            self.__start_level_menu()
        print('pause menu')

    def render(self) -> None:
        self.__button_group.draw(pygame.display.get_surface())

    @staticmethod
    def __start_game() -> None:
        event_handler.post(application_events.START_GAME, level_name="level_1")
        event_handler.post(application_events.STOP_PAUSE_MENU)

    @staticmethod
    def __start_level_menu() -> None:
        event_handler.post(application_events.START_LEVEL_MENU)
        event_handler.post(application_events.STOP_PAUSE_MENU)