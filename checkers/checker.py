from .constants import SQUARE_SIZE, CROWN, BLACK_CHECKER, WHITE_CHECKER, WHITE
import pygame


class Checker:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col
        self.y = SQUARE_SIZE * self.row

    def make_king(self):
        self.king = True

    def draw(self, win):
        if self.color == WHITE:
            win.blit(WHITE_CHECKER, (self.x, self.y))
        else:
            win.blit(BLACK_CHECKER, (self.x, self.y))

        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)
