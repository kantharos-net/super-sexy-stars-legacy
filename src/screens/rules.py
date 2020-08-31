import pygame
import sys
from screens.common import *
from elements.text import Text
from elements.button import Button
from elements.game_status import GameStatus, GameState


class RulesScreen():
    screen: pygame.Surface = None
    settings: dict = {}

    def __init__(self,
                 screen: pygame.Surface = screen,
                 settings: dict = settings
                 ):
        self.screen = screen
        self.settings = settings
        self.initial_load = False
        self.rules_title_text = None
        self.back_button = None
        self.rules_text = None

    def load_rules_screen(self) -> None:
        self.rules_title_text = Text(
            text=self.settings["rules_title_text_text"],
            width=self.settings["rules_title_text_width"],
            height=self.settings["rules_title_text_height"],
            position_x=self.settings["rules_title_text_pos_x"],
            position_y=self.settings["rules_title_text_pos_y"],
            text_font=self.settings["rules_title_text_text_font"],
            text_size=self.settings["rules_title_text_text_size"],
            screen=self.screen,
            text_color=tuple(self.settings["rules_title_text_text_color"])
        )

        self.back_button = Button(
            text=self.settings["back_button_text"],
            width=self.settings["back_button_width"],
            height=self.settings["back_button_height"],
            position_x=self.settings["back_button_pos_x"],
            position_y=self.settings["back_button_pos_y"],
            text_font=self.settings["back_button_text_font"],
            text_size=self.settings["back_button_text_size"],
            screen=self.screen,
            button_color=tuple(self.settings["back_button_color"]),
            text_color=tuple(self.settings["back_button_text_color"])
        )

        self.rules_text = Text(
            text=self.load_rules_text(),
            width=self.settings["rules_text_box_width"],
            height=self.settings["rules_text_box_height"],
            position_x=self.settings["rules_text_box_pos_x"],
            position_y=self.settings["rules_text_box_pos_y"],
            text_font=self.settings["rules_text_box_text_font"],
            text_size=self.settings["rules_text_box_text_size"],
            screen=self.screen,
            text_color=tuple(self.settings["rules_text_box_text_color"])
        )

        self.rules_title_text.draw_text()
        self.back_button.draw_button()
        self.rules_text.draw_text()
        pygame.display.flip()

    def run_rules_screen(self, game_status: GameStatus) -> None:
        if not self.initial_load:
            self.load_rules_screen()
            self.initial_load = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if self.back_button.is_clicked(mouse_x, mouse_y):
                    game_status.game_screen = GameState.TITLE
                    clear_screen(screen=self.screen, settings=self.settings)
                    self.initial_load = False

    def load_rules_text(self) -> str:
        try:
            rules_file = open(self.settings["rules_path"])
            rules_content = rules_file.read()
            rules_file.close()
        except FileNotFoundError as fnf:
            print(fnf.args)
            sys.exit(1)

        return str(rules_content)
