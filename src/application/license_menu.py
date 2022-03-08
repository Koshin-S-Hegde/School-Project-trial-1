import pygame
from pygame import Vector2
from pygame.sprite import Group, GroupSingle
from src.application_handling.scenes.scene import Scene
from src.objects import Object
from src.application_handling import application_events
from src.objects.event_integrated_button import EventIntegratedButton


class LicenseMenu(Scene):
    __primary_background: Object
    __button_group: Group
    __primary_background_group: GroupSingle

    def restart(self) -> None:
        super().restart()
        # backgrounds
        self.__primary_background_config()
        # buttons
        self.__button_group = Group()
        self.__back_button_config()

    def __primary_background_config(self) -> None:
        primary_background = Object()
        primary_background.set_image_path('images/background_images/moss_forest.png')
        primary_background.set_size(Vector2(100, 100))
        primary_background.set_position(Vector2(50, 50))
        self.__primary_background_group = GroupSingle(primary_background)

    def __back_button_config(self) -> None:
        back_button = EventIntegratedButton()
        back_button.set_default_image_path('images/button_images/back_arrow1.png')
        back_button.set_hover_image_path('images/button_images/back_arrow2.png')
        back_button.add_click_event(application_events.STOP_LICENSE_MENU)
        back_button.add_click_event(application_events.START_MAIN_MENU)
        back_button.set_size(Vector2(3, 6))
        back_button.set_position(Vector2(3, 6))
        self.__button_group.add(back_button)

    def update(self, delta_time: float) -> None:
        self.__primary_background_group.update(delta_time=delta_time)
        self.__button_group.update(delta_time=delta_time)

    def render(self) -> None:
        self.__primary_background_group.draw(pygame.display.get_surface())
        self.__button_group.draw(pygame.display.get_surface())

