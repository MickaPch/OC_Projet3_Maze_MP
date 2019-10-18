"""Maze class. Control display of the game."""
import copy
import pygame
from lib.guardian import Guardian
from lib.player import Player
from lib.item import Item
from lib.bag import Bag


class Maze():
    """
    Manages the display of the game grid.
    """
    def __init__(self, game_map, screen):
        """
        Maze grid, from Grid class which import external file.
        """
        self.maze_grid = copy.deepcopy(game_map.grid)
        self.screen = screen
        self.guardian = Guardian(game_map)
        self.player = Player(game_map)
        self.needle = Item(game_map, self.guardian)
        self.tube = Item(game_map, self.guardian)
        self.ether = Item(game_map, self.guardian)
        self.bag = Bag()
        self.objects_list = [
            game_map,
            self.player,
            self.guardian,
            self.needle,
            self.tube,
            self.ether,
            self.bag
            ]
        self.item_1 = (6, 21)
        self.item_2 = (8, 21)
        self.item_3 = (10, 21)
        self.bag_items = [self.item_1, self.item_2, self.item_3]
        self.floor = None
        self.wall = None
        self.macgyver = None
        self.guard = None
        self.exit_tile = None
        self.exit_open = None
        self.needle_img = None
        self.tube_img = None
        self.ether_img = None
        self.empty_bag = None
        self.item_bag = None
        self.seringue_img = None
        self.splash1 = None
        self.splash2 = None
        self.splash3 = None
        self.rip = None
        self.bag_font = None
        self.text_full = None
        self._running = True
        self.list_guardian_animation = []

    def load_image(self, name):
        """
        Load pygame image stored in ressources/ by name only
        """
        path = 'ressources/' + name + '.png'
        return pygame.image.load(path)

    def blit_item(
            self, item_to_blit, position,
            centerx=0, centery=0, convert=True
    ):
        """
        Blit an image defined by load_image at this position
        For the update of the position, return Rect object
        """
        posx = position[0]
        posy = position[1]
        if convert:
            convx = convy = 32
        else:
            convx = convy = 1
        self.screen.blit(
            item_to_blit,
            (posx*convx + centerx, posy*convy + centery)
        )
        rect_item = pygame.rect.Rect(
            int(position[0])*convx,
            int(position[1])*convy,
            32,
            32
        )
        return rect_item

    def init_map(self, game_map):
        """
        Initialize the pygame maze.
        """
        # Import images
        self.floor = self.load_image('floor').convert()
        self.wall = self.load_image('rock_block').convert()
        self.macgyver = self.load_image('MacGyver2').convert_alpha()
        self.guard = self.load_image('Gardien2').convert_alpha()
        self.exit_tile = self.load_image('door_closed').convert()
        self.exit_open = self.load_image('door_open').convert_alpha()
        self.needle_img = self.load_image('aiguille2').convert_alpha()
        self.tube_img = self.load_image('tuyau2').convert_alpha()
        self.ether_img = self.load_image('ether3').convert_alpha()
        self.empty_bag = self.load_image('item_empty').convert_alpha()
        self.item_bag = self.load_image('item_pick').convert_alpha()
        self.seringue_img = self.load_image('seringue2').convert_alpha()
        self.splash1 = self.load_image('splash1').convert_alpha()
        self.splash2 = self.load_image('splash2').convert_alpha()
        self.splash3 = self.load_image('splash3').convert_alpha()
        self.rip = self.load_image('rip').convert_alpha()

        # Import font
        font = pygame.font.SysFont("ebrima", 22)
        self.bag_font = font.render("Bag content :", True, (255, 255, 255))
        self.text_full = font.render("=", True, (255, 255, 255))

        # Initialize all positions
        for allowed_position in game_map.allowed_tiles:
            self.blit_item(self.floor, allowed_position)
        for forbidden_position in game_map.forbidden_tiles:
            self.blit_item(self.wall, forbidden_position)
        list_init_blit = [
            [self.macgyver, self.player.position, 4],
            [self.guard, self.guardian.position, 2],
            [self.exit_tile, game_map.exit],
            [self.needle_img, self.needle.position],
            [self.ether_img, self.ether.position, 6],
            [self.tube_img, self.tube.position, 2],
            [self.bag_font, (1, 21)],
            [self.empty_bag, self.item_1],
            [self.empty_bag, self.item_2],
            [self.empty_bag, self.item_3]
        ]
        for item_to_blit in list_init_blit:
            self.blit_item(*item_to_blit)

        pygame.display.flip()

        self._running = True

    def death_animation(self):
        """Animate images at guardian position"""
        self.list_guardian_animation = [
            self.floor,
            self.splash1,
            self.splash2,
            self.splash3,
            self.rip
        ]
        for element in self.list_guardian_animation:
            guardian_position = self.blit_item(element, self.guardian.position)
            pygame.display.update(guardian_position)
            pygame.time.delay(300)

    def on_render(self, game_map):
        """
        Refresh the tiles of the maze
        """
        # Rects to actualize
        dirty_rects = []
        # Erase player previous position
        previous_position = self.blit_item(self.floor, self.player.previouspos)
        dirty_rects.append(previous_position)
        # Add actual player position
        current_position = self.blit_item(
            self.macgyver, self.player.position, 4)
        dirty_rects.append(current_position)
        # Add item if picked
        self.bag.control_bag(self.player, self.needle, self.tube, self.ether)
        if self.bag.needle_picked == 1:
            position = self.bag_items.pop(0)
            needle_position = self.blit_item(self.needle_img, position)
            self.blit_item(self.item_bag, position)
            dirty_rects.append(needle_position)
            self.bag.needle_picked += 1
        elif self.bag.tube_picked == 1:
            position = self.bag_items.pop(0)
            tube_position = self.blit_item(self.tube_img, position, 2)
            self.blit_item(self.item_bag, position)
            dirty_rects.append(tube_position)
            self.bag.tube_picked += 1
        elif self.bag.ether_picked == 1:
            position = self.bag_items.pop(0)
            ether_position = self.blit_item(self.ether_img, position, 6)
            self.blit_item(self.item_bag, position)
            dirty_rects.append(ether_position)
            self.bag.ether_picked += 1
        pygame.display.update(dirty_rects)
        if self.bag.full_items == 1:
            sign_position = self.blit_item(self.text_full, (12, 21))
            pygame.display.update(sign_position)
            sering_position = self.blit_item(self.seringue_img, (14, 21))
            pygame.display.update(sering_position)

            # Death animation
            self.death_animation()

            exit_tile = self.blit_item(self.floor, game_map.exit)
            self.blit_item(self.exit_open, game_map.exit)
            pygame.display.update(exit_tile)
            self.bag.full_items += 1

    def game_over(self):
        """
        Display Game Over message
        """
        result_font = pygame.font.SysFont("ebrima", 60, bold=1)
        game_over = result_font.render(
            "Game Over !!!", True, (255, 0, 0))
        game_over_position = (
            672 / 2 - game_over.get_width() // 2,
            704 / 2 - game_over.get_height() // 2
        )
        self.blit_item(game_over, game_over_position, convert=False)
        pygame.display.flip()

    def win_game(self):
        """
        Display Win message
        """
        result_font = pygame.font.SysFont("ebrima", 55, bold=1)
        game_won = result_font.render(
            "You won the game !!!", True, (255, 255, 0))
        game_won_position = (
            672 / 2 - game_won.get_width() // 2,
            704 / 2 - game_won.get_height() // 2
        )
        self.blit_item(game_won, game_won_position, convert=False)
        pygame.display.flip()
