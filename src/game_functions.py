import sys
import pygame
from board import Board
from button import Button
from settings import Settings


def check_events(ai_settings, screen, play_button, game_board, stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, play_button, game_board, stats, mouse_x, mouse_y) 
        

def check_play_button(ai_settings, screen, play_button, game_board, stats, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and not stats.game_active:
           #pygame.mouse.set_visible(False)
           game_board.draw_board()
           stats.game_active = True

          
def update_screen(ai_settings, screen, stats, play_button, game_board):
    screen.fill(ai_settings.bg_color)
    if not stats.game_active:
        play_button.draw_button()
    else:
        game_board.draw_board()
    pygame.display.flip()
    
