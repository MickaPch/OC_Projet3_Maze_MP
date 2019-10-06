import random
import copy


class Item:
    """
    Items to pick. Initialize 3 items from different positions.
    """
    list_items = []

    def __init__(self, carte, guardian):
        """
        Position de départ aléatoire dans la liste des cases autorisées
        """
        if Item.list_items == []:
            allowed_positions = copy.deepcopy(carte.allowed_tiles)
            allowed_positions.pop(
                carte.allowed_tiles.index(guardian.position))
            Item.list_items = random.sample(allowed_positions, 3)
        self.position = Item.list_items.pop(0)
        self.posx = self.position[0]
        self.posy = self.position[1]
