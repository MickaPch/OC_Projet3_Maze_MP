# Rédaction du jeu de labyrinthe en console sans pygame
import random
import copy


class Game:
    """Game loop"""
    def __init__(self):
        self._running = True

    def on_init(self, file):
        self.carte = Grid()
        self.carte.initialize_maze(file)
        self.maze = Maze(self.carte)
        self.guardian = Guardian(self.carte)
        self.player = Player(self.carte)
        self._running = True

    def move(self):
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
        while self._running:
            self.maze.refresh(self.carte, self.player, self.guardian)
            print(self.maze)
            self.move()
            self.maze.refresh(self.carte, self.player, self.guardian)
            if self.player.position == self.guardian.position:
                print(self.maze)
                print('Game Over')
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
        self.initialize_grid(file)
        self.initialize_exits()


class Maze():

    def __init__(self, carte):
        self.maze_grid = copy.deepcopy(carte.grid)

    def refresh(self, carte, player, guardian):
        self.maze_grid = copy.deepcopy(carte.grid)
        player_posx = player.position[0]
        player_posy = player.position[1]
        self.maze_grid[player_posy][player_posx] = 'P'
        guardian_posx = guardian.position[0]
        guardian_posy = guardian.position[1]
        self.maze_grid[guardian_posy][guardian_posx] = 'G'
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


class Guardian:
    def __init__(self, maze):
        if maze.exit[0] == 0:
            self.position = (maze.exit[0] + 1, maze.exit[1])
        if maze.exit[0] == maze._len_X - 1:
            self.position = (maze.exit[0] - 1, maze.exit[1])
        if maze.exit[1] == 0:
            self.position = (maze.exit[0], maze.exit[1] + 1)
        if maze.exit[1] == maze._len_Y - 1:
            self.position = (maze.exit[0], maze.exit[1] - 1)


class Player:

    def __init__(self, carte):
        self.position = carte.entrance

    def on_move(self, keyboard_input, carte):
        if keyboard_input == 8:
            test_position = (self.position[0], self.position[1] - 1)
            if test_position in carte.allowed_tiles:
                self.position = test_position
        elif keyboard_input == 6:
            test_position = (self.position[0] + 1, self.position[1])
            if test_position in carte.allowed_tiles:
                self.position = test_position
        elif keyboard_input == 5:
            test_position = (self.position[0], self.position[1] + 1)
            if test_position in carte.allowed_tiles:
                self.position = test_position
        elif keyboard_input == 4:
            test_position = (self.position[0] - 1, self.position[1])
            if test_position in carte.allowed_tiles:
                self.position = test_position


def main():

    jeu = Game()
    jeu.on_init('map.txt')
    jeu.on_execute()


if __name__ == "__main__":
    main()
