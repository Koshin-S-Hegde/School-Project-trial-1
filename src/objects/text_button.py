from collections import defaultdict

import pygame.mouse
from pygame import Vector2
from pygame.sprite import AbstractGroup

from src.event_handling import event_handler
from src.objects.button import Button
from src.objects.text import Text


class TextButton(Text, Button):
    __mouse_is_down: defaultdict[int, bool]

    def __init__(
            self, *groups: AbstractGroup,
            back_ground_color: tuple[int, int, int],
            text_color: tuple[int, int, int],
            size: Vector2, position: Vector2,
            text: str,
            quality: int = 200
    ):
        super().__init__(
            *groups,
            back_ground_color=back_ground_color,
            text_color=text_color,
            size=size, position=position, text=text,
            quality=quality
        )
        self.__mouse_is_down = defaultdict(lambda: False)

        event_handler.subscribe(pygame.MOUSEBUTTONDOWN, self.__mouse_button_down_callback)
        event_handler.subscribe(pygame.MOUSEBUTTONUP, self.__mouse_button_up_callback)

    def is_pressed(self, mouse_button: int) -> bool:
        return (
                self.__mouse_is_down[mouse_button] and
                self.rect.collidepoint(pygame.mouse.get_pos())
        )

    def __mouse_button_down_callback(self, event: pygame.event.Event) -> None:
        self.__mouse_is_down[event.button] = True

    def __mouse_button_up_callback(self, event):
        self.__mouse_is_down[event.button] = False
