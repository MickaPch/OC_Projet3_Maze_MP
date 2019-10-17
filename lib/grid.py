import random


class Grid:
    """
    Initialization of maze map.
    21 x 21
    """

    def __init__(self):
        """
        Initialization of the grid.
        Not anymore used in pygame version.
        """
        self.grid = {}
        for i in range(21):
            self.grid[i] = [' ']*21
        self._len_X = len(self.grid[0])
        self._len_Y = len(self.grid)

    def initialize_maze(self, file):
        """
        Import maze map from txt file.
        Creation of forbidden_tiles and allowed_tiles lists.
        Grid creation not anymore used in pygame version.
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

        for position in self.allowed_tiles:
            if position[1] == 0:
                self.exit = position                
            elif position[1] == self._len_Y-1:
                self.entrance = position

        return self.grid, self.forbidden_tiles, self.allowed_tiles, self.entrance, self.exit
