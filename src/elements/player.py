from elements.card import Card
from typing import List

class Player(object):
    name: str = ""
    hand: List[Card] = []

    def __init__(self, 
        name: str = name,
        hand: List[Card] = hand 
    ):
        self.name = name
        self.hand = hand

    def dump_object(self):
        pass
