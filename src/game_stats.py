from elements.round import Round

class GameStats():
    game_active: bool = False

    def __init__(self, game_active: bool = game_active):
        self.game_active = game_active
        self.round = Round()
