from src.application.credit_menu import CreditMenu
from src.application.license_menu import LicenseMenu
from src.application_handling import application_events
from src.application.game.game import Game
from src.application.main_menu import MainMenu
from src.application.pause_menu import PauseMenu
from src.application_handling.scenes.scene import Scene
from src.application_handling.scenes.scene_group import SceneGroup
from src.application.end_menu import EndMenu
from src.event_handling import event_handler


class ApplicationHandler:
    __main_menu: MainMenu
    __pause_menu: PauseMenu
    __game: Game
    __end_menu: EndMenu
    __credit_menu: CreditMenu
    __credit_menu: Scene
    __license_menu: Scene
    __license_menu: LicenseMenu
    __pause_menu: Scene
    __end_menu: Scene
    __scene_group: SceneGroup

    def __init__(self) -> None:
        self.__scene_group = SceneGroup()
        self.__init_scenes()
        self.__init_callbacks()

    def __init_scenes(self) -> None:
        self.__main_menu = MainMenu()
        self.__main_menu.restart()
        self.__pause_menu = PauseMenu()
        self.__end_menu = EndMenu()
        self.__license_menu = LicenseMenu()
        self.__credit_menu = CreditMenu()
        self.__game = Game()
        # scene group
        self.__scene_group.append(self.__game)
        self.__scene_group.append(self.__main_menu)
        self.__scene_group.append(self.__pause_menu)
        self.__scene_group.append(self.__end_menu)
        self.__scene_group.append(self.__license_menu)
        self.__scene_group.append(self.__credit_menu)

    def __init_callbacks(self) -> None:
        # main menu
        event_handler.subscribe(application_events.START_MAIN_MENU, self.__main_menu.restart)
        event_handler.subscribe(application_events.STOP_MAIN_MENU, self.__main_menu.dispose)
        # pause menu
        event_handler.subscribe(application_events.START_PAUSE_MENU, self.__pause_menu.restart)
        event_handler.subscribe(application_events.STOP_PAUSE_MENU, self.__pause_menu.dispose)
        # game
        event_handler.subscribe(application_events.START_GAME, self.__game.restart)
        event_handler.subscribe(application_events.PAUSE_GAME, self.__game.pause)
        event_handler.subscribe(application_events.RESUME_GAME, self.__game.resume)
        event_handler.subscribe(application_events.STOP_GAME, self.__game.dispose)
        # end menu
        event_handler.subscribe(application_events.START_END_MENU, self.__end_menu.restart)
        event_handler.subscribe(application_events.STOP_END_MENU, self.__end_menu.dispose)
        # credit menu
        event_handler.subscribe(application_events.START_CREDIT_MENU, self.__credit_menu.restart)
        event_handler.subscribe(application_events.STOP_CREDIT_MENU, self.__credit_menu.dispose)
        # license menu
        event_handler.subscribe(application_events.START_LICENSE_MENU,self.__license_menu.restart)
        event_handler.subscribe(application_events.STOP_LICENSE_MENU,self.__license_menu.dispose)

    def update(self) -> None:
        self.__scene_group.update()

    def render(self) -> None:
        self.__scene_group.render()
