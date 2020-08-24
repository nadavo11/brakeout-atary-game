import pygame
import random

from bonus import Bonus

WIDTH = 64
HEIGHT = 32
progress = False


class Brick():

    def __init__(self, x, y, r, g, b):
        self.width = WIDTH
        self.hight = HEIGHT
        from breakout import DIM
        self.x = x
        self.y = y
        self.red = r
        self.green = g
        self.blue = b

        #

    def check_side(self, x, y, rad):
        self.loc = [self.x + self.width / 2, self.y + self.hight / 2]

        if self.width / 2 + rad > x - self.loc[0] > -0.5 * self.width - rad and self.hight / 2 + rad > y - \
                self.loc[1] > -self.hight / 2 - rad:
            m = self.hight / self.width
            x0 = self.x + self.width / 2
            y0 = self.y + self.hight / 2
            if x - x0 -rad < self.width / 2 and m * (x - x0) > y - y0 > -m * (x - x0):
                return 'right'
            if x - x0 +rad> self.width / 2 and m * (x - x0) < y - y0 < -m * (x - x0):
                return 'left'
            if y - y0 -rad < self.width / 2 and -m * (x - x0) < y - y0 > m * (x - x0):
                return 'down'
            if y - y0 +rad > self.width / 2 and -m * (x - x0) > y - y0 < m * (x - x0):
                return 'up'

    def destroy(self):
        from breakout import bricks
        if random.choice([True, False, False, 0, 0, 0, 0, 0, ]):
            bonus = Bonus(self.x, self.y)
            from breakout import bonuses
            bonuses.append(bonus)
        bricks.remove(self)

    def update(self):

        from breakout import win
        pygame.draw.rect(win, (self.red, self.green, self.blue), (int(self.x), int(self.y), self.width, self.hight))
