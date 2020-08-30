import json
import pygame
import sys
import game_flow
from game_status import GameStatus

from elements.board import Board
from elements.button import Button
from elements.log_screen import LogScreen

data_files_path = "./config/game-data.json"
settings_path = "./config/settings.json"

def load_data_files() -> dict:
    try:
        fd = open(data_files_path)
        data = dict(json.load(fd))
        fd.close()
    except FileNotFoundError as fnf:
        print(fnf.args)
        exit(1)
    
    return data

def load_settings() -> dict:
    try:
        fd = open(settings_path)
        settings = dict(json.load(fd))
        fd.close()
    except FileNotFoundError as fnf:
        print(fnf.args)
        exit(1)
    
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
            game_flow.title_screen(screen = screen, settings = settings, stats = stats)
        else:
            game_flow.game_screen(screen = screen, settings = settings, stats = stats)
'''            
            game_flow.check_events(
                screen = screen,
                play_button = play_button,
                game_board = game_board,
                stats = stats
            )  
            game_flow.update_screen(
                settings = settings, 
                screen = screen,
                play_button = play_button,
                game_board = game_board,
                stats = stats
            )
'''

run_game()   