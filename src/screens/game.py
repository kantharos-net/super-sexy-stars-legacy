import sys

import pygame

from elements.board import Board
from elements.button import Button
from elements.log_screen import LogScreen
from elements.text import Text
from utils.common import clear_screen, load_text
from utils.game_status import GameState, GameStatus


class GameScreen():
    screen: pygame.Surface = None
    settings: dict = {}

    def __init__(self,
                 screen: pygame.Surface = screen,
                 settings: dict = settings
                 ):
        self.screen = screen
        self.settings = settings
        self.initial_load = False

        self.game_board = None
        self.log_screen = None
        self.log_screen_title_text = None
        self.confirm_button = None

    def load_game_screen(self) -> None:
        self.game_board = Board(
            width=self.settings["board_width"],
            height=self.settings["board_height"],
            position_x=self.settings["board_pos_x"],
            position_y=self.settings["board_pos_y"],
            screen=self.screen,
            board_color=tuple(self.settings["board_color"])
        )

        self.log_screen_title_text = Text(
            text=self.settings["log_screen_title_text_text"],
            width=self.settings["log_screen_title_text_width"],
            height=self.settings["log_screen_title_text_height"],
            position_x=self.settings["log_screen_title_text_pos_x"],
            position_y=self.settings["log_screen_title_text_pos_y"],
            text_font=self.settings["log_screen_title_text_text_font"],
            text_size=self.settings["log_screen_title_text_text_size"],
            screen=self.screen,
            text_color=tuple(self.settings["log_screen_title_text_text_color"])
        )

        self.log_screen = LogScreen(
            width=self.settings["log_screen_width"],
            height=self.settings["log_screen_height"],
            position_x=self.settings["log_screen_pos_x"],
            position_y=self.settings["log_screen_pos_y"],
            log_text=self.settings["log_screen_log_text"],
            text_font=self.settings["log_screen_text_font"],
            text_size=self.settings["log_screen_text_size"],
            screen=self.screen,
            log_screen_color=tuple(self.settings["log_screen_color"]),
            log_screen_text_color=tuple(self.settings["log_screen_text_color"])
        )

        self.confirm_button = Button(
            text=self.settings["confirm_button_text"],
            width=self.settings["confirm_button_width"],
            height=self.settings["confirm_button_height"],
            position_x=self.settings["confirm_button_pos_x"],
            position_y=self.settings["confirm_button_pos_y"],
            text_font=self.settings["confirm_button_text_font"],
            text_size=self.settings["confirm_button_text_size"],
            screen=self.screen,
            button_color=tuple(self.settings["confirm_button_color"]),
            text_color=tuple(self.settings["confirm_button_text_color"])
        )

        self.game_board.draw_board()
        self.log_screen.draw_log_screen()
        self.log_screen_title_text.draw_text()
        self.confirm_button.draw_button()
        pygame.display.flip()

    def run_game_screen(self, game_status: GameStatus) -> None:
        if not self.initial_load:
            self.load_game_screen()
            self.initial_load = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if self.confirm_button.is_clicked(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit(0)
