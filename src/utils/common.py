import json
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

def load_json_file(file_path: str) -> dict:
    try:
        file_d = open(file_path)
        data = dict(json.load(file_d))
        file_d.close()
    except FileNotFoundError as fnf:
        print(fnf.args)
        sys.exit(1)

    return data
    