import pygame
from pygame import Vector2
from pygame.sprite import Group

from src.application_handling import application_events
from src.application_handling.scenes.scene import Scene
from src.event_handling import event_handler
from src.objects import Button
from src.objects.event_integrated_button import EventIntegratedButton


class MainMenu(Scene):
    __start_button: EventIntegratedButton
    __level_select_button: Button
    __quit_button: Button
    __button_group: Group

    def __init__(self) -> None:
        super().__init__()
        self.__start_button_config()
        self.__level_select_button_config()
        self.__quit_button_config()
        self.__button_list = [self.__start_button, self.__level_select_button, self.__quit_button]
        self.__button_group = Group(self.__button_list)

    def __start_button_config(self) -> None:
        self.__start_button = EventIntegratedButton()
        self.__start_button.set_default_image_path('images/button_images/start_1.png')
        self.__start_button.set_hover_image_path('images/button_images/start_2.png')
        self.__start_button.add_click_event(application_events.STOP_MAIN_MENU)
        self.__start_button.add_click_event(application_events.START_GAME, level_name="level_1")
        self.__start_button.set_size(Vector2(35, 15))
        self.__start_button.set_position(Vector2(50, 30))

    def __level_select_button_config(self) -> None:
        self.__level_select_button = Button()
        self.__level_select_button.set_image_path('images/button_images/level_1.png')
        self.__level_select_button.set_size(Vector2(35, 15))
        self.__level_select_button.set_position((Vector2(50, 50)))

    def __quit_button_config(self) -> None:
        self.__quit_button = Button()
        self.__quit_button.set_image_path('images/button_images/exit_1.png')
        self.__quit_button.set_size(Vector2(35, 15))
        self.__quit_button.set_position(Vector2(50, 70))

    def update(self, delta_time: float) -> None:
        self.__button_group.update(delta_time=delta_time)

    @staticmethod
    def __start_level_menu() -> None:
        event_handler.post(application_events.START_LEVEL_MENU)
        event_handler.post(application_events.STOP_MAIN_MENU)

    def render(self) -> None:
        self.__button_group.draw(pygame.display.get_surface())
