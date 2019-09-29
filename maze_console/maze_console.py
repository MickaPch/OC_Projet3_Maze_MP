# Rédaction du jeu de labyrinthe en console sans pygame
import random
import copy


class Game:
    """Game loop"""
    def __init__(self):
        self._running = True

    def on_init(self, file):
        """
        Initialize the game parameters
        """
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
        # self.maze.refresh(self.player, self.guardian)

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


class Grid:
    """
    Initialisation de la carte de jeu.
    Positions 21 x 21
    """

    def __init__(self):
        self.grid = {}
        for i in range(21):
            self.grid[i] = [' ']*21
        self._len_X = len(self.grid[0])
        self._len_Y = len(self.grid)

    def initialize_grid(self, file):
        """
        Récupération de la carte du labyrinthe depuis fichier txt.
        Transformation du labyrinthe en zone de jeu.
        Création des listes forbidden_tiles et allowed_tiles.
        """
        self.forbidden_tiles = []
        self.allowed_tiles = []
        with open(file, 'r') as f:
            for y in range(21):
                maze_line = f.readline().split()
                x = 0
                while x < len(maze_line):
                    if maze_line[x] == '1':
                        self.forbidden_tiles.append((x, y))
                    elif maze_line[x] == '0':
                        self.allowed_tiles.append((x, y))
                    x += 1

        for obj in self.forbidden_tiles:
            x = obj[0]
            y = obj[1]
            self.grid[y][x] = 'X'

        return self.grid, self.forbidden_tiles, self.allowed_tiles

    def initialize_exits(self):
        """
        Initialize the entrance & exit positions
        """
        exits = []
        for position in self.allowed_tiles:
            if position[0] == 0:
                exits.append(position)
            elif position[0] == self._len_X-1:
                exits.append(position)
            elif position[1] == 0:
                exits.append(position)
            elif position[1] == self._len_Y-1:
                exits.append(position)

        self.entrance = exits.pop(random.randint(0, len(exits)-1))
        self.exit = exits[random.randint(0, len(exits)-1)]

        return self.entrance, self.exit

    def initialize_maze(self, file):
        """
        Function 2 in 1
        """
        self.initialize_grid(file)
        self.initialize_exits()


class Maze():
    """
    Affichage de la grille de jeu
    """
    def __init__(self, carte):
        """
        Fond de la carte depuis Grid (qui importe depuis fichier externe).
        """
        self.maze_grid = copy.deepcopy(carte.grid)

    def refresh(self, carte, player, guardian, needle, tube, ether, bag):
        """
        Rafraichissement de l'affichage de la grille de jeu.
        """
        self.maze_grid = copy.deepcopy(carte.grid)

        bag.control_bag(player, needle, tube, ether)
        if bag.is_needle:
            self.maze_grid[needle.posy][needle.posx] = " "
        else:
            self.maze_grid[needle.posy][needle.posx] = 'N'

        if bag.is_tube:
            self.maze_grid[tube.posy][tube.posx] = " "
        else:
            self.maze_grid[tube.posy][tube.posx] = 'T'

        if bag.is_ether:
            self.maze_grid[ether.posy][ether.posx] = " "
        else:
            self.maze_grid[ether.posy][ether.posx] = 'E'

        if bag.full:
            self.maze_grid[guardian.posy][guardian.posx] = " "
        else:
            self.maze_grid[guardian.posy][guardian.posx] = guardian.print

        self.maze_grid[player.posy][player.posx] = player.print

        return self.maze_grid

    def print_maze(self):
        """
        Boucle pour transformer le labyrinthe en str()
        pour affichage en console
        """
        maze_string = str()
        for i in range(len(self.maze_grid)):
            maze_string += " ".join(map(str, self.maze_grid[i])) + "\n"
        return maze_string

    def __str__(self):
        """Appel à la fonction print_maze() pour affichage en console"""
        return self.print_maze()


class Guardian():
    def __init__(self, carte):
        """
        Initialisation de la position du gardien
        """
        if carte.exit[0] == 0:
            self.position = (carte.exit[0] + 1, carte.exit[1])
        elif carte.exit[0] == carte._len_X - 1:
            self.position = (carte.exit[0] - 1, carte.exit[1])
        elif carte.exit[1] == 0:
            self.position = (carte.exit[0], carte.exit[1] + 1)
        elif carte.exit[1] == carte._len_Y - 1:
            self.position = (carte.exit[0], carte.exit[1] - 1)
        self.posx = self.position[0]
        self.posy = self.position[1]
        self.print = 'G'


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


def main():
    """
    Fonction du jeu
    """
    jeu = Game()            # Création du jeu
    jeu.on_init('map.txt')  # Initialisation et import de la carte
    jeu.on_execute()        # Boucle de jeu


if __name__ == "__main__":
    main()
