""" where the magic happens """
import pygame
from random import randint

from .settings import *

class Ball:
    def __init__(self):

        # stats
        self.score = 0
        self.standard_ball = True
        self.shaken = False

        # cool downs
        self.cooldown = 0
        self.max_cooldown = 50

        # positioning
        self.x = WIDTH//2
        self.y = HEIGHT//2

        #Ui
        self.surf = pygame.display.get_surface()
        self.font = pygame.font.Font("freesansbold.ttf", 32)

        self.answer = "Press 'S' to shake"
        self.answer_index = [0,0]

        self.text = self.font.render(self.answer, True, "#000000", COLOR_BACKGROUND)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (WIDTH//2, HEIGHT//2+250)
        self.results = [
            ["It is Certain", "It is decidedly so", "without a doubt", "yes definitely", "you may rely on it"],
            ["As I see it, yes", "most likely", "outlook good", "yes", "signs point to yes"],
            ["Reply hazy, try again", "Ask again later", "better not tell you now", "cannot predict now", "concentrate and ask again"],
            ["Don't count on it", "My reply is NO", "My sources say no", "outlook not so good", "very doubtful"]
            ]

    def roll(self):
        return (randint(0, 3), randint(0,4))

    def get_plays(self):
        return self.score

    def draw(self):
        centerY = HEIGHT//2
        if self.standard_ball:
            # the standard ball will have the 8 written on it
            offset = -50
            textoffset = 27
            pygame.draw.circle(self.surf, "#1a1a1a", (self.x, centerY), 175)
            pygame.draw.circle(self.surf, "#f2f2f2", (self.x+offset, centerY+offset), 80)
            pygame.draw.circle(self.surf, "#0d0d0d", (self.x+offset-18, centerY+offset+textoffset), 30, 7)
            pygame.draw.circle(self.surf, "#0d0d0d", (self.x+offset-8, centerY+offset-textoffset), 30, 7)

    def readout(self):
        self.surf.blit(self.text, self.text_rect)

    def shake(self):
        text_height_offset = 250
        self.answer_index = self.roll()
        self.answer = self.results[self.answer_index[0]][self.answer_index[1]]
        self.text = self.font.render(self.answer, True, "#000000", COLOR_BACKGROUND)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x, self.y+text_height_offset)

    def do_action(self):
        # set stats
        self.cooldown = self.max_cooldown
        self.shaken = True
        self.score += 1
        self.shake()

    def checkinput(self):
        if self.cooldown <= 0:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:
                self.do_action()

    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1
        self.draw()
        self.readout()
        self.checkinput()
