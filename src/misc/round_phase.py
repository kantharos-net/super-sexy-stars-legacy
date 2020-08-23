from enum import Enum

class RoundPhase(Enum):
    ROUND_START = 0
    ATTR_CHOOSING = 1
    ATTR_COMPARISON = 2
    CARD_REDIST = 3
    ROUND_END = 4
