# Rédaction du jeu de labyrinthe en console sans pygame
import random


class Grid:
    """
    Initialisation de la carte de jeu.
    Positions 20 x 20
    """

    def __init__(self):
        self.grid = {}
        for i in range(21):
            self.grid[i] = ['.']*21


class Wall:
    """Impassable wall"""

    def __init__(self, x, y):
        self._posx = x
        self._posy = y
        self.position = (self._posx, self._posy)


class Maze():

    def __init__(self, carte, file):
        self._len_X = len(carte.grid[0])
        self._len_Y = len(carte.grid)

        self._entrance = (0, 10)
        self._exit = (20, 10)

    def initialize_maze(self, carte, file):
        lab_grid = carte.grid
        walls = []
        with open(file, 'r') as f:
            for y in range(21):
                maze_line = f.readline().split()
                x = 0
                while x < len(maze_line):
                    if maze_line[x] == '1':
                        walls.append((x, y))
                    x += 1

        for obj in walls:
            x = obj[0]
            y = obj[1]
            lab_grid[y][x] = 'X'

        return lab_grid

    def on_init(self, carte, file):
        
        self.maze_grid = initialize_maze(self, carte, file)

    def print_maze(self):
        """
        Boucle pour transformer le labyrinthe en str()
        pour affichage en console
        """
        maze_string = str()
        for i in range(self._len_Y):
            maze_string += " ".join(map(str, self.maze_grid[i])) + "\n"
        return maze_string

    def __str__(self):
        """Appel à la fonction print_maze() pour affichage en console"""
        return self.print_maze()


def main():

    carte = Grid()
    maze = Maze(carte, 'map.txt')
    print(maze)
    # print(maze.initialize_maze())
    # print(maze._exit)


if __name__ == "__main__":
    main()
