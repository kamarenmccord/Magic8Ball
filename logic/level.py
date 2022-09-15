""" Level container of the game """
import pygame
from random import randint

from .settings import *
from .ball import Ball

class Level:
    def __init__(self, screen):
        self.paused = False
        self.ball = Ball()
        self.screen = screen


    def update(self):
        # check for updates
        self.ball.update(self.screen)
