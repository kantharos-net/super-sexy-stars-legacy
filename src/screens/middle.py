import sys

import pygame

from elements.button import Button
from elements.game_status import GameState, GameStatus
from elements.input_box import InputBox
from elements.player import Player
from elements.text import Text
from screens.common import *


class MiddleScreen():
    screen: pygame.Surface = None
    settings: dict = {}

    def __init__(self,
                 screen: pygame.Surface = screen,
                 settings: dict = settings
                 ):
        self.screen = screen
        self.settings = settings
        self.initial_load = False

        self.game_title = None
        self.play_button = None
        self.back_button = None
        self.name_inputbox = None
        self.copyright_button = None

    def load_middle_screen(self) -> None:
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
            text=self.settings["play_button_text"],
            width=self.settings["play_button_width"],
            height=self.settings["play_button_height"],
            position_x=self.settings["play_button_pos_x"],
            position_y=self.settings["play_button_pos_y"],
            text_font=self.settings["play_button_text_font"],
            text_size=self.settings["play_button_text_size"],
            screen=self.screen,
            button_color=tuple(self.settings["play_button_color"]),
            text_color=tuple(self.settings["play_button_text_color"])
        )

        self.back_button = Button(
            text=self.settings["middle_back_button_text"],
            width=self.settings["middle_back_button_width"],
            height=self.settings["middle_back_button_height"],
            position_x=self.settings["middle_back_button_pos_x"],
            position_y=self.settings["middle_back_button_pos_y"],
            text_font=self.settings["middle_back_button_text_font"],
            text_size=self.settings["middle_back_button_text_size"],
            screen=self.screen,
            button_color=tuple(self.settings["middle_back_button_color"]),
            text_color=tuple(self.settings["middle_back_button_text_color"])
        )

        self.name_inputbox = InputBox(
            standard_text=self.settings["name_inputbox_standard_text"],
            width=self.settings["name_inputbox_width"],
            height=self.settings["name_inputbox_height"],
            position_x=self.settings["name_inputbox_pos_x"],
            position_y=self.settings["name_inputbox_pos_y"],
            text_font=self.settings["name_inputbox_text_font"],
            text_size=self.settings["name_inputbox_text_size"],
            max_character=self.settings["name_inputbox_max_character"],
            border_size=self.settings["name_inputbox_border_size"],
            border_color=self.settings["name_inputbox_border_color"],
            screen=self.screen,
            active_color=self.settings["name_inputbox_active_color"],
            inactive_color=self.settings["name_inputbox_inactive_color"],
            text_color=self.settings["name_inputbox_text_color"]
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
        self.back_button.draw_button()
        self.name_inputbox.draw_inputbox()
        self.copyright_button.draw_button()

        pygame.display.flip()

    def run_middle_screen(self, game_status: GameStatus) -> None:
        if not self.initial_load:
            self.load_middle_screen()
            self.initial_load = True

        for event in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            Player.name = self.name_inputbox.update_inputbox(mouse_x, mouse_y, event)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.play_button.is_clicked(mouse_x, mouse_y):
                    game_status.game_screen = GameState.PLAYING
                    clear_screen(screen=self.screen, settings=self.settings)
                    self.initial_load = False
                elif self.back_button.is_clicked(mouse_x, mouse_y):
                    game_status.game_screen = GameState.TITLE
                    clear_screen(screen=self.screen, settings=self.settings)
                    self.initial_load = False
                elif self.copyright_button.is_clicked(mouse_x, mouse_y):
                    game_status.game_screen = GameState.COPYRIGHT
                    clear_screen(screen=self.screen, settings=self.settings)
                    self.initial_load = False
