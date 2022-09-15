""" where the magic happens """
import pygame
from random import randint

from .settings import *

class Ball:
    def __init__(self):
        self.standard_ball = True
        self.surf = pygame.display.get_surface()
        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.answer = "Press 'S' to shake"
        self.text = self.font.render(self.answer, True, "#000000", COLOR_BACKGROUND)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (WIDTH//2, HEIGHT//2+250)
        self.shaken = False
        self.display = "lens"
        self.random_answer = [0,0]
        self.results = [
            ["It is Certain", "It is decidedly so", "without a doubt", "yes definitely", "you may rely on it"],
            ["As I see it, yes", "most likely", "outlook good", "yes", "signs point to yes"],
            ["Reply hazy, try again", "Ask again later", "better not tell you now", "cannot predict now", "concentrate and ask again"],
            ["Don't count on it", "My reply is NO", "My sources say no", "outlook not so good", "very doubtful"]
            ]

        self.cooldown = 0
        self.max_cooldown = 50

    def roll(self):
        return (randint(0, 3), randint(0,4))

    def draw(self):
        centerX = WIDTH//2
        centerY = HEIGHT//2
        if self.standard_ball:
            # the standard ball will have the 8 written on it
            offset = -50
            textoffset = 27
            pygame.draw.circle(self.surf, "#1a1a1a", (centerX, centerY), 175)
            pygame.draw.circle(self.surf, "#f2f2f2", (centerX+offset, centerY+offset), 80)
            pygame.draw.circle(self.surf, "#0d0d0d", (centerX+offset-18, centerY+offset+textoffset), 30, 7)
            pygame.draw.circle(self.surf, "#0d0d0d", (centerX+offset-8, centerY+offset-textoffset), 30, 7)

    def readout(self):
        self.surf.blit(self.text, self.text_rect)

    def shake(self):
        self.random_answer = self.roll()
        self.shaken = True
        self.answer = self.results[self.random_answer[0]][self.random_answer[1]]
        self.cooldown = self.max_cooldown
        self.text = self.font.render(self.answer, True, "#000000", COLOR_BACKGROUND)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (WIDTH//2, HEIGHT//2+250)

    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1
        self.draw()
        self.readout()
