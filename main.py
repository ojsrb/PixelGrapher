#Config

resolution = 100
frameRate = 10


import math
import pygame
import sys

w = 400

pygame.init()
window = pygame.display.set_mode((w, w), pygame.SCALED)
pygame.display.set_caption("PixelGrapher")

screen = pygame.display.get_surface()

clock = pygame.time.Clock()

radius = (w // resolution) / 2

dots = []

counter = 1
cycle = 1

for i in range(resolution):
    newrow = []
    for j in range(resolution):
        newrow.append(-1)
    dots.append(newrow)

def set(x, y, val):
    try:
        dots[x][y] = val
    except:
        pass

def get(x, y):
    return dots[x][y]

def clear():
    for i in range(0, resolution):
        for j in range(resolution):
            dots[i][j] = -1

def vertical(x):
    for i in range(resolution):
        set(x, i, 1)

def horizontal(y):
    for i in range(resolution):
        set(i, y, 1)

def line(slope, intercept=0):
    for i in range(resolution):
        y = resolution - math.floor(i * round(slope, 4)) - intercept
        if y < 0:
            return
        set(i, y, 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((25, 25, 25))

    #Animations and drawings

    line(8)
    line(4)
    line(2)
    line(1)
    line(1/2)
    line(1/4)
    line(1/8)

    #END ANIMATIONS

    #RENDER
    for i in range(resolution):
        row = dots[i]
        for j in range(resolution):
            if row[j] < 0:
                pygame.draw.circle(screen, (0, 0, 0), [i * radius * 2 + radius, j * radius * 2 + radius], radius)
            else:
                pygame.draw.circle(screen, (255, 255, 255), [i * radius * 2 + radius, j * radius * 2 + radius], radius)


    pygame.display.update()

    #END RENDER

    counter += 1

    clock.tick(frameRate)
