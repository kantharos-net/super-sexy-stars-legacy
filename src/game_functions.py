import sys
import pygame
from elements.board import Board
from elements.button import Button

###################################################################################
#
# GAME FUNCIONS
#
# Manage all events and update screen of the game.
#
###################################################################################

# Check all the events of the game.
def check_events(screen, play_button, game_board, stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(screen, stats, play_button, game_board, mouse_x, mouse_y) 
        
# Check the event of mouse click. Sets the game as started or not.
def check_play_button(screen, stats, play_button, game_board, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and not stats.game_active:
           game_board.draw_board()
           stats.game_active = True

# Keeps the screen updated while the game is still running.
def update_screen(settings, screen, stats, play_button, game_board):
    screen.fill(settings["bg_color"])
    if not stats.game_active:
        play_button.draw_button()
    else:
        game_board.draw_board()
    pygame.display.flip()
    
