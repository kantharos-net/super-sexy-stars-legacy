from enum import Enum

from elements.round import Round


class GameState(Enum):
    TITLE = 0
    RULES = 1
    MIDDLE = 3
    PLAYING = 4
    COPYRIGHT = 5

class GameStatus():
    game_screen: GameState = GameState.TITLE

    def __init__(self, game_screen: GameState = game_screen):
        self.game_screen = game_screen
        # self.round = Round()
