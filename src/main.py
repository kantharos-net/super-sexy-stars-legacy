import json
import sys

import pygame

from elements.game_status import GameState, GameStatus
from screens.game import GameScreen
from screens.rules import RulesScreen
from screens.title import TitleScreen
from screens.copyright import CopyrightScreen

DATA_FILES_PATH = "./config/game-data.json"
SETTINGS_PATH = "./config/settings.json"

# Method to load game data
def load_data_files() -> dict:
    try:
        file_d = open(DATA_FILES_PATH)
        data = dict(json.load(file_d))
        file_d.close()
    except FileNotFoundError as fnf:
        print(fnf.args)
        sys.exit(1)

    return data

# Method to load game settings
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
    # Load settings and game data.
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

    game_status = GameStatus()

    title_screen = TitleScreen(screen=screen, settings=settings)
    game_screen = GameScreen(screen=screen, settings=settings)
    rules_screen = RulesScreen(screen=screen, settings=settings)
    copyright_screen = CopyrightScreen(screen=screen, settings=settings)

    while True:
        if game_status.game_screen == GameState.TITLE:
            title_screen.run_title_screen(game_status)
        elif game_status.game_screen == GameState.RULES:
            rules_screen.run_rules_screen(game_status)
        elif game_status.game_screen == GameState.COPYRIGHT:
            copyright_screen.run_copyright_screen(game_status)
        elif game_status.game_screen == GameState.PLAYING:
            game_screen.run_game_screen(game_status)

run_game()
