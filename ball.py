import pygame
import math

score = 0


class Ball():
    def __init__(self):
        self.rad = 8
        from breakout import DIM
        self.x = float(DIM[0] // 2)
        self.y = float(DIM[1] // 2)
        self.velx = 2.0
        self.vely = 2.0
        self.score = 1
        self.superball = False

    def die(self):
        from breakout import DIM
        if self.y >= DIM[1]:
            pygame.quit()

    def figure_dir(self):
        from breakout import b
        thetamax = (-15 * math.pi / 16)
        thetamin = -math.pi / 16
        theta = math.atan2(self.vely, self.velx)
        vel = math.hypot(self.vely, self.velx)
        pos = (self.x - b.x) / b.width
        theta = -math.pi * (1 - pos)
        if theta <= thetamax:
            theta = thetamax
        if theta >= thetamin:
            theta = thetamin
        print(pos)
        self.score += 1
        vel += 1 / (2 * self.score)
        self.velx = vel * math.cos(theta)
        self.vely = vel * math.sin(theta)

        from breakout import BLK

    def bounce(self, rad):
        from breakout import bricks
        from breakout import b
        from breakout import DIM
        if self.x +rad > DIM[0]:        # ****************WALLS BOUNCE
            self.velx *= -1
            self.x = DIM[0] -rad
        if self.x -rad < 0:
            self.x = rad +rad+4
            self.velx *= -1
        if self.y <= 0:  # ****************ROOF BOUNCE
            self.vely *= -1
        if self.y +rad >= b.y:  # ****************BAR BOUNCE
            if self.x - 4 >= b.x and self.x <= (b.x + b.width + 12):
                self.vely *= -1
                self.figure_dir()

        for brick in bricks:  # *****************BRICK BOUNCE
            side = brick.check_side(self.x, self.y, rad)
            if side == 'right' or side == 'left':
                if not self.superball:
                    self.velx *= -1
                brick.destroy()
            # break
            if side == 'up' or side == 'down':
                if not self.superball:
                    self.y -= self.vely
                    self.vely *= -1

                brick.destroy()

    def move(self):
        self.x += self.velx
        self.y += self.vely

    def update(self):
        self.bounce(self.rad)
        self.move()
        self.die()
        from breakout import win
        pygame.draw.circle(win, (200, 200, 200), (int(self.x - self.rad), int(self.y - self.rad)), self.rad)
    # pygame.draw.rect(win, (180, 120, 120), (self.x, self.y, self.width, self.hight))
