import pygame.mixer

from src import event_handling


class Scene:
    __is_paused: bool
    __is_disabled: bool
    __to_pause_events: dict[int, set[event_handling.supported_event_formats]]
    __to_disable_events: dict[int, set[event_handling.supported_event_formats]]

    def __init__(self) -> None:
        self.__is_paused = True
        self.__is_disabled = True
        self.__to_pause_events = dict()
        self.__to_disable_events = dict()

    def update(self, delta_time: float) -> None:
        """This is called every single frame.\n
        Inherit this method to do stuff every frame."""

    def render(self) -> None:
        """This is called every single frame.\n
        Inherit this method to render objects to the screen"""

    def pause(self) -> None:
        """This function is to be called whenever the scene has to pause."""
        self.__is_paused = True
        for event_type in self.__to_pause_events:
            for callback in self.__to_pause_events[event_type]:
                event_handling.event_handler.unsubscribe(event_type, callback)

    def resume(self) -> None:
        """This function is to be called whenever the scene has to resume."""
        self.__is_paused = False
        for event_type in self.__to_pause_events:
            for callback in self.__to_pause_events[event_type]:
                event_handling.event_handler.subscribe(event_type, callback)

    def disable(self) -> None:
        self.pause()
        self.__is_disabled = True
        for event_type in self.__to_disable_events:
            for callback in self.__to_disable_events[event_type]:
                event_handling.event_handler.unsubscribe(event_type, callback)

    def enable(self) -> None:
        self.pause()
        self.__is_disabled = False
        for event_type in self.__to_disable_events:
            for callback in self.__to_disable_events[event_type]:
                event_handling.event_handler.subscribe(event_type, callback)

    @property
    def is_paused(self) -> bool:
        return self.__is_paused

    @property
    def is_disabled(self) -> bool:
        return self.__is_disabled

    def restart(self) -> None:
        self.__is_paused = False
        self.__is_disabled = False
        """Restart the Scene"""

    def _add_to_pause_event_callback(self, event_type: int, callback: event_handling.supported_event_formats) -> None:
        self.__to_pause_events.setdefault(event_type, set())
        self.__to_pause_events[event_type].add(callback)
        event_handling.event_handler.subscribe(event_type, callback)

    def dispose(self) -> None:
        """
        Call this ONLY if you do NOT need any of the changes made to th Scene instance.\n
        If you are inheriting this class, make sure that you delete ALL the objects
        (using del keyword or by just equating it to null)
        """
        self.disable()
        pygame.mixer.stop()
