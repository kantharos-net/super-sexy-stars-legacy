import pygame
import sys
from typing import List, Tuple
#from card import Card

class Board():
    width: int = 950
    height: int = 800
    board_color: Tuple[int, int, int] = (0,0,0)
    screen: pygame.Surface = None

    def __init__(self, settings,
        screen: pygame.Surface = screen,
        width: int = width,
        height: int = height,
        board_color: Tuple[int, int, int] = board_color
    ):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width = width
        self.height = height
        self.board_color = board_color
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
