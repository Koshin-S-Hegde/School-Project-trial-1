import sys
import pygame

from src.application_handling.application_handler import ApplicationHandler
from src.event_handling import event_handler


def main() -> None:
    pygame.init()
    pygame.display.set_mode((500, 500), pygame.RESIZABLE)
    event_handler.subscribe(pygame.QUIT, handle_game_quit)
    run()


def run() -> None:
    application_handler: ApplicationHandler = ApplicationHandler()
    while True:
        update(application_handler)
        pygame.event.clear()
        render(application_handler)


def update(application_handler: ApplicationHandler) -> None:
    event_handler.update()
    application_handler.update()


def render(application_handler: ApplicationHandler) -> None:
    pygame.display.get_surface().fill((0, 0, 0))
    application_handler.render()
    pygame.display.flip()


def handle_game_quit() -> None:
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
