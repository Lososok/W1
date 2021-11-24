import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
RED = (255, 0, 0)
BLACK = (0, 0 , 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

rect(screen, WHITE, ((0, 0), (400, 400)))       # background

circle(screen, YELLOW, (200, 200), 150)         # main face

rect(screen, BLACK, ((125, 270), (150, 30)))    # mouth

circle(screen, RED, (125, 150), 30)             # eyes
circle(screen, BLACK, (125, 150), 15)
circle(screen, RED, (275, 150), 20)
circle(screen, BLACK, (275, 150), 10)

polygon(screen, BLACK, [(170, 144), (45, 62), (51, 54), (176, 136), (170, 144)])    # eyebrows
polygon(screen, BLACK, [(230, 142), (350, 102), (346, 93), (226, 133), (230, 142)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
