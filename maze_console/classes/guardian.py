class Guardian():
    def __init__(self, carte):
        """
        Initialisation de la position du gardien
        """
        if carte.exit[0] == 0:
            self.position = (carte.exit[0] + 1, carte.exit[1])
        elif carte.exit[0] == carte._len_X - 1:
            self.position = (carte.exit[0] - 1, carte.exit[1])
        elif carte.exit[1] == 0:
            self.position = (carte.exit[0], carte.exit[1] + 1)
        elif carte.exit[1] == carte._len_Y - 1:
            self.position = (carte.exit[0], carte.exit[1] - 1)
        self.posx = self.position[0]
        self.posy = self.position[1]
        self.print = 'G'
