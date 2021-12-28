import pygame
from pygame import Vector2
from pygame.sprite import Group, GroupSingle

from src.application_handling import application_events
from src.application_handling.scenes.scene import Scene
from src.objects import Object
from src.objects.event_integrated_button import EventIntegratedButton


class MainMenu(Scene):
    __secondary_background: Object
    __primary_background: Object
    __button_group: Group
    __secondary_background_group: Group
    __primary_background_group: GroupSingle

    def restart(self) -> None:
        super().restart()
        # groups
        self.__button_group = Group()
        self.__secondary_background_group = Group()
        # backgrounds
        self.__primary_background_config()
        self.__secondary_background_config()
        # button configs
        self.__start_button_config()
        self.__level_select_button_config()
        self.__quit_button_config()
        self.__credit_button_config()
        self.__license_button_config()

    def __primary_background_config(self) -> None:
        primary_background = Object()
        primary_background.set_image_path('images/background_images/moss_forest.png')
        primary_background.set_size(Vector2(100, 100))
        primary_background.set_position(Vector2(50, 50))
        self.__primary_background_group = GroupSingle(primary_background)

    def __secondary_background_config(self) -> None:
        secondary_background = Object()
        secondary_background.set_image_path('images/background_images/rencar_background9.png')
        secondary_background.set_size(Vector2(100, 100))
        secondary_background.set_position(Vector2(51, 50))
        self.__secondary_background_group = Group(secondary_background)

    def __start_button_config(self) -> None:
        start_button = EventIntegratedButton()
        start_button.set_default_image_path('images/button_images/start_1.png')
        start_button.set_hover_image_path('images/button_images/start_2.png')
        start_button.add_click_event(application_events.STOP_MAIN_MENU)
        start_button.add_click_event(application_events.START_GAME, level_name="level_1")
        start_button.set_size(Vector2(21, 8))
        start_button.set_position(Vector2(50, 50))
        self.__button_group.add(start_button)

    def __level_select_button_config(self) -> None:
        level_select_button = EventIntegratedButton()
        level_select_button.set_default_image_path('images/button_images/level_1.png')
        level_select_button.set_hover_image_path('images/button_images/level_2.png')
        level_select_button.add_click_event(application_events.STOP_MAIN_MENU)
        level_select_button.add_click_event(application_events.START_LEVEL_MENU)
        level_select_button.set_size(Vector2(21, 8))
        level_select_button.set_position((Vector2(50, 60)))
        self.__button_group.add(level_select_button)

    def __quit_button_config(self) -> None:
        quit_button = EventIntegratedButton()
        quit_button.set_default_image_path('images/button_images/exit_1.png')
        quit_button.set_hover_image_path('images/button_images/exit_2.png')
        quit_button.add_click_event(pygame.QUIT)
        quit_button.set_size(Vector2(21, 8))
        quit_button.set_position(Vector2(50, 70))
        self.__button_group.add(quit_button)

    def __credit_button_config(self) -> None:
        credit_button = EventIntegratedButton()
        credit_button.set_default_image_path('images/button_images/credit_1.png')
        credit_button.set_hover_image_path('images/button_images/credit_2.png')
        credit_button.set_size(Vector2(4, 7))
        credit_button.set_position(Vector2(88, 95))
        self.__button_group.add(credit_button)

    def __license_button_config(self) -> None:
        license_button = EventIntegratedButton()
        license_button.set_default_image_path('images/button_images/license_1.png')
        license_button.set_hover_image_path('images/button_images/license_2.png')
        license_button.set_size(Vector2(4, 7))
        license_button.set_position(Vector2(94, 95))
        self.__button_group.add(license_button)

    def update(self, delta_time: float) -> None:
        self.__primary_background_group.update(delta_time=delta_time)
        self.__secondary_background_group.update(delta_time=delta_time)
        self.__button_group.update(delta_time=delta_time)

    def render(self) -> None:
        self.__primary_background_group.draw(pygame.display.get_surface())
        self.__secondary_background_group.draw(pygame.display.get_surface())
        self.__button_group.draw(pygame.display.get_surface())
