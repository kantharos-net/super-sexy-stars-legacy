import json
import pygame
import sys
import game_functions as gf
from board import Board
from game_stats import GameStats
from settings import Settings
from button import Button

def load_data_files() -> dict:
    try:
        fd = open("./data/game-data.json")
        data = dict(json.load(fd))
        fd.close()
    except FileNotFoundError as fnf:
        print(fnf.args)
        exit(1)
    
    return data

def invoke_board() -> None:
    pass

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Super Trunfo Porn")
    play_button = Button(ai_settings,screen ,"start")
    game_board = Board(ai_settings,screen)
    stats = GameStats(ai_settings)
    while True:
        gf.check_events(ai_settings, screen, play_button, game_board, stats)  
        gf.update_screen(ai_settings, screen, stats, play_button, game_board)

run_game()

    