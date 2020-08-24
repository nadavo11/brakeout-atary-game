import math

import pygame

from ball import Ball
from bar import Bar
from brick import Brick, WIDTH, HEIGHT

DIM = [1280 , 600]
pygame.init()

clock = pygame.time.Clock()
clock.tick(10)
BLK = 4
run = True
mode = 'game'
win = pygame.display.set_mode((DIM[0],DIM[1]))
pygame.display.set_caption("My Game")
color = [255, 50, 0]

###################################################################################################################################
#                                                   RUN LOOP!
b = Bar()
ball = Ball()
bricks = []
bonuses =[]
brick_counter = 0
for r in range((DIM[0])//64):
    for h in range(6):

        red = 240-(42*h)
        blue = 240 - red
        green =50
        h = h * HEIGHT
        i = r * WIDTH
        brick = Brick(i,h,red,green, blue)
        bricks.append(brick)
def progress(b):
    for br in bricks:
        br.y += HEIGHT
    for r in range((DIM[0]) // 64):
        h = 0
        i = r * WIDTH
        rd = abs(math.cos(0.1*b)*250)
        gr = abs(math.sin(0.154*b)*250)
        bl = abs(math.sin(0.21253*b)*250)
        brick = Brick(i, h, rd, gr,bl)
        bricks.append(brick)

    ball. score+=1
while run:
    m_x, m_y = pygame.mouse.get_pos()
    if mode == 'game':
        pygame.time.delay(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        win.fill((0, 0, 0, 5))
        b.update()
        for i in bricks:
            i.update()
        for i in bonuses:
            i.update()
        ball.update()
        if ball.score % 9 ==0:
            progress(brick_counter)
            brick_counter +=1
        if ball.score %14 ==0:
            ball.superball == False
            progress(brick_counter)
            brick_counter +=1
            progress(brick_counter)
            brick_counter+=1
            progresss = False
        pygame.display.update()

#TERMINATE PROGRAM
pygame.quit()
