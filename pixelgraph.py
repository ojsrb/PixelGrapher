import time

import pygame
import sys
import math

#Config

res = 0
fr = 10

#Animation variables

counter = 1
continuous = 1
backandforth = 1
change = 1

dots = []

screen = 0

radius = 0

clock = 0

def set(x, y, val):
    global dots, backandforth, counter, continuous, change, res, fr
    try:
        dots[x][y] = val
    except:
        pass

def get(x, y):
    global dots, backandforth, counter, continuous, change, res, fr
    return dots[x][y]

def clear():
    global dots, backandforth, counter, continuous, change, res, fr
    for i in range(0, res):
        for j in range(res):
            dots[i][j] = -1

def vertical(x, min=0, max=200):
    global dots, backandforth, counter, continuous, change, res, fr
    for i in range(min, max):
        set(x, i, 1)

def horizontal(y, min=0, max=200):
    global dots, backandforth, counter, continuous, change, res, fr
    for i in range(min, max):
        set(i, y, 1)

def line(slope, intercept=0, color=1, min=0, max=200):
    global dots, backandforth, counter, continuous, change, res, fr
    for i in range(min, max):
        y = res - math.floor(i * round(slope, 4)) - intercept
        if y < 0:
            return
        set(i, y, color)

def rect(x, y, w, h, color=1):
    global dots, backandforth, counter, continuous, change, res, fr
    for i in range(x, x+w):
        vertical(i, min=y, max=y+h)

def init(resolution, width, framerate):
    global dots, backandforth, counter, continuous, change, res, fr, screen, radius, clock

    res = resolution
    fr = framerate

    w = width

    pygame.init()
    window = pygame.display.set_mode((w, w), pygame.SCALED)
    pygame.display.set_caption("PixelGrapher")

    screen = pygame.display.get_surface()

    clock = pygame.time.Clock()

    dots = []

    radius = (w // res) / 2

    for i in range(res):
        newrow = []
        for j in range(res):
            newrow.append(-1)
        dots.append(newrow)


def update():
    global dots, backandforth, counter, continuous, change, res, fr, screen, clock, radius

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for i in range(res):
        row = dots[i]
        for j in range(res):
            if row[j] < 0:
                pygame.draw.circle(screen, (0, 0, 0), [i * radius * 2 + radius, j * radius * 2 + radius], radius)
            else:
                color = (255, 255, 255)
                if row[j] == 1:
                    color = (255, 255, 255)
                elif row[j] == 2:
                    color = (255, 50, 50)
                elif row[j] == 3:
                    color = (255, 255, 50)
                elif row[j] == 4:
                    color = (50, 255, 50)
                elif row[j] == 5:
                    color = (50, 255, 255)
                elif row[j] == 6:
                    color = (50, 50, 255)
                pygame.draw.circle(screen, color, [i * radius * 2 + radius, j * radius * 2 + radius], radius)

    pygame.display.update()

    # END RENDER

    counter += 1

    if counter > res:
        counter = 1

    continuous += 1

    backandforth += change

    if backandforth > res:
        change = -1
        backandforth = res
    elif backandforth < 1:
        change = 1
        backandforth = 1

    clock.tick(fr)

    screen.fill((25, 25, 25))
