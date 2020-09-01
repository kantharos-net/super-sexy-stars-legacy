import pygame


def clear_screen(
        screen: pygame.Surface,
        settings: dict
    ) -> None:
    screen.fill(settings["bg_color"])
    pygame.display.flip()
