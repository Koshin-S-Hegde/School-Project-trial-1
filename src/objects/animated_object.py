import pygame

from src.objects.object import Object


class AnimatedObject(Object):
    __current_sprite_index: float
    __frame_list: list[pygame.Surface]
    __animation_speed: float
    __should_animation_run: bool

    def __init__(self):
        super().__init__()
        self.__current_sprite_index = 0
        self.__frame_list = []
        self.__should_animation_run = False

    def set_first_frame(self, sprite_path: str) -> None:
        self.set_image_surface(pygame.image.load(sprite_path))
        self.__frame_list.append(pygame.image.load(sprite_path))

    def set_custom_frame(self, frame_number: int) -> None:
        self.set_image_surface(self.__frame_list[frame_number])

    def set_frame_per_second(self, speed: float) -> None:
        self.__animation_speed = speed

    def add_animation_sprite(self, sprite_path: str) -> None:
        self.__frame_list.append(pygame.image.load(sprite_path))

    def __animation_loop(self, delta_time: float) -> None:
        if self.__should_animation_run:
            self.__current_sprite_index += self.__animation_speed * delta_time
            if self.__current_sprite_index >= len(self.__frame_list):
                self.__current_sprite_index = 0
            self.set_image_surface(self.__frame_list[int(self.__current_sprite_index)])

    def enable_animation(self) -> None:
        self.__should_animation_run = True

    def disable_animation(self) -> None:
        self.__should_animation_run = False

    def update(self, *args, **kwargs) -> None:
        super(AnimatedObject, self).update(*args, **kwargs)
        self.__animation_loop(kwargs['delta_time'])
