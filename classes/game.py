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
        self.height = 704
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
        self.needle = Item(self.carte, self.guardian)
        self.tube = Item(self.carte, self.guardian)
        self.ether = Item(self.carte, self.guardian)
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
        self.item_1 = (5.5, 21)
        self.item_2 = (7, 21)
        self.item_3 = (8.5, 21)
        self.bag_items = [self.item_1, self.item_2, self.item_3]

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
        self.exit_open = pygame.image.load(
            'ressources/door_open.png'
        ).convert_alpha()
        self.needle_img = pygame.image.load(
            'ressources/aiguille2.png'
            ).convert_alpha()
        self.tube_img = pygame.image.load(
            'ressources/tuyau2.png'
            ).convert_alpha()
        self.ether_img = pygame.image.load(
            'ressources/ether3.png'
            ).convert_alpha()
        font = pygame.font.SysFont("ebrima", 22)
        self.bag_font = font.render("Bag content :", True, (255, 255, 255))
        self.text_full = font.render("=", True, (255, 255, 255))
        self.empty_bag = pygame.image.load(
            'ressources/item_empty.png'
        ).convert_alpha()
        self.item_bag = pygame.image.load(
            'ressources/item_pick.png'
        ).convert_alpha()
        self.seringue_img = pygame.image.load(
            'ressources/seringue2.png'
        ).convert_alpha()
        self.splash1 = pygame.image.load(
            'ressources/splash1.png'
        ).convert_alpha()
        self.splash2 = pygame.image.load(
            'ressources/splash2.png'
        ).convert_alpha()
        self.splash3 = pygame.image.load(
            'ressources/splash3.png'
        ).convert_alpha()
        self.rip = pygame.image.load(
            'ressources/rip.png'
        ).convert_alpha()

        # Initialize all positions
        for allowed_position in self.carte.allowed_tiles:
            self._screen.blit(
                self.floor,
                (allowed_position[0]*32, allowed_position[1]*32))
        for forbidden_position in self.carte.forbidden_tiles:
            self._screen.blit(
                self.wall,
                (forbidden_position[0]*32, forbidden_position[1]*32))
        self._screen.blit(
            self.macgyver,
            (self.player.posx*32+4, self.player.posy*32))
        self._screen.blit(
            self.guard,
            (self.guardian.posx*32+2, self.guardian.posy*32))
        self._screen.blit(
            self.exit_tile,
            (self.carte.exit[0]*32, self.carte.exit[1]*32))
        self._screen.blit(
            self.needle_img,
            (self.needle.position[0]*32, self.needle.position[1]*32))
        self._screen.blit(
            self.ether_img,
            (self.ether.position[0]*32, self.ether.position[1]*32))
        self._screen.blit(
            self.tube_img,
            (self.tube.position[0]*32, self.tube.position[1]*32))
        self._screen.blit(
            self.bag_font,
            (1*32, 21*32))
        self._screen.blit(
            self.empty_bag,
            (self.item_1[0]*32, self.item_1[1]*32))
        self._screen.blit(
            self.empty_bag,
            (self.item_2[0]*32, self.item_2[1]*32))
        self._screen.blit(
            self.empty_bag,
            (self.item_3[0]*32, self.item_3[1]*32))

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
        # Rects to actualize
        dirty_rects = []
        # Erase player previous position
        self._screen.blit(
            self.floor,
            (self.player.previouspos[0]*32, self.player.previouspos[1]*32))
        previous_position = pygame.rect.Rect(
            self.player.previouspos[0]*32,
            self.player.previouspos[1]*32,
            32,
            32)
        dirty_rects.append(previous_position)
        # Add actual player position
        self._screen.blit(
            self.macgyver,
            (self.player.posx*32+4, self.player.posy*32))
        current_position = pygame.rect.Rect(
            self.player.posx*32+4,
            self.player.posy*32,
            32,
            32)
        dirty_rects.append(current_position)
        # Add item if picked
        self.bag.control_bag(self.player, self.needle, self.tube, self.ether)
        if self.bag.needle_picked == 1:
            position = self.bag_items.pop(0)
            self._screen.blit(
                self.needle_img,
                (position[0]*32, position[1]*32)
            )
            self._screen.blit(
                self.item_bag,
                (position[0]*32, position[1]*32)
            )
            needle_position = pygame.rect.Rect(
                int(position[0]*32),
                int(position[1]*32),
                32,
                32)
            dirty_rects.append(needle_position)
            self.bag.needle_picked += 1
        elif self.bag.tube_picked == 1:
            position = self.bag_items.pop(0)
            self._screen.blit(
                self.tube_img,
                (position[0]*32, position[1]*32)
            )
            self._screen.blit(
                self.item_bag,
                (position[0]*32, position[1]*32)
            )
            tube_position = pygame.rect.Rect(
                int(position[0]*32),
                int(position[1]*32),
                32,
                32)
            dirty_rects.append(tube_position)
            self.bag.tube_picked += 1
        elif self.bag.ether_picked == 1:
            position = self.bag_items.pop(0)
            self._screen.blit(
                self.ether_img,
                (position[0]*32, position[1]*32)
            )
            self._screen.blit(
                self.item_bag,
                (position[0]*32, position[1]*32)
            )
            ether_position = pygame.rect.Rect(
                int(position[0]*32),
                int(position[1]*32),
                32,
                32)
            dirty_rects.append(ether_position)
            self.bag.ether_picked += 1
        if self.bag.full_items == 1:
            self._screen.blit(
                self.text_full,
                (10*32, 21*32))
            arrow_position = pygame.rect.Rect(10*32, 21*32, 32, 32)
            dirty_rects.append(arrow_position)
            self._screen.blit(
                self.seringue_img,
                (12*32, 21*32))
            sering_position = pygame.rect.Rect(12*32, 21*32, 32, 32)
            dirty_rects.append(sering_position)

            # Death animation
            guardian_position = pygame.rect.Rect(
                self.guardian.posx*32,
                self.guardian.posy*32,
                32,
                32)
            self._screen.blit(
                self.floor,
                (self.guardian.posx*32, self.guardian.posy*32))
            self._screen.blit(
                self.splash1,
                (self.guardian.posx*32, self.guardian.posy*32))
            pygame.display.update(guardian_position)
            pygame.time.delay(500)
            self._screen.blit(
                self.splash2,
                (self.guardian.posx*32, self.guardian.posy*32))
            pygame.display.update(guardian_position)
            pygame.time.delay(500)
            self._screen.blit(
                self.splash3,
                (self.guardian.posx*32, self.guardian.posy*32))
            pygame.display.update(guardian_position)
            pygame.time.delay(500)
            self._screen.blit(
                self.rip,
                (self.guardian.posx*32, self.guardian.posy*32))
            dirty_rects.append(guardian_position)

            self._screen.blit(
                self.floor,
                (self.carte.exit[0]*32, self.carte.exit[1]*32))
            self._screen.blit(
                self.exit_open,
                (self.carte.exit[0]*32, self.carte.exit[1]*32))
            exit_tile = pygame.rect.Rect(
                self.carte.exit[0]*32,
                self.carte.exit[1]*32,
                32,
                32)
            dirty_rects.append(exit_tile)
            self.bag.full_items += 1

        pygame.display.update(dirty_rects)

    def on_execute(self):
        """Game"""

        self.init_map()
        while self._running:
            pygame.time.delay(120)
            for event in pygame.event.get():
                if (event.type == QUIT or
                    (event.type == KEYDOWN and
                        event.key == K_ESCAPE)):
                    self._running = False
            self.player.enter_key(self.carte)
            self.player.print_position()
            self.on_render()

            if self.player.position == self.guardian.position:
                if not self.bag.full:
                    result_font = pygame.font.SysFont("ebrima", 60, bold=1)
                    game_over = result_font.render(
                        "Game Over !!!", True, (255, 0, 0))
                    self._screen.blit(
                        game_over,
                        (672 / 2 - game_over.get_width() // 2,
                            704 / 2 - game_over.get_height() // 2))
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    self._running = False
                else:
                    self._screen.blit(
                        self.splash1,
                        (self.guardian.posx*32, self.guardian.posy*32))
                    self._screen.blit(
                        self.splash2,
                        (self.guardian.posx*32, self.guardian.posy*32))
                    self._screen.blit(
                        self.splash3,
                        (self.guardian.posx*32, self.guardian.posy*32))
                    self._screen.blit(
                        self.rip,
                        (self.guardian.posx*32, self.guardian.posy*32))
                    self._screen.blit(
                        self.macgyver,
                        (self.guardian.posx*32, self.guardian.posy*32))
                    guardian_position = pygame.rect.Rect(
                        self.guardian.posx*32,
                        self.guardian.posy*32,
                        32,
                        32)
                    pygame.display.update(guardian_position)
            if self.player.position == self.carte.exit:
                result_font = pygame.font.SysFont("ebrima", 55, bold=1)
                game_won = result_font.render(
                    "You've won the game !!!", True, (255, 255, 0))
                self._screen.blit(
                    game_won,
                    (672 / 2 - game_won.get_width() // 2,
                        704 / 2 - game_won.get_height() // 2))
                pygame.display.flip()
                pygame.time.delay(2000)
                self._running = False
