import json
import sys

import pygame

from screens.copyright import CopyrightScreen
from screens.game import GameScreen
from screens.middle import MiddleScreen
from screens.rules import RulesScreen
from screens.title import TitleScreen
from utils.common import load_json_file
from utils.game_status import GameState, GameStatus

DATA_FILES_PATH = "./config/game-data.json"
SETTINGS_PATH = "./config/settings.json"

def run_game():
    # Load settings and game data.
    settings = load_json_file(SETTINGS_PATH)
    game_data = load_json_file(DATA_FILES_PATH)

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
    middle_screen = MiddleScreen(screen=screen, settings=settings)
    copyright_screen = CopyrightScreen(screen=screen, settings=settings)

    while True:
        if game_status.game_screen == GameState.TITLE:
            title_screen.run_title_screen(game_status)
        elif game_status.game_screen == GameState.RULES:
            rules_screen.run_rules_screen(game_status)
        elif game_status.game_screen == GameState.MIDDLE:
            middle_screen.run_middle_screen(game_status)
        elif game_status.game_screen == GameState.COPYRIGHT:
            copyright_screen.run_copyright_screen(game_status)
        elif game_status.game_screen == GameState.PLAYING:
            game_screen.run_game_screen(game_status)

run_game()
