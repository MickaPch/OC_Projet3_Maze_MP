"""Game class, control the game loop"""
import pygame
from pygame.locals import (
    FULLSCREEN, QUIT, KEYDOWN, K_ESCAPE
)
from lib.grid import Grid
from lib.maze import Maze


class Game:
    """Game loop"""
    def __init__(self, file):
        """
        Initial parameters
        """
        pygame.init()
        self._running = True
        self.width = 672
        self.height = 704
        self.size = (self.width, self.height)
        self.game_map = Grid()
        self.game_map.initialize_maze(file)
        self._screen = pygame.display.set_mode(
            self.size, FULLSCREEN
        )
        self.maze = Maze(self.game_map, self._screen)

    def on_event(self, event):
        """
        Stop the game if quit or escape.
        Return keydown
        """
        if event.type == QUIT:
            self._running = False
            return
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            self._running = False
            return
        elif event.type == KEYDOWN:
            return event.key

    def on_execute(self):
        """Game"""

        self.maze.init_map(self.game_map)
        while self._running:
            pygame.time.delay(120)
            for event in pygame.event.get():
                if (event.type == QUIT
                        or (event.type == KEYDOWN
                            and event.key == K_ESCAPE)):
                    self._running = False
            self.maze.player.enter_key(self.game_map)
            self.maze.player.print_position()
            self.maze.on_render(self.game_map)

            if self.maze.player.position == self.maze.guardian.position:
                if not self.maze.bag.full:
                    self.maze.death_animation()
                    guardian_position = self.maze.blit_item(
                        self.maze.guard, self.maze.guardian.position)
                    pygame.display.update(guardian_position)
                    self.maze.game_over()
                    pygame.time.delay(2000)
                    self._running = False
                else:
                    for element in self.maze.list_guardian_animation:
                        self.maze.blit_item(
                            element, self.maze.guardian.position)
                    guardian_position = self.maze.blit_item(
                        self.maze.macgyver, self.maze.guardian.position)
                    pygame.display.update(guardian_position)
            if self.maze.player.position == self.game_map.exit:
                self.maze.win_game()
                pygame.time.delay(2000)
                self._running = False
