""" overlay to display text and other various object text """

import pygame

from .settings import *

class Ui:
    def __init__(self, observer):
        self.plays = observer.ball.get_plays
        self.pos = (0,0)
        self.maxPos = (WIDTH, HEIGHT)

        self.corner_top_right = (self.maxPos[0]-150, 0)
        self.corner_bottom_left = (0, self.maxPos[1]-150)
        self.surf = pygame.display.get_surface()

        self.bar_width = 80
        self.top_bar = pygame.Rect(0,0, self.maxPos[0], self.bar_width)
        self.bottom_bar = pygame.Rect(0, self.maxPos[1]-self.bar_width, self.maxPos[0], self.bar_width)

        self.font = pygame.font.Font("freesansbold.ttf", 20)

    def draw(self):
        pygame.draw.rect(self.surf, BAR_COLOR, self.top_bar)
        pygame.draw.rect(self.surf, BAR_COLOR, self.bottom_bar)

        if self.plays() > 0:
            self.text = self.font.render(str(f'Shakes: {self.plays()}'), True, "#000000", BAR_COLOR)
            self.text_rect = self.text.get_rect()
            self.text_rect.center = (70, 40)
            self.surf.blit(self.text, self.text_rect)

    def update(self):
        self.draw()
