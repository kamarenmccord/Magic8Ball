""" Level container of the game """
import pygame
from random import randint

from .settings import *

class Level:
    def __init__(self):
        self.paused = False


    def update(self):
        # check for updates
        pass