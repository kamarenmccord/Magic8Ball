""" where the magic happens """
import pygame

from settings import *

class Ball:
    def __init__(self):
        self.shape = "cicle"
        self.display = "lens"
        self.size = (64, 64)
        self.surf = pygame.rect.Rect(64, 64)
        
        self.cooldown = 0
        self.maxcooldown = 300


    def draw(self):
        pygame.draw.circle(self.surf, "#000", (WIDTH//2, HEIGHT//2), 200)

    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1
