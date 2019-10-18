"""Guardian class. Init by position."""


class Guardian():
    """
    Guardian 1 cell before exit
    """
    def __init__(self, game_map):
        """
        Initialize guardian position. 1 cell before exit to keep the exit and
        see where exit is.
        Guardian on North wall.
        """
        self.position = (game_map.exit[0], game_map.exit[1] + 1)
        self.posx = self.position[0]
        self.posy = self.position[1]
