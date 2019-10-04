import pygame
from classes.grid import Grid
from classes.maze import Maze
from classes.guardian import Guardian
from classes.player import Player
from classes.item import Item
from classes.bag import Bag


class Game:
    """Game loop"""
    def __init__(self):
        self._running = True
        # self._display_surf = None
        # self.width = 600
        # self.height = 600
        # self.size = (self.width, self.height)

    def on_init(self, file):
        """
        Initialize the game parameters
        """
        # pygame.init()           # Initialization of pygame

        self.carte = Grid()
        self.carte.initialize_maze(file)
        self.maze = Maze(self.carte)
        self.guardian = Guardian(self.carte)
        self.player = Player(self.carte)
        self.needle = Item(self.carte)
        self.tube = Item(self.carte)
        self.ether = Item(self.carte)
        self.bag = Bag()
        self.objects_list = [
            self.carte,
            self.player,
            self.guardian,
            self.needle,
            self.tube,
            self.ether,
            self.bag
            ]
        self._running = True

    def move(self):
        """
        Control the input.
        """
        input_loop = True
        while input_loop:
            try:
                keyboard_input = int(input(
                        'Déplacement du joueur (8, 5, 4, 6)\n>>> '
                        ))
                keyboard_input in [4, 5, 6, 8]
                input_loop = False
                self.player.on_move(keyboard_input, self.carte)
            except:
                input_loop = True

    def on_execute(self):
        """Game"""
        while self._running:
            self.maze.refresh(*self.objects_list)
            print(self.maze)
            print(
                "Bag :\nNeedle : {}\nTube : {}\nEther : {}".format(
                    self.bag.is_needle,
                    self.bag.is_tube,
                    self.bag.is_ether
                ))
            self.move()
            self.maze.refresh(*self.objects_list)
            if self.player.position == self.guardian.position:
                if self.bag.full:
                    print(self.maze)
                    print("Well done !\nYou beat the guardian !")
                else:
                    print(self.maze)
                    print('Game Over !!!')
                    self._running = False
            if self.player.position == self.carte.exit:
                print(self.maze)
                print("GREAAAAT !!! \nYou won this game !!!")
                self._running = False
