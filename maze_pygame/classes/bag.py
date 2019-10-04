class Bag:

    def __init__(self):
        """
        Au départ : sac vide
        """
        self.is_needle = False
        self.is_tube = False
        self.is_ether = False
        self.full = False

    def control_bag(self, player, needle, tube, ether):
        """
        Contrôle si le joueur ramasse un objet
        """
        if (player.posx, player.posy) == (needle.posx, needle.posy):
            self.is_needle = True
        elif (player.posx, player.posy) == (tube.posx, tube.posy):
            self.is_tube = True
        elif (player.posx, player.posy) == (ether.posx, ether.posy):
            self.is_ether = True

        # Contrôle si le sac est plein
        if self.is_needle and self.is_tube and self.is_ether:
            self.full = True

        return self.is_needle, self.is_tube, self.is_ether, self.full
