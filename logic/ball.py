""" where the magic happens """
import pygame
from random import randint

from .settings import *

class Ball:
    def __init__(self):

        # stats
        self.score = 0
        self.standard_ball = True
        self.past_guess = []
        self.background_color = COLOR_BACKGROUND

        # cool downs
        self.cooldown = 0
        self.max_cooldown = 50

        # positioning
        self.x = WIDTH//2
        self.y = HEIGHT//2
        self.direction = -1  # Defualt direction is up
        self.speed = 3

        # boundries
        self.shaken = False
        self.shaking = False
        shake_offset = 40
        self.Y_LOWER = self.y-shake_offset
        self.Y_UPPER = self.y+shake_offset
        self.shake_count = 0
        self.shake_stop_count = 3*3  # 3 * n-cycles

        #Ui
        self.surf = pygame.display.get_surface()
        self.font = pygame.font.Font("freesansbold.ttf", 32)

        self.answer = "Press 'S' to shake"
        self.answer_index = [0,0]

        self.text = self.font.render(self.answer, True, TEXT_COLOR, self.background_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (WIDTH//2, HEIGHT//2+250)
        self.results = RESULTS

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
            pygame.draw.circle(self.surf, "#1a1a1a", (self.x, self.y), 175)
            pygame.draw.circle(self.surf, "#f2f2f2", (self.x+offset, self.y+offset), 80)
            pygame.draw.circle(self.surf, "#0d0d0d", (self.x+offset-18, self.y+offset+textoffset), 30, 7)
            pygame.draw.circle(self.surf, "#0d0d0d", (self.x+offset-8, self.y+offset-textoffset), 30, 7)
        
        self.surf.blit(self.text, self.text_rect)

    def shake(self):
        text_height_offset = 250

        self.answer_index = self.roll()
        self.answer = self.results[self.answer_index[0]][self.answer_index[1]]
        self.past_guess.append(self.answer)
        self.text = self.font.render(self.answer, True, TEXT_COLOR, self.background_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x, self.y+text_height_offset)

    def move(self):
        # modify the specific y Coordinate
        self.y += self.speed * self.direction

        # check for boundry and set direction
        if self.direction < 0:
            if self.y < self.Y_LOWER:
                self.direction *= -1
                self.shake_count += 1
        else:
            if self.y > self.Y_UPPER:
                self.direction *= -1
                self.shake_count += 1
        if self.direction < 0 and self.y == HEIGHT//2:
            self.shake_count += 1

        if self.shake_count >= self.shake_stop_count:
            self.shake_count = 0
            self.shaking = False
            # re-roll the answer var and set its respective stats
            self.shake()

    def do_action(self):
        # set stats
        self.cooldown = self.max_cooldown
        self.shaken = True
        self.score += 1
        self.shaking = True

    def checkinput(self):
        if self.cooldown <= 0 and self.shaking == False:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:
                self.do_action()

    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1
        if self.shaking == True:
            self.move()
        self.draw()
        self.checkinput()
