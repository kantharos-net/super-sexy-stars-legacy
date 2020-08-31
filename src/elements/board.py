import pygame
import sys
from typing import Tuple

class Board():
    width: int = 0
    height: int = 0
    position_x: int = 0
    position_y: int = 0
    board_color: Tuple[int, int, int] = (0,0,0)
    screen: pygame.Surface = None

    def __init__(self,
        width: int = width,
        height: int = height,
        position_x: int = position_x,
        position_y: int = position_y,
        screen: pygame.Surface = screen,
        board_color: Tuple[int, int, int] = board_color
    ):
        self.width = width
        self.height = height
        self.screen = screen
        self.board_color = board_color
        self.board_rect = pygame.Rect(
            (self.position_x, self.position_y),
            (self.width, self.height)
        )

    def draw_board(self) -> None:
        self.screen.fill(self.board_color, self.board_rect)

    def dump_object(self) -> None:
        pass
