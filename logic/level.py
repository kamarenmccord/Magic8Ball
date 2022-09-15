""" Level container of the game """
import pygame
import sys

from .settings import *
from .ball import Ball
from .ui import Ui

class Level:
    def __init__(self):
        self.light_mode = LIGHT_MODE
        self.ball = Ball()
        self.overlay = Ui(self)

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        # check for updates
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.quit()

        self.ball.update()
        self.overlay.update()
