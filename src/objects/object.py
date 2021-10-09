import pygame.image
from pygame import Vector2
from pygame.sprite import AbstractGroup
from pygame.sprite import Sprite

from src.event_handling import event_handler


class Object(Sprite):
    __original_image: pygame.Surface
    __size_percentage: Vector2
    __position_percentage: Vector2

    def __init__(self, *groups: AbstractGroup):
        super().__init__(*groups)
        self.set_image_path("images/default_object.png")
        event_handler.subscribe(pygame.VIDEORESIZE, self.__window_resize_event_callback)

    # Image manipulation
    def set_image_surface(self, surface: pygame.Surface) -> None:
        self.__original_image = surface.convert_alpha()
        self.__update_image_size()

    def set_image_path(self, image_path: str) -> None:
        self.set_image_surface(pygame.image.load(image_path))

    #  Size manipulation
    def set_size(self, size: Vector2) -> None:
        self.__size_percentage = size
        self.__update_image_size()

    def get_size(self) -> Vector2:
        try:
            return self.__size_percentage
        except AttributeError:
            return Vector2(50, 50)  # Default size

    def __update_image_size(self) -> None:
        absolute_size = list(self.__get_absolute_size())
        self.image = pygame.transform.scale(self.__original_image, absolute_size)
        self.rect = self.image.get_rect()
        self.__update_position()

    def __get_absolute_size(self) -> list[int]:
        window_size: Vector2 = Vector2(pygame.display.get_surface().get_size())
        return [
            int(window_size[i] * self.get_size()[i] // 100) for i in range(2)
        ]

    # Position manipulation
    def set_position(self, position: Vector2) -> None:
        self.__position_percentage = position
        self.rect.center = self.__get_absolute_position()

    def get_position(self) -> Vector2:
        try:
            return self.__position_percentage
        except AttributeError:
            return Vector2(50, 50)  # Default position

    def __update_position(self) -> None:
        self.set_position(self.get_position())

    def __get_absolute_position(self) -> Vector2:
        window_size: Vector2 = Vector2(pygame.display.get_surface().get_size())
        return Vector2([
            window_size[i] * self.get_position()[i] for i in range(2)
        ]) // 100

    def __window_resize_event_callback(self) -> None:
        self.__update_image_size()
        self.__update_position()

    def update(self, *args, **kwargs) -> None:
        super(Object, self).update(*args, **kwargs)
        if "delta_time" not in kwargs:
            raise TypeError("delta_time key argument was not passed.")
