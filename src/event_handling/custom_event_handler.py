import pygame
from singleton_decorator import singleton


@singleton
class EventCreator:
    """WARNING:- Do NOT create events outside this class"""
    __current_highest_event_type: int

    def __init__(self) -> None:
        self.__current_highest_event_type = pygame.USEREVENT - 1

    def create_event(self) -> int:
        """WARNING:- Do NOT use it multiple times for a single event"""
        self.__current_highest_event_type += 1
        return self.__current_highest_event_type
