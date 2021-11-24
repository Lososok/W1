import pygame
from pygame.draw import *

pygame.init()

def draw_NLO(x_NLO, y_NLO, height_NLO, wide_NLO):
    '''
    draw NLO on screen since middle of lower part (x_NLO, y_NLO)
    with full height and wide = 'height_NLO', 'wide_NLO'
    x_NLO - horizontal coordinate
    y_NLO - vertical coordinate
    height_NLO - full hight
    wide_NLO - full wide
    '''
    pass
def draw_alien(x_alien, y_alien, height_alien, wide_alien):
    '''
    draw alien on screen since middle of lower part (x_alien, y_alien)
    with full height and wide = 'height_alien', 'wide_alien'
    x_alien - horizontal coordinate
    y_alien - vertical coordinate
    height_alien - full hight
    wide_alien - full wide
    '''
    pass
def draw_backgraund(y_backgraund, x_moon, y_moon, r_moon):
    '''
    draw land, heaven and line between they
    draw the Moon
    y_bacgraund - ratio land and heaven
    r_moon - radius the Moon
    x_moon - horizontal coordinate
    y_moon - vertical coordinat
    '''
    pass
def draw_clouds(N, visibility):
    '''
    draw N clouds with 'visibility' visibility
    N - quantity clouds
    visibility - noticeability
    '''
    pass

screen = pygame.display.set_mode((500, 700))
FPS = 30
WHITE = (255, 255, 255)
GREY = (169, 169, 169)
GREEN = (0, 100, 0)
RED = (178, 34, 34)
BLUE = (47, 79, 79)
BLACK = (0, 0, 0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
