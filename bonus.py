import random

import pygame


class Bonus():

    def __init__(self, x, y):
        self.width = 32
        self.hight = 32
        from breakout import DIM
        self.x = x
        self.y = y
        self.velx = random.randint(-2, 2)
        self.vely = random.randint(1, 2)
        self.type =  random.choice(['superball', 'regball','smallball','bigball','bigbar','smallbar','progress'])

    def bounce(self, rad):
        from breakout import bricks
        from breakout import b
        from breakout import DIM
        if self.x >= DIM[0] or self.x <= 0:  # ****************WALLS BOUNCE
            self.velx *= -1

    def catch(self):
        from breakout import b
        if self.x - 4 >= b.x and self.x <= (b.x + b.width + 12) and b.y == self.y:
            self.execute()
            from breakout import bonuses
            bonuses.remove(self)
    def execute(self):
        from breakout import progress
        from breakout import ball
        from breakout import b
        if self.type == 'superball':
            ball.superball = True
        if self.type == 'regball':
            ball.superball = False
        if self.type == 'smallball':
            ball.rad = ball.rad//2
        if self.type == 'bigball':
            ball.rad *=2
        if self.type == 'bigbar':
            b. width += 80
        if self.type == 'smallbar':
            if b.width> 90:
                b.width -= 70
        if self.type == 'progress':
          pass

    def moove(self):
        self.x += self.velx
        self.y += self.vely

    def update(self):
        self.bounce(self.width)
        self.moove()
        self.catch()
        #self.die()
        from breakout import win
        pygame.draw.rect(win, (200, 200, 200),
                         (int(self.x - self.width / 2), int(self.y - self.width / 2), self.hight, self.width))


    # pygame.draw.rect(win, (180, 120, 120), (self.x, self.y, self.width, self.hight))
