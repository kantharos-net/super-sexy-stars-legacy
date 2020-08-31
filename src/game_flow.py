import sys
import pygame
from elements.board import Board
from elements.button import Button
from elements.text import Text
from elements.log_screen import LogScreen
from game_status import GameStatus

def title_screen(screen: pygame.Surface, settings: dict, stats:GameStatus) -> None:
    game_title = Text(
        text = settings["title_text_text"],
        width = settings["title_text_width"],
        height = settings["title_text_height"],
        position_x = settings["title_text_pos_x"],
        position_y = settings["title_text_pos_y"],
        text_font = settings["title_text_text_font"],
        text_size = settings["title_text_text_size"],
        screen = screen,
        text_color = tuple(settings["title_text_text_color"])
    )

    play_button = Button(
        text = settings["start_button_text"],
        width = settings["start_button_width"],
        height = settings["start_button_height"],
        position_x = settings["start_button_pos_x"],
        position_y = settings["start_button_pos_y"],
        text_font = settings["start_button_text_font"],
        text_size = settings["start_button_text_size"],
        screen = screen,
        button_color = tuple(settings["start_button_color"]),
        text_color = tuple(settings["start_button_text_color"])
    )

    rules_button = Button(
        text = settings["rules_button_text"],
        width = settings["rules_button_width"],
        height = settings["rules_button_height"],
        position_x = settings["rules_button_pos_x"],
        position_y = settings["rules_button_pos_y"],
        text_font = settings["rules_button_text_font"],
        text_size = settings["rules_button_text_size"],
        screen = screen,
        button_color = tuple(settings["rules_button_color"]),
        text_color = tuple(settings["rules_button_text_color"])
    )

    quit_button = Button(
        text = settings["quit_button_text"],
        width = settings["quit_button_width"],
        height = settings["quit_button_height"],
        position_x = settings["quit_button_pos_x"],
        position_y = settings["quit_button_pos_y"],
        text_font = settings["quit_button_text_font"],
        text_size = settings["quit_button_text_size"],
        screen = screen,
        button_color = tuple(settings["quit_button_color"]),
        text_color = tuple(settings["quit_button_text_color"])
    )

    game_title.draw_text()
    play_button.draw_button()
    rules_button.draw_button()
    quit_button.draw_button()

    while not stats.game_active:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if play_button.is_clicked(mouse_x, mouse_y):
                    stats.game_active = True
                elif rules_button.is_clicked(mouse_x, mouse_y):
                    show_rules(
                        screen = screen,
                        settings = settings
                    )
                elif quit_button.is_clicked(mouse_x, mouse_y):
                    sys.exit(1)


def show_rules(screen: pygame.Surface, settings: dict) -> None:
    try:
        rules_file = open(settings["rules_path"])
        rules_content = rules_file.read()
        rules_file.close()
    except FileNotFoundError as fnf:
        print(fnf.args)
        exit(1)

    print(rules_content)

def game_screen_initial_prep(screen: pygame.Surface, settings: dict) -> None:

    game_board = Board(
        width = settings["board_width"],
        height = settings["board_height"],
        screen = screen,
        board_color = tuple(settings["board_color"])
    )

    log_screen = LogScreen(
        width = settings["log_screen_width"],
        height = settings["log_screen_height"],
        top_message = settings["log_screen_top_message"],
        text_font = settings["log_screen_text_font"],
        text_size = settings["log_screen_text_size"],
        screen = screen,
        log_screen_color = tuple(settings["log_screen_color"]),
        log_screen_text_color = tuple(settings["log_screen_text_color"])
    )

    game_board.draw_board()
    log_screen.draw_log_screen()

    pass

def game_screen(screen: pygame.Surface, stats: GameStatus, settings: dict) -> None:
    if stats.initial_setup:
        game_screen_initial_prep(
            screen = screen,
            settings = settings
        )
        stats.initial_setup = False

    pass

def check_events(
        screen: pygame.Surface, 
        play_button: Button, 
        game_board: Board,
        log_screen: LogScreen,
        stats: GameStatus
    ) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_button.is_clicked(mouse_x, mouse_y) and not stats.game_active:
                game_board.draw_board()
                log_screen.draw_log_screen()
                stats.game_active = True

def update_screen(
        settings: dict, 
        screen: pygame.Surface, 
        stats: GameStatus, 
        play_button: Button, 
        game_board: Board
    ) -> None:
    screen.fill(settings["bg_color"])
    if not stats.game_active:
        play_button.draw_button()
    else:
        game_board.draw_board()
    pygame.display.flip()
    
