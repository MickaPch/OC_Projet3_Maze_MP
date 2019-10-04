import random


class Item:
    """Items to pick"""
    # Ajouter sous-classes pour chaque item pour
    # personnaliser les blit dans pygame
    item_list = list()

    def __init__(self, carte):
        """
        Position de départ aléatoire dans la liste des cases autorisées
        """
        if Item.item_list == []:
            self.position = carte.allowed_tiles[
                random.randint(0, len(carte.allowed_tiles) - 1)
                ]
            Item.item_list.append(self.position)
        else:
            test = True
            while test:
                position_test = carte.allowed_tiles[
                    random.randint(0, len(carte.allowed_tiles) - 1)
                ]
                if position_test not in Item.item_list:
                    self.position = position_test
                    test = False
        self.posx = self.position[0]
        self.posy = self.position[1]
