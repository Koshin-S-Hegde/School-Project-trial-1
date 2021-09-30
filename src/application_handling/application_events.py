from src.event_handling import event_creator

START_GAME: int = event_creator.create_event()
END_GAME: int = event_creator.create_event()
STOP_LEVEL_MENU: int = event_creator.create_event()
