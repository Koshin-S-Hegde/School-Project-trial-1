import pygame
from pygame.sprite import AbstractGroup

from src.event_handling import event_handler
from src.objects.animated_button import AnimatedButton


class EventIntegratedButton(AnimatedButton):
    __events_to_be_posted: dict[int, dict[str]]

    def __init__(self, *groups: AbstractGroup) -> None:
        super().__init__(*groups)
        self.__events_to_be_posted = dict()
        self.change_frame(1, "images/default.png")
        self.change_frame(0, "images/default.png")

    def update(self, *args, **kwargs) -> None:
        super(EventIntegratedButton, self).update(*args, **kwargs)

        if self.is_pressed(pygame.BUTTON_LEFT):
            for event in self.__events_to_be_posted:
                event_handler.post(event, **self.__events_to_be_posted[event])

        if self.is_hovering():
            self.set_custom_frame(1)
        else:
            self.set_custom_frame(0)

    def add_click_event(self, event: int, **kwargs) -> None:
        self.__events_to_be_posted[event] = kwargs

    def set_hover_image_path(self, path: str) -> None:
        self.change_frame(1, path)

    def set_default_image_path(self, path: str) -> None:
        self.change_frame(0, path)
