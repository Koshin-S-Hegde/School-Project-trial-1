import time

from src.application_handling.scenes.scene import Scene


class SceneGroup:
    __scenes: list[Scene]
    __last_time_update_was_called: float
    __first_frame_done: bool

    def __init__(self) -> None:
        self.__scenes = list()
        self.__last_time_update_was_called = time.time()
        self.__first_frame_done = False

    def update(self) -> None:
        """Updates all scenes in the group that are not paused"""
        if not self.__first_frame_done:
            self.__last_time_update_was_called = time.time()
            self.__first_frame_done = True
        delta_time: float = (time.time() - self.__last_time_update_was_called) * 10
        for scene in self.__scenes:
            if not scene.is_paused:
                scene.update(delta_time)
        self.__last_time_update_was_called = time.time()

    def render(self) -> None:
        """All the rendering stuff will be handled here"""
        for scene in self.__scenes:
            if not scene.is_disabled:
                scene.render()

    def append(self, scene: Scene) -> None:
        self.__scenes.append(scene)
