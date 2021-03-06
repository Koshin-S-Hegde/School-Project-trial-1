import pygame
from pygame import Vector2
from pygame.sprite import Group, GroupSingle
from src.application_handling.scenes.scene import Scene
from src.game_objects import GameObject
from src.application_handling import application_events
from src.game_objects.event_integrated_button import EventIntegratedButton


class EndMenu(Scene):
    __primary_background: GameObject
    __secondary_background: GameObject
    # groups
    __secondary_background_group: GroupSingle
    __button_group: Group
    __primary_background_group: GroupSingle

    def restart(self):
        super().restart()
        self.__button_group = Group()
        # background configs
        self.__primary_background_config()
        self.__secondary_background_config()
        # button configs
        self.__retry_button_config()
        self.__main_menu_button_config()

    def __primary_background_config(self) -> None:
        primary_background = GameObject()
        primary_background.set_image_path('images/background_images/transparent_background_set/tra-3.png')
        primary_background.set_size(Vector2(100, 100))
        primary_background.set_position(Vector2(50, 50))
        self.__primary_background_group = GroupSingle(primary_background)

    def __secondary_background_config(self) -> None:
        secondary_background = GameObject()
        secondary_background.set_image_path('images/background_images/try_again.png')
        secondary_background.set_size(Vector2(100, 100))
        secondary_background.set_position(Vector2(51, 56))
        self.__secondary_background_group = GroupSingle(secondary_background)

    def __retry_button_config(self) -> None:
        resume_button = EventIntegratedButton()
        resume_button.set_default_image_path('images/button_images/retry_1.png')
        resume_button.set_hover_image_path('images/button_images/retry_2.png')
        resume_button.add_click_event(application_events.STOP_END_MENU)
        resume_button.add_click_event(application_events.START_GAME)
        resume_button.set_size(Vector2(21, 8))
        resume_button.set_position(Vector2(50, 45))
        self.__button_group.add(resume_button)

    def __main_menu_button_config(self) -> None:
        main_menu_button = EventIntegratedButton()
        main_menu_button.set_default_image_path('images/button_images/main_menu_1.png')
        main_menu_button.set_hover_image_path('images/button_images/main_menu_2.png')
        main_menu_button.add_click_event(application_events.STOP_GAME)
        main_menu_button.add_click_event(application_events.STOP_END_MENU)
        main_menu_button.add_click_event(application_events.START_MAIN_MENU)
        main_menu_button.set_size(Vector2(21, 8))
        main_menu_button.set_position(Vector2(50, 60))
        self.__button_group.add(main_menu_button)

    def update(self, delta_time: float) -> None:
        self.__primary_background_group.update(delta_time=delta_time)
        self.__secondary_background_group.update(delta_time=delta_time)
        self.__button_group.update(delta_time=delta_time)

    def render(self) -> None:
        self.__primary_background_group.draw(pygame.display.get_surface())
        self.__secondary_background_group.draw(pygame.display.get_surface())
        self.__button_group.draw(pygame.display.get_surface())
