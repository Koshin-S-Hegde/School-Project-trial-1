import time

from src.application_handling.scenes.scene import Scene


class SceneGroup:
    __scenes: list[Scene]
    __last_time_update_was_called: float

    def __init__(self) -> None:
        self.__scenes = list()
        self.__last_time_update_was_called = time.time()

    def update(self) -> None:
        """Updates all scenes in the group that are not paused"""
        delta_time: float = self.__last_time_update_was_called - time.time()
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
