class Guardian():
    def __init__(self, carte):
        """
        Initialize guardian position. 1 cell before exite to keep the exit and
        see where exit is.
        """
        # If exit on West wall
        if carte.exit[0] == 0:
            self.position = (carte.exit[0] + 1, carte.exit[1])
        # East wall
        elif carte.exit[0] == carte._len_X - 1:
            self.position = (carte.exit[0] - 1, carte.exit[1])
        # North wall
        elif carte.exit[1] == 0:
            self.position = (carte.exit[0], carte.exit[1] + 1)
        # South wall
        elif carte.exit[1] == carte._len_Y - 1:
            self.position = (carte.exit[0], carte.exit[1] - 1)
        self.posx = self.position[0]
        self.posy = self.position[1]
        self.print = 'G'
