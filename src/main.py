import sys
import json
import pygame
import game_flow
from game_status import GameStatus

DATA_FILES_PATH = "./config/game-data.json"
SETTINGS_PATH = "./config/settings.json"

def load_data_files() -> dict:
    try:
        file_d = open(DATA_FILES_PATH)
        data = dict(json.load(file_d))
        file_d.close()
    except FileNotFoundError as fnf:
        print(fnf.args)
        sys.exit(1)

    return data

def load_settings() -> dict:
    try:
        file_d = open(SETTINGS_PATH)
        settings = dict(json.load(file_d))
        file_d.close()
    except FileNotFoundError as fnf:
        print(fnf.args)
        sys.exit(1)

    return settings

def invoke_board() -> None:
    pass

def first_setup(settings: dict) -> None:
    pass

def run_game():
    # LOAD THINGS
    settings = load_settings()
    game_data = load_data_files()
    first_setup(settings)

    # GAME INIT
    pygame.init()
    screen = pygame.display.set_mode(
        (settings["screen_width"], settings["screen_height"])
    )
    pygame.display.set_caption(settings["game_title"])
    screen.fill(settings["bg_color"])

    stats = GameStatus()

    while True:
        if not stats.game_active:
            game_flow.title_screen(screen=screen, settings=settings, stats=stats)
        else:
            game_flow.game_screen(screen=screen, settings=settings, stats=stats)

run_game()
