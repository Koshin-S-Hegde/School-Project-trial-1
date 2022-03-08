from src.event_handling import event_creator

# game
START_GAME: int = event_creator.create_event()
PAUSE_GAME: int = event_creator.create_event()
RESUME_GAME: int = event_creator.create_event()
END_GAME: int = event_creator.create_event()
# main menu
START_MAIN_MENU: int = event_creator.create_event()
STOP_MAIN_MENU: int = event_creator.create_event()
# pause menu
START_PAUSE_MENU: int = event_creator.create_event()
STOP_PAUSE_MENU: int = event_creator.create_event()
# end menu
START_END_MENU: int = event_creator.create_event()
STOP_END_MENU: int = event_creator.create_event()
# credit menu
START_CREDIT_MENU: int = event_creator.create_event()
STOP_CREDIT_MENU: int = event_creator.create_event()
# license_menu
START_LICENSE_MENU: int = event_creator.create_event()
STOP_LICENSE_MENU: int = event_creator.create_event()
