import pygame


class Bar():
    def __init__(self):
        self.width = 128
        self.hight = 16
        from breakout import DIM
        self.x = DIM[0]//2
        self.y = DIM[1] - 2*self.hight
        from breakout import BLK


    def update(self):
        from breakout import win
        from breakout import m_x
        self.x = m_x -self.width//2
        pygame.draw.rect(win,(120,120,180),(self.x,self.y,self.width,self.hight))


