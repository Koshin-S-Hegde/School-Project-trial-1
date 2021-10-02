from typing import Callable, Any, Union
import pygame.event
from singleton_decorator import singleton


@singleton
class EventHandler:
    """
    This class handles ALL the pygame events.\n
    WARNING:- Do NOT handle events outside of this class.
    """

    supported_callback_events: type = Union[Callable[[], Any], Callable[[pygame.event.Event], Any]]
    __event_callbacks: dict[int, set[supported_callback_events]]

    def __init__(self) -> None:
        self.__event_callbacks = dict()

    def post(self, event_type: int, **kwargs) -> None:
        """Emits a new event."""
        pygame.event.post(pygame.event.Event(event_type, **kwargs))
        self.update()

    def subscribe(self, event_type: int, callback: supported_callback_events) -> None:
        """
        Usage:- add_event_callback(event type, the name of the function)\n
        Incorrect:- add_event_callback(23, my_function())\n
        Correct:- add_event_callback(23, my_function)
        """

        self.__event_callbacks.setdefault(event_type, set())
        self.__event_callbacks[event_type].add(callback)

    def unsubscribe(self, event_type: int, callback: supported_callback_events) -> None:
        """Removes the callback from the event list\n
        Usage is same as add_event_callback"""

        try:
            self.__event_callbacks[event_type].remove(callback)
        except (ValueError, KeyError):
            print(f"WARNING:- {callback.__name__} not found for event type {event_type}")

    def update(self) -> None:
        for required_event in self.__event_callbacks.keys():
            for posted_event in pygame.event.get(required_event):
                for callback in self.__event_callbacks[posted_event.type].copy():
                    try:
                        callback(posted_event)
                    except TypeError:
                        callback()
