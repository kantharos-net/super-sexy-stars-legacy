from typing import List
from player import Player
from card import Card
from .misc.round_phase import RoundPhase
from .misc.round_state import RoundState

class Round(object):
    number: int = 0
    attr_selection: str = ""
    state: RoundState = 0
    winner: Player = Player("",[])
    players: List[Player] = []
    comparison: List[Card] = []

    def __init__(self, 
        number: int = number,
        attr_selection: str = attr_selection,
        state: RoundState = state,
        winner: Player = winner,
        players: List[Player] = players,
        comparison: List[Card] = comparison,
    ):
        self.number=number
        self.attr_selection=attr_selection
        self.state=state
        self.winner=winner
        self.players=players
        self.comparison=comparison

    def dump_object(self) -> None:
        pass