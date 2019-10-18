"""Grid class. Import the grid from an external file."""


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
        self._len_x = len(self.grid[0])
        self._len_y = len(self.grid)
        self.forbidden_tiles = []
        self.allowed_tiles = []
        self.exit = None
        self.entrance = None

    def initialize_maze(self, file):
        """
        Import maze map from txt file.
        Creation of forbidden_tiles and allowed_tiles lists.
        Grid creation not anymore used in pygame version.
        """
        with open(file, 'r') as txt_file:
            for y_pos in range(21):
                maze_line = txt_file.readline().split()
                x_pos = 0
                while x_pos < len(maze_line):
                    if maze_line[x_pos] == '1':
                        self.forbidden_tiles.append((x_pos, y_pos))
                    elif maze_line[x_pos] == '0':
                        self.allowed_tiles.append((x_pos, y_pos))
                    x_pos += 1

        for obj in self.forbidden_tiles:
            x_pos = obj[0]
            y_pos = obj[1]
            self.grid[y_pos][x_pos] = 'X'

        for position in self.allowed_tiles:
            if position[1] == 0:
                self.exit = position
            elif position[1] == self._len_y-1:
                self.entrance = position

        return (
            self.grid,
            self.forbidden_tiles,
            self.allowed_tiles,
            self.entrance,
            self.exit
        )
