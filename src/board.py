import pygame
import sys
from settings import Settings
#from card import Card
#from typing import List

class Board():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width = 950
        self.height = 800
        self.board_color = (0,0,0)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topleft = self.screen_rect.topleft

    def draw_board(self):
        self.screen.fill(self.board_color, self.rect)

    #background: str = ""
    #compare_field: List[Card] = []
    #history: List[str] = []

    #def __init__(self, 
        #background: str = background,
        #compare_field: List[Card] = compare_field,
        #history: List[str] = history
    #):
        #self.background=background
        #self.compare_field=compare_field
        #self.history = history

    def dump_object(self) -> None:
        pass
