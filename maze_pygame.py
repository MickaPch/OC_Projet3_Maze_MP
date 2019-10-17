from lib.game import Game


def main():
    """
    Fonction du jeu
    """
    # Création du jeu
    maze_game = Game()
    # Initialisation et import de la carte
    maze_game.on_init('ressources/map.txt')
    # Boucle de jeu
    maze_game.on_execute()


if __name__ == "__main__":
    main()
