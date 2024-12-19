#Config

resolution = 100
frameRate = 30


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

def line(slope, intercept=0, color=1):
    for i in range(resolution):
        y = resolution - math.floor(i * round(slope, 4)) - intercept
        if y < 0:
            return
        set(i, y, color)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((25, 25, 25))

    #Animations and drawings

    clear()

    line(8, color=2)
    line(4, color=3)
    line(2, color=4)
    line(1, color=5)
    line(1/2, color=6)
    line(1/4, color=2)
    line(1/8, color=3)


    #END ANIMATIONS

    #RENDER
    for i in range(resolution):
        row = dots[i]
        for j in range(resolution):
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

    #END RENDER

    counter += 1

    clock.tick(frameRate)
