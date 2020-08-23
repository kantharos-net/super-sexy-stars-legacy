import pygame

from card import Card
from typing import List

class Board(object):
    background: str = ""
    compare_field: List[Card] = []
    history: List[str] = []

    def __init__(self, 
        background: str = background,
        compare_field: List[Card] = compare_field,
        history: List[str] = history
    ):
        self.background=background
        self.compare_field=compare_field
        self.history = history

    def create_board(self) -> None:
        pass

    def dump_object(self) -> None:
        pass