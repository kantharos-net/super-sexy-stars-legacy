import sys

import pygame

from elements.button import Button
from elements.game_status import GameState, GameStatus
from elements.text import Text
from screens.common import *


class TitleScreen():
    screen: pygame.Surface = None
    settings: dict = {}

    def __init__(self,
                 screen: pygame.Surface = screen,
                 settings: dict = settings
                 ):
        self.screen = screen
        self.settings = settings
        self.initial_load = False

        self.play_button = None
        self.rules_button = None
        self.quit_button = None
        self.game_title = None
        self.copyright_button = None

    def load_title_screen(self) -> None:
        self.game_title = Text(
            text=self.settings["title_text_text"],
            width=self.settings["title_text_width"],
            height=self.settings["title_text_height"],
            position_x=self.settings["title_text_pos_x"],
            position_y=self.settings["title_text_pos_y"],
            text_font=self.settings["title_text_text_font"],
            text_size=self.settings["title_text_text_size"],
            screen=self.screen,
            text_color=tuple(self.settings["title_text_text_color"])
        )

        self.play_button = Button(
            text=self.settings["start_button_text"],
            width=self.settings["start_button_width"],
            height=self.settings["start_button_height"],
            position_x=self.settings["start_button_pos_x"],
            position_y=self.settings["start_button_pos_y"],
            text_font=self.settings["start_button_text_font"],
            text_size=self.settings["start_button_text_size"],
            screen=self.screen,
            button_color=tuple(self.settings["start_button_color"]),
            text_color=tuple(self.settings["start_button_text_color"])
        )

        self.rules_button = Button(
            text=self.settings["rules_button_text"],
            width=self.settings["rules_button_width"],
            height=self.settings["rules_button_height"],
            position_x=self.settings["rules_button_pos_x"],
            position_y=self.settings["rules_button_pos_y"],
            text_font=self.settings["rules_button_text_font"],
            text_size=self.settings["rules_button_text_size"],
            screen=self.screen,
            button_color=tuple(self.settings["rules_button_color"]),
            text_color=tuple(self.settings["rules_button_text_color"])
        )

        self.quit_button = Button(
            text=self.settings["quit_button_text"],
            width=self.settings["quit_button_width"],
            height=self.settings["quit_button_height"],
            position_x=self.settings["quit_button_pos_x"],
            position_y=self.settings["quit_button_pos_y"],
            text_font=self.settings["quit_button_text_font"],
            text_size=self.settings["quit_button_text_size"],
            screen=self.screen,
            button_color=tuple(self.settings["quit_button_color"]),
            text_color=tuple(self.settings["quit_button_text_color"])
        )

        self.copyright_button = Button(
            text=self.settings["copyright_button_text"],
            width=self.settings["copyright_button_width"],
            height=self.settings["copyright_button_height"],
            position_x=self.settings["copyright_button_pos_x"],
            position_y=self.settings["copyright_button_pos_y"],
            text_font=self.settings["copyright_button_text_font"],
            text_size=self.settings["copyright_button_text_size"],
            screen=self.screen,
            button_color=tuple(self.settings["copyright_button_color"]),
            text_color=tuple(self.settings["copyright_button_text_color"])
        )

        self.game_title.draw_text()
        self.play_button.draw_button()
        self.rules_button.draw_button()
        self.copyright_button.draw_button()
        self.quit_button.draw_button()
        pygame.display.flip()

    def run_title_screen(self, game_status: GameStatus) -> None:
        if not self.initial_load:
            self.load_title_screen()
            self.initial_load = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if self.play_button.is_clicked(mouse_x, mouse_y):
                    game_status.game_screen = GameState.MIDDLE
                    clear_screen(screen=self.screen, settings=self.settings)
                    self.initial_load = False
                elif self.rules_button.is_clicked(mouse_x, mouse_y):
                    game_status.game_screen = GameState.RULES
                    clear_screen(screen=self.screen, settings=self.settings)
                    self.initial_load = False
                elif self.copyright_button.is_clicked(mouse_x, mouse_y):
                    game_status.game_screen = GameState.COPYRIGHT
                    clear_screen(screen=self.screen, settings=self.settings)
                    self.initial_load = False
                elif self.quit_button.is_clicked(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit(0)
