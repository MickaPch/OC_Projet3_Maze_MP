"""Game function."""
from lib.game import Game


def main():
    """
    Game function.
    """
    # Game creation
    maze_game = Game('ressources/map.txt')
    # Game loop
    maze_game.on_execute()


if __name__ == "__main__":
    main()
