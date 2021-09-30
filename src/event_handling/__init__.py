from src.event_handling.custom_event_handler import EventCreator
from src.event_handling.event_handler import EventHandler


event_handler: EventHandler = EventHandler()
supported_event_formats: type = event_handler.supported_callback_events
event_creator: EventCreator = EventCreator()
