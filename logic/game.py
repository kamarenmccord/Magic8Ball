""" main set up of the game """
import pygame
import sys

from .settings import *
from .level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level(self.screen)
        pygame.display.set_caption(CUSTOM_TITLE)


    def quit(self):
        pygame.quit()
        sys.exit()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.quit()
            self.screen.fill("#4c72fc")
            self.level.update()
            pygame.display.update()
            self.clock.tick(FPS)
