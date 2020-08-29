import json
import pygame
import sys
import game_functions as gf
from game_stats import GameStats

from elements.board import Board
from elements.button import Button

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

def run_game():
    # LOAD THINGS
    settings = load_settings()
    game_data = load_data_files()

    # GAME INIT
    pygame.init()
    screen = pygame.display.set_mode((settings["screen_width"], settings["screen_height"]))
    pygame.display.set_caption(settings["title"])
    play_button = Button(screen ,"start")
    game_board = Board(settings, screen)
    stats = GameStats()
    
    while True:
        gf.check_events(screen, play_button, game_board, stats)  
        gf.update_screen(settings, screen, stats, play_button, game_board)

run_game()

    