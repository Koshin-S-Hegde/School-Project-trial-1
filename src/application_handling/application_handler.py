from typing import Type

from src.application_handling import application_events
from src.application.game.game import Game
from src.application.level_menu import LevelMenu
from src.application.main_menu import MainMenu
from src.application.pause_menu import PauseMenu
from src.application_handling.scenes.scene import Scene
from src.application_handling.scenes.scene_group import SceneGroup
from src.event_handling import event_handler


class ApplicationHandler:
    __main_menu: MainMenu
    __level_menu: LevelMenu
    __pause_menu: PauseMenu
    __game: Game
    __pause_menu: Scene
    __end_menu: Scene
    __scene_group: SceneGroup

    def __init__(self) -> None:
        self.__scene_group = SceneGroup()
        self.__init_scenes()
        self.__init_callbacks()

    def __init_scenes(self) -> None:
        self.__main_menu = MainMenu()
        self.__level_menu = self.__create_disposed_scene(LevelMenu)
        self.__pause_menu = self.__create_disposed_scene(PauseMenu)
        self.__game = self.__create_disposed_scene(Game)
        self.__scene_group.append(self.__main_menu)
        self.__scene_group.append(self.__level_menu)
        self.__scene_group.append(self.__pause_menu)
        self.__scene_group.append(self.__game)

    @staticmethod
    def __create_disposed_scene(scene_type: Type):  # TODO:- Fix the type hints for this
        scene: scene_type = scene_type()
        scene.dispose()
        return scene

    def __init_callbacks(self) -> None:
        # main menu
        event_handler.subscribe(application_events.START_MAIN_MENU, self.__main_menu.restart)
        event_handler.subscribe(application_events.STOP_MAIN_MENU, self.__main_menu.dispose)
        # level menu
        event_handler.subscribe(application_events.START_LEVEL_MENU, self.__level_menu.restart)
        event_handler.subscribe(application_events.STOP_LEVEL_MENU, self.__level_menu.dispose)
        # pause menu
        event_handler.subscribe(application_events.START_PAUSE_MENU, self.__pause_menu.restart)
        event_handler.subscribe(application_events.STOP_PAUSE_MENU, self.__pause_menu.dispose)
        # game
        event_handler.subscribe(application_events.START_GAME, self.__game.restart)
        event_handler.subscribe(application_events.END_GAME, self.__game.dispose)

    def update(self) -> None:
        self.__scene_group.update()

    def render(self) -> None:
        self.__scene_group.render()
