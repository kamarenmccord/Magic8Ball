""" overlay to display text and other various object text """

import pygame

from .settings import *

class Ui:
    def __init__(self, observer):
        self.plays = observer.ball.get_plays
        self.ball = observer.ball
        self.check_history = self.ball.get_history
        self.pos = (0,0)
        self.maxPos = (WIDTH, HEIGHT)
        self.bar_color = BAR_COLOR
        self.show_guesses = True
        self.font = pygame.font.Font("freesansbold.ttf", 20)
        self.font_small = pygame.font.Font("freesansbold.ttf", 15)

        self.corner_top_right = (self.maxPos[0]-150, 0)
        self.corner_bottom_left = (0, self.maxPos[1]-150)
        self.surf = pygame.display.get_surface()

        # Ui Bars
        self.bar_width = 80
        self.top_bar = pygame.Rect(0,0, self.maxPos[0], self.bar_width)
        self.bottom_bar = pygame.Rect(0, self.maxPos[1]-self.bar_width, self.maxPos[0], self.bar_width)

        self.right_bar = pygame.Rect((WIDTH-350, 0), (350, HEIGHT))
        self.right_bar_border = pygame.Rect((WIDTH-350, 0), (2,HEIGHT))

        # Exit box
        box_size = 23
        box_x = 30
        box_y = self.bar_width+20
        self.exit_icon = pygame.Rect(box_x, box_y, box_size,box_size)
        self.exit_border = pygame.Rect(box_x, box_y, box_size, box_size)
        self.box_text = self.font_small.render("X", True, WHITE, RED)
        self.box_text_rect = self.box_text.get_rect()
        self.box_text_rect.topleft = (self.exit_icon.x+BORDER_SIZE+3, self.exit_icon.y+BORDER_SIZE+1)

    def draw(self):
        # underlay ui bars
        pygame.draw.rect(self.surf, BAR_COLOR, self.top_bar)
        pygame.draw.rect(self.surf, BAR_COLOR, self.bottom_bar)

        # Exit Button
        pygame.draw.rect(self.surf, RED, self.exit_icon)
        pygame.draw.rect(self.surf, WHITE, self.exit_border, BORDER_SIZE)
        self.surf.blit(self.box_text, self.box_text_rect)

        # right bar implementation
        # hidable right side "shrinks into right/slides out"
        # displays up to the last 10 guesses
        # pause game? check only for input to hide?

        if self.show_guesses:
            if self.plays() > 1:
                if self.ball.past_guess:
                    pygame.draw.rect(self.surf, BAR_COLOR, self.right_bar)
                    pygame.draw.rect(self.surf, BLACK, self.right_bar_border)
                    for index, guess in enumerate(self.ball.past_guess, 1):
                        text = self.font.render(guess, True, TEXT_COLOR, BAR_COLOR)
                        text_rect = text.get_rect()
                        text_rect.center = (WIDTH-180, HEIGHT-60-(index*50))
                        self.surf.blit(text, text_rect)

        if self.plays() > 0:
            self.text = self.font.render(str(f'Shakes: {self.plays()}'), True, TEXT_COLOR, BAR_COLOR)
            self.text_rect = self.text.get_rect()
            self.text_rect.center = (70, 40)
            self.surf.blit(self.text, self.text_rect)

        if DEBUG:
            self.debug_draw((self.ball.shake_count))


    def debug_draw(self, *args):
            for index, arg in enumerate(args):
                item_text = self.font.render(str(f"move count: {arg}"), True, TEXT_COLOR, BAR_COLOR)
                item_text_rect = item_text.get_rect()
                item_text_rect.center = (70*((index+1)*4), 40)
                self.surf.blit(item_text, item_text_rect)

    def update(self):
        self.draw()
        self.check_history()
