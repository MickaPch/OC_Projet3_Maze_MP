"""Player class. Control MacGyver moves."""
import pygame
from pygame.locals import (
    K_LEFT, K_RIGHT, K_UP, K_DOWN
)


class Player():
    """
    MacGyver
    """
    def __init__(self, game_map):
        """
        Start position
        """
        self.position = game_map.entrance
        self.previouspos = self.position
        self.posx = self.position[0]
        self.posy = self.position[1]
        self.rect = pygame.rect.Rect((self.posx*32, self.posy*32, 32, 32))

    def enter_key(self, game_map):
        """
        Control if it's possible to move or not.
        """
        key = pygame.key.get_pressed()
        if key[K_LEFT]:
            test_position = (self.posx - 1, self.posy)
            if test_position in game_map.allowed_tiles:
                self.rect.move_ip(-32, 0)
        if key[K_RIGHT]:
            test_position = (self.posx + 1, self.posy)
            if test_position in game_map.allowed_tiles:
                self.rect.move_ip(32, 0)
        if key[K_UP]:
            test_position = (self.posx, self.posy - 1)
            if test_position in game_map.allowed_tiles:
                self.rect.move_ip(0, -32)
        if key[K_DOWN]:
            test_position = (self.posx, self.posy + 1)
            if test_position in game_map.allowed_tiles:
                self.rect.move_ip(0, 32)

    def print_position(self):
        """
        Refresh the player position and save previous
        """
        self.previouspos = self.position
        self.position = (int(self.rect[0] / 32), int(self.rect[1] / 32))
        self.posx = self.position[0]
        self.posy = self.position[1]
