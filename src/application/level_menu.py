import pygame
from pygame import Vector2
from pygame.sprite import Group, GroupSingle

from src.application_handling import application_events
from src.application_handling.scenes.scene import Scene
from src.objects import Object
from src.objects.event_integrated_button import EventIntegratedButton


class LevelMenu(Scene):
    __button_group: Group
    __background: Object
    __background_group: GroupSingle

    def __init__(self) -> None:
        super().__init__()
        # groups
        self.__button_group = Group()
        # background configs
        self.__primary_background_config()
        # button configs
        self.__level_button_config()

    def __primary_background_config(self) -> None:
        background = Object()
        background.set_image_path('images/background_images/transparent_background_set/tra-3.png')
        background.set_size(Vector2(100, 100))
        background.set_position(Vector2(50, 50))
        self.__background_group = GroupSingle(background)

    def __level_button_config(self) -> None:
        level_button = EventIntegratedButton()
        level_button.set_default_image_path('images/button_images/level_1.png')
        level_button.set_hover_image_path('images/button_images/level_2.png')
        level_button.add_click_event(application_events.START_GAME, level_name="level_1")
        level_button.add_click_event(application_events.STOP_LEVEL_MENU)
        level_button.set_size(Vector2(23, 8))
        level_button.set_position(Vector2(50, 50))
        self.__button_group.add(level_button)

    def update(self, delta_time: float) -> None:
        self.__background_group.update(delta_time=delta_time)
        self.__button_group.update(delta_time=delta_time)

    def render(self) -> None:
        self.__background_group.draw(pygame.display.get_surface())
        self.__button_group.draw(pygame.display.get_surface())
