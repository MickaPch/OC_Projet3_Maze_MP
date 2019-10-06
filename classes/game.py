import pygame
from pygame.locals import *
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
        self._display_surf = None
        self.width = 672
        self.height = 693
        self.size = (self.width, self.height)

    def on_init(self, file):
        """
        Initialize the game parameters
        """
        pygame.init()           # Initialization of pygame
        self._screen = pygame.display.set_mode(
            self.size, FULLSCREEN
            )

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

    def init_map(self):
        # Import images
        self.floor = pygame.image.load('ressources/floor.png').convert()
        self.wall = pygame.image.load('ressources/rock_block.png').convert()
        self.macgyver = pygame.image.load(
            'ressources/MacGyver2.png'
            ).convert_alpha()
        self.guard = pygame.image.load(
            'ressources/Gardien2.png'
            ).convert_alpha()
        self.exit_tile = pygame.image.load(
            'ressources/door_closed.png'
            ).convert()
        self.needle_img = pygame.image.load(
            'ressources/aiguille2.png'
            ).convert_alpha()
        self.tube_img = pygame.image.load(
            'ressources/tuyau2.png'
            ).convert_alpha()
        self.ether_img = pygame.image.load(
            'ressources/ether3.png'
            ).convert_alpha()
        self.bag_img = pygame.image.load(
            'ressources/bag2.png'
        ).convert_alpha()

        # Initialize all positions
        for allowed_position in self.carte.allowed_tiles:
            self._screen.blit(
                self.floor,
                (allowed_position[0]*32, allowed_position[1]*32)
            )
        for forbidden_position in self.carte.forbidden_tiles:
            self._screen.blit(
                self.wall,
                (forbidden_position[0]*32, forbidden_position[1]*32)
            )
        self._screen.blit(
            self.macgyver,
            (self.player.posx*32+4, self.player.posy*32)
        )
        self._screen.blit(
            self.guard,
            (self.guardian.posx*32+2, self.guardian.posy*32)
        )
        self._screen.blit(
            self.exit_tile,
            (self.carte.exit[0]*32, self.carte.exit[1]*32)
        )
        self._screen.blit(
            self.needle_img,
            (self.needle.position[0]*32, self.needle.position[1]*32)
        )
        self._screen.blit(
            self.ether_img,
            (self.ether.position[0]*32, self.ether.position[1]*32)
        )
        self._screen.blit(
            self.tube_img,
            (self.tube.position[0]*32, self.tube.position[1]*32)
        )
        self._screen.blit(
            self.bag_img,
            (1*32, 21*32)
        )

        pygame.display.flip()

        self._running = True

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
            return
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            self._running = False
            return
        elif event.type == KEYDOWN:
            return event.key

    def on_render(self):
        dirty_rects = []
        self._screen.blit(
            self.floor,
            (self.player.previouspos[0]*32, self.player.previouspos[1]*32)
        )
        dirty_rects.append(
            (self.player.previouspos[0]*32, self.player.previouspos[1]*32)
            )
        self._screen.blit(
            self.macgyver,
            (self.player.posx*32, self.player.posy*32)
        )
        dirty_rects.append((self.player.posx*32, self.player.posy*32))
        pygame.display.update(dirty_rects)

    def on_execute(self):
        """Game"""

        self.init_map()
        while self._running:
            pygame.time.delay(150)
            for event in pygame.event.get():
                if (event.type == QUIT or
                    (event.type == KEYDOWN and
                        event.key == K_ESCAPE)):
                    self._running = False
            self.player.enter_key(self.carte)
            self.player.print_position()
            self.on_render()

            # self.maze.refresh(*self.objects_list)
            # print(self.maze)
            # print(
            #     "Bag :\nNeedle : {}\nTube : {}\nEther : {}".format(
            #         self.bag.is_needle,
            #         self.bag.is_tube,
            #         self.bag.is_ether
            #     ))
            # self.move()
            # self.maze.refresh(*self.objects_list)
            # if self.player.position == self.guardian.position:
            #     # if self.bag.full:
            #     #     # print(self.maze)
            #     #     # print("Well done !\nYou beat the guardian !")
            #     # else:
            #     #     # print(self.maze)
            #     #     # print('Game Over !!!')
            #     #     self._running = False
            if self.player.position == self.carte.exit:
                # print(self.maze)
                # print("GREAAAAT !!! \nYou won this game !!!")
                self._running = False

        # self.clean_up()
