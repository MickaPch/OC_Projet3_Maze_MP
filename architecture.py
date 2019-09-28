import os
import pygame
from pygame.locals import *

# DA PYTHON - PROJET 3

# Aidez MacGyver à s'échapper:
# Jeu de labyrinthe en pygame.

# Nom, attributs et méthodes des classes du jeu:


class Game:
    """
    Game loop.
    """
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.width = 200  # import data from other file
        self.height = 200  # import data from other file
        self.size = (self.width, self.height)

    def on_init(self):
        pygame.init()
        # adapt with Labyrinth class
        self._display_surf = pygame.display.set_mode(
            self.size, pygame.HWSURFACE
            )
        self._running = True

    def on_event(self):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if not self.on_init():
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


class Labyrinth:
    """
    Game grid.
    Import structure elements from other file.
    Size, wall, obstacles ...
    """


class Obstacle:
    """
    Wall, ...
    """


class MacGyver:
    """
    Player, item to move by keyboard controls ←↑↓→.
    Check if movement is possible on grid.
    Action on pick of an item.
    """

    def __init__(self):
        self.player = pygame.image.load(
                                    'Mac_Gyver_ressources/MacGyver.png'
                                    ).convert()
        # position de départ
        # sprite
        pass

    def on_move(self):
        # action de mouvement action joueur
        pass


class Item:
    """
    Items that need to be picked up (needle, tube, ether).
    Action on pick by MacGyver (disapear).
    """

    def __init__(self):
        # position de départ
        pass

    def _picked_up(self):
        # disparition de l'objet au passage de MacGyver
        pass


class Bag:
    """
    Fill when MacGyver pick an item, show what item is already pick.
    """

    def __init__(self):
        # Montrer sac qqpart dans la fenêtre de jeu
        # état de départ : vide
        pass

    def _fill(self):
        # Ajouter l'objet collecté dans le sac
        pass

    def _full(self):
        # sac plein
        return True


class Guardian:
    """
    Guardian of the exit of the labyrinth.
    Lose the game if all items aren't picked up.
    """

    def __init__(self):
        # position de départ : bloque la sortie du labyrinthe
        # sprite
        pass

    def _try_pass(self):
        # hu
        pass


if __name__ == "__main__":
    macGyverGame = Game()
    macGyverGame.on_execute()
