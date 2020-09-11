import sys

import pygame


def clear_screen(
        screen: pygame.Surface,
        settings: dict
    ) -> None:
    screen.fill(settings["bg_color"])
    pygame.display.flip()


def load_text(path: str) -> str:
    try:
        file_d = open(path)
        content = file_d.read()
        file_d.close()
    except FileNotFoundError as fnf:
        print("Could not find file " + path + " " + fnf.args)
        sys.exit(1)

    return str(content)
