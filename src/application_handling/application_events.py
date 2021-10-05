from src.event_handling import event_creator

# game
START_GAME: int = event_creator.create_event()
PAUSE_GAME: int = event_creator.create_event()
RESUME_GAME: int = event_creator.create_event()
END_GAME: int = event_creator.create_event()
# level menu
START_LEVEL_MENU: int = event_creator.create_event()
STOP_LEVEL_MENU: int = event_creator.create_event()
# main menu
START_MAIN_MENU: int = event_creator.create_event()
STOP_MAIN_MENU: int = event_creator.create_event()
# pause menu
START_PAUSE_MENU: int = event_creator.create_event()
STOP_PAUSE_MENU: int = event_creator.create_event()
