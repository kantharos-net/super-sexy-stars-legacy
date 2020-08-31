
class Card():
    name: str = ""
    rank: str = ""
    position: int = 0
    card_image: str = ""
    attributes: dict = {}
    is_super_t: bool = False

    def __init__(self,
                 name: str = name,
                 rank: str = rank,
                 position: int = position,
                 card_image: str = card_image,
                 attributes: dict = attributes,
                 is_super_t: bool = is_super_t
                 ):
        self.name = name
        self.rank = rank
        self.position = position
        self.card_image = card_image
        self.attributes = attributes
        self.is_super_t = is_super_t

    def dump_object(self) -> None:
        pass
