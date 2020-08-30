from elements.round import Round

class GameStatus():
    game_active: bool = False
    initial_setup: bool =  True

    def __init__(self, game_active: bool = game_active, initial_setup: bool = initial_setup):
        self.game_active = game_active
        self.initial_setup = initial_setup
        # self.round = Round()
