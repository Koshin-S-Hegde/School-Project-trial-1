import pygame
from pygame import Vector2
from pygame.sprite import Group, GroupSingle

from src.application_handling import application_events
from src.application_handling.scenes.scene import Scene
from src.objects import Object
from src.objects.animated_object import AnimatedObject
from src.objects.event_integrated_button import EventIntegratedButton


class MainMenu(Scene):
    __secondary_background: Object
    __primary_background: Object
    __third_background: AnimatedObject
    __third_background_size: int
    __third_background_animation_started: bool
    __button_group: Group
    __secondary_background_group: Group
    __primary_background_group: GroupSingle
    __third_background_group: GroupSingle

    def restart(self) -> None:
        super().restart()
        # groups
        self.__button_group = Group()
        self.__secondary_background_group = Group()
        # variables
        self.__third_background_size = 10
        self.__third_background_animation_started = False
        # backgrounds
        self.__third_background_config()
        self.__primary_background_config()
        self.__secondary_background_config()
        # button configs
        self.__start_button_config()
        self.__quit_button_config()
        self.__credit_button_config()
        self.__license_button_config()
        # music
        self.__main_menu_music_config()

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

    def __third_background_config(self) -> None:
        self.__third_background = AnimatedObject()
        image_path = 'images/background_images/transparent_background_set/tra-'

        for i in range(1, self.__third_background_size + 1):
            self.__third_background.add_animation_sprite(f'{image_path}{i}.png')

        self.__third_background.set_frame_per_second(5)
        self.__third_background.set_size(Vector2(100, 100))
        self.__third_background.set_position(Vector2(50, 50))
        self.__third_background.enable_animation()
        self.__third_background.set_current_frame(0)
        self.__third_background_group = GroupSingle(self.__third_background)

    def __start_button_config(self) -> None:
        start_button = EventIntegratedButton()
        start_button.set_default_image_path('images/button_images/start_1.png')
        start_button.set_hover_image_path('images/button_images/start_2.png')
        start_button.add_click_event(application_events.STOP_MAIN_MENU)
        start_button.add_click_event(application_events.START_GAME, level_name="level_1")
        start_button.set_size(Vector2(21, 8))
        start_button.set_position(Vector2(50, 50))
        self.__button_group.add(start_button)

    def __quit_button_config(self) -> None:
        quit_button = EventIntegratedButton()
        quit_button.set_default_image_path('images/button_images/exit_1.png')
        quit_button.set_hover_image_path('images/button_images/exit_2.png')
        quit_button.add_click_event(pygame.QUIT)
        quit_button.set_size(Vector2(21, 8))
        quit_button.set_position(Vector2(50, 60))
        self.__button_group.add(quit_button)

    def __credit_button_config(self) -> None:
        credit_button = EventIntegratedButton()
        credit_button.set_default_image_path('images/button_images/credit_1.png')
        credit_button.set_hover_image_path('images/button_images/credit_2.png')
        credit_button.add_click_event(application_events.STOP_MAIN_MENU)
        credit_button.add_click_event(application_events.START_CREDIT_MENU)
        credit_button.set_size(Vector2(4, 7))
        credit_button.set_position(Vector2(88, 95))
        self.__button_group.add(credit_button)

    def __license_button_config(self) -> None:
        license_button = EventIntegratedButton()
        license_button.set_default_image_path('images/button_images/license_1.png')
        license_button.set_hover_image_path('images/button_images/license_2.png')
        license_button.add_click_event(application_events.STOP_MAIN_MENU)
        license_button.add_click_event(application_events.START_LICENSE_MENU)
        license_button.set_size(Vector2(4, 7))
        license_button.set_position(Vector2(94, 95))
        self.__button_group.add(license_button)

    @staticmethod
    def __main_menu_music_config():
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('music/alexander-nakarada-dungeons-and-dragons.mp3'), -1)
        pygame.mixer.Channel(0).set_volume(0.8)

    def update(self, delta_time: float) -> None:
        self.__primary_background_group.update(delta_time=delta_time)
        self.__secondary_background_group.update(delta_time=delta_time)
        self.__third_background_group.update(delta_time=delta_time)

        if self.__third_background_animation_started and self.__third_background_size == self.__third_background.get_current_frame() + 1:
            self.__third_background.disable_animation()
        if self.__third_background.get_current_frame() == 1:
            self.__third_background_animation_started = True

        self.__button_group.update(delta_time=delta_time)

    def render(self) -> None:
        self.__primary_background_group.draw(pygame.display.get_surface())
        self.__secondary_background_group.draw(pygame.display.get_surface())
        self.__button_group.draw(pygame.display.get_surface())
        self.__third_background_group.draw(pygame.display.get_surface())
