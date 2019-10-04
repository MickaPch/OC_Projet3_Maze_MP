import copy


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
