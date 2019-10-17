import random
import copy


class Item:
    """
    Items to pick. Initialize 3 items from different positions.
    """
    list_items = []

    def __init__(self, game_map, guardian, player):
        """
        Random start position in allowed_podisions
        """
        if Item.list_items == []:
            allowed_positions = copy.deepcopy(game_map.allowed_tiles)
            del allowed_positions[game_map.allowed_tiles.index(guardian.position)]
            del allowed_positions[game_map.allowed_tiles.index(game_map.exit)]
            Item.list_items = random.sample(allowed_positions, 3)
        self.position = Item.list_items.pop(0)
        self.posx = self.position[0]
        self.posy = self.position[1]
