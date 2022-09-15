""" where the magic happens """
import pygame

from .settings import *

class Ball:
    def __init__(self):
        self.standard_ball = True
        self.shaken = False
        self.display = "lens"
        self.size = (64, 64)
        self.surf = pygame.Surface((64*3, 64*3))
        
        self.cooldown = 0
        self.maxcooldown = 300


    def draw(self, screen):
        centerX = WIDTH//2
        centerY = HEIGHT//2
        if self.standard_ball:
            offset = -50
            textoffset = 27
            pygame.draw.circle(screen, "#1a1a1a", (centerX, centerY), 175)
            pygame.draw.circle(screen, "#f2f2f2", (centerX+offset, centerY+offset), 80)
            pygame.draw.circle(screen, "#0d0d0d", (centerX+offset-18, centerY+offset+textoffset), 30, 7)
            pygame.draw.circle(screen, "#0d0d0d", (centerX+offset-8, centerY+offset-textoffset), 30, 7)

    def readout(self, screen):
        if self.shaken:
            # draw last result
            pass
        else:
            # advise to shake the ball
            pass

    def update(self, screen):
        if self.cooldown > 0:
            self.cooldown -= 1
        self.draw(screen)
        self.readout(screen)
