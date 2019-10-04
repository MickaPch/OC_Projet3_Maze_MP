# Rédaction du jeu de labyrinthe en console sans pygame
from classes.game import Game


def main():
    """
    Fonction du jeu
    """
    jeu = Game()            # Création du jeu
    jeu.on_init('ressources/map.txt')  # Initialisation et import de la carte
    jeu.on_execute()        # Boucle de jeu


if __name__ == "__main__":
    main()
