import random


class Item:
    """
    Items to pick. Initialize 3 items from different positions.
    """
    list_items = []

    def __init__(self, carte):
        """
        Position de départ aléatoire dans la liste des cases autorisées
        """
        if Item.list_items == []:
            Item.list_items = random.sample(carte.allowed_tiles, 3)
        self.position = Item.list_items.pop(0)
        self.posx = self.position[0]
        self.posy = self.position[1]
