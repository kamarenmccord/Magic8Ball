""" where the magic happens """
import pygame

from .settings import *

class Ball:
    def __init__(self):
        self.standard_ball = True
        self.display = "lens"
        self.size = (64, 64)
        self.surf = pygame.Surface((64*3, 64*3))
        
        self.cooldown = 0
        self.maxcooldown = 300


    def draw(self, screen):
        if self.standard_ball:
            offset = -50
            textoffset = 27
            pygame.draw.circle(screen, "#000000", (WIDTH//2, HEIGHT//2), 175)
            pygame.draw.circle(screen, "#FFFFFF", (WIDTH//2+offset, HEIGHT//2+offset), 80)
            pygame.draw.circle(screen, "#000000", (WIDTH//2+offset-18, HEIGHT//2+offset+textoffset), 30, 7)
            pygame.draw.circle(screen, "#000000", (WIDTH//2+offset-8, HEIGHT//2+offset-textoffset), 30, 7)

    def update(self, screen):
        if self.cooldown > 0:
            self.cooldown -= 1
        self.draw(screen)
