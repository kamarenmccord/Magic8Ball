""" Level container of the game """
import pygame
import sys

from .settings import *
from .ball import Ball

class Level:
    def __init__(self):
        self.paused = False
        self.ball = Ball()

    def quit(self):
        pygame.quit()
        sys.exit()

    def shake_ball(self):
        if self.ball.cooldown <= 0:
            self.ball.shake()

    def update(self):
        # check for updates
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.quit()
                if event.key == pygame.K_s:
                    self.shake_ball()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.shake_ball()
        self.ball.update()
