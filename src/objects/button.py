from collections import defaultdict

import pygame
from pygame.sprite import AbstractGroup

from src.event_handling import event_handler
from src.objects.object import Object


class Button(Object):
    __mouse_is_down: defaultdict[int, bool]

    def __init__(self, *groups: AbstractGroup):
        super().__init__(*groups)
        self.__mouse_is_down = defaultdict(lambda: False)

        event_handler.subscribe(pygame.MOUSEBUTTONDOWN, self.__mouse_button_down_callback)
        event_handler.subscribe(pygame.MOUSEBUTTONUP, self.__mouse_button_up_callback)

    def is_pressed(self, mouse_button: int) -> bool:
        return (
                self.__mouse_is_down[mouse_button] and
                self.is_hovering()
        )

    def is_hovering(self) -> bool:
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def __mouse_button_down_callback(self, event: pygame.event.Event) -> None:
        self.__mouse_is_down[event.button] = True

    def __mouse_button_up_callback(self, event):
        self.__mouse_is_down[event.button] = False
