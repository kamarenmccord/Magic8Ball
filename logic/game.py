""" main set up of the game """
import pygame

from .settings import *
from .level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()
        pygame.display.set_caption(CUSTOM_TITLE)

    def run(self):
        while True:
            self.screen.fill("#4c72fc")
            self.level.update()
            pygame.display.update()
            self.clock.tick(FPS)
