import random


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
