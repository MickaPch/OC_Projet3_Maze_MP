from classes.game import Game


def main():
    """
    Fonction du jeu
    """
    # Création du jeu
    jeu = Game()
    # Initialisation et import de la carte
    jeu.on_init('ressources/map.txt')
    # Boucle de jeu
    jeu.on_execute()


if __name__ == "__main__":
    main()
