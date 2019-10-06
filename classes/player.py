import pygame


class Player():

    def __init__(self, carte):
        """
        Initialisation de la position de départ du joueur et de son affichage.
        """
        self.position = carte.entrance
        self.previouspos = self.position
        self.posx = self.position[0]
        self.posy = self.position[1]
        self.print = pygame.image.load(
                                    'ressources/MacGyver.png'
                                    ).convert()
        self.rect = pygame.rect.Rect((self.posx*32, self.posy*32, 32, 32))

    def enter_key(self, carte):
        """
        Contrôle si le mouvement est possible ou non.
        """
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            test_position = (self.posx - 1, self.posy)
            if test_position in carte.allowed_tiles:
                self.rect.move_ip(-32, 0)
        if key[pygame.K_RIGHT]:
            test_position = (self.posx + 1, self.posy)
            if test_position in carte.allowed_tiles:
                self.rect.move_ip(32, 0)
        if key[pygame.K_UP]:
            test_position = (self.posx, self.posy - 1)
            if test_position in carte.allowed_tiles:
                self.rect.move_ip(0, -32)
        if key[pygame.K_DOWN]:
            test_position = (self.posx, self.posy + 1)
            if test_position in carte.allowed_tiles:
                self.rect.move_ip(0, 32)

    def print_position(self):
        self.previouspos = self.position
        self.position = (int(self.rect[0] / 32), int(self.rect[1] / 32))
        self.posx = self.position[0]
        self.posy = self.position[1]
