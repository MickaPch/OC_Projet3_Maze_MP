class Player():

    def __init__(self, carte):
        """
        Initialisation de la position de départ du joueur et de son affichage.
        """
        self.position = carte.entrance
        self.posx = self.position[0]
        self.posy = self.position[1]
        self.print = 'P'

    def on_move(self, keyboard_input, carte):
        """
        Contrôle si le mouvement est possible ou non.
        """
        if keyboard_input == 8:
            test_position = (self.posx, self.posy - 1)
            if test_position in carte.allowed_tiles:
                self.position = test_position
        elif keyboard_input == 6:
            test_position = (self.posx + 1, self.posy)
            if test_position in carte.allowed_tiles:
                self.position = test_position
        elif keyboard_input == 5:
            test_position = (self.posx, self.posy + 1)
            if test_position in carte.allowed_tiles:
                self.position = test_position
        elif keyboard_input == 4:
            test_position = (self.posx - 1, self.posy)
            if test_position in carte.allowed_tiles:
                self.position = test_position
        self.posx = self.position[0]
        self.posy = self.position[1]
