from typing import Type

from src.application_handling import application_events
from src.application.game.game import Game
from src.application.level_menu import LevelMenu
from src.application.start_menu import StartMenu
from src.application_handling.scenes.scene import Scene
from src.application_handling.scenes.scene_group import SceneGroup
from src.event_handling import event_handler


class ApplicationHandler:
    __start_menu: StartMenu
    __level_menu: LevelMenu
    __game: Game
    __pause_menu: Scene
    __end_menu: Scene
    __scene_group: SceneGroup

    def __init__(self) -> None:
        self.__scene_group = SceneGroup()
        self.__init_scenes()
        self.__init_callbacks()

    def __init_scenes(self) -> None:
        self.__start_menu = self.__create_disposed_scene(StartMenu)
        self.__game = self.__create_disposed_scene(Game)
        self.__scene_group.append(self.__game)
        self.__level_menu = LevelMenu()
        self.__scene_group.append(self.__level_menu)

    @staticmethod
    def __create_disposed_scene(scene_type: Type[Scene]):  # TODO:- Fix the type hints for this
        scene: Scene = scene_type()
        scene.dispose()
        return scene

    def __init_callbacks(self) -> None:
        event_handler.subscribe(application_events.START_GAME, self.__game.restart)
        event_handler.subscribe(application_events.END_GAME, self.__game.dispose)
        event_handler.subscribe(application_events.STOP_LEVEL_MENU, self.__level_menu.dispose)

    def update(self) -> None:
        self.__scene_group.update()

    def render(self) -> None:
        self.__scene_group.render()
