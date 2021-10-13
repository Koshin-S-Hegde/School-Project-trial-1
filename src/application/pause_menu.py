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
    __main_menu_button: Button
    __button_group: Group

    def __init__(self) -> None:
        super().__init__()
        self.__start_button_config()
        self.__level_select_button_config()
        self.__main_menu_button_config()
        button_list = [self.__start_button, self.__level_select_button, self.__main_menu_button]
        self.__button_group = Group(button_list)

    def __start_button_config(self) -> None:
        self.__start_button = Button()
        self.__start_button.set_image_path('images/button_images/menu_bar_resume.png')
        self.__start_button.set_size(Vector2(35, 15))
        self.__start_button.set_position(Vector2(50, 30))

    def __level_select_button_config(self) -> None:
        self.__level_select_button = Button()
        self.__level_select_button.set_image_path('images/button_images/menu_bar_level.png')
        self.__level_select_button.set_size(Vector2(35, 15))
        self.__level_select_button.set_position((Vector2(50, 50)))

    def __main_menu_button_config(self) -> None:
        self.__main_menu_button = Button()
        self.__main_menu_button.set_image_path('images/button_images/menu_bar_main_menu.png')
        self.__main_menu_button.set_size(Vector2(35, 15))
        self.__main_menu_button.set_position(Vector2(50, 70))

    def update(self, delta_time: float) -> None:
        self.__button_group.update(delta_time=delta_time)
        if self.__start_button.is_pressed(BUTTON_LEFT):
            self.__resume_game()
        if self.__level_select_button.is_pressed(BUTTON_LEFT):
            self.__start_level_menu()
        if self.__main_menu_button.is_pressed(BUTTON_LEFT):
            self.__start_main_menu()

    def render(self) -> None:
        self.__button_group.draw(pygame.display.get_surface())

    @staticmethod
    def __resume_game() -> None:
        event_handler.post(application_events.RESUME_GAME)
        event_handler.post(application_events.STOP_PAUSE_MENU)

    @staticmethod
    def __start_level_menu() -> None:
        event_handler.post(application_events.START_LEVEL_MENU)
        event_handler.post(application_events.STOP_PAUSE_MENU)

    @staticmethod
    def __start_main_menu() -> None:
        event_handler.post(application_events.END_GAME)
        event_handler.post(application_events.STOP_PAUSE_MENU)
        event_handler.post(application_events.START_MAIN_MENU)
