import pygame
from pygame.draw import *

pygame.init()

def main():
    y_backgraund = 350
    x_moon, y_moon, r_moon = 325, 175, 75
    x_alien, y_alien = 100, 100
    height_alien, wide_alien = 280, 187.5       # [280, 187.5]
    draw_backgraund(y_backgraund, x_moon, y_moon, r_moon)
    draw_aliens(x_alien, y_alien, height_alien, wide_alien)
'''
    draw_NLO(x_NLO, y_NLO, height_NLO, wide_NLO)
    draw_clouds(N_clouds, visibility)
'''

def draw_backgraund(y_backgraund, x_moon, y_moon, r_moon):
    '''
    draw land, heaven and line between they
    draw the Moon
    y_bacgraund - ratio land and heaven
    r_moon - radius the Moon
    x_moon - horizontal coordinate
    y_moon - vertical coordinat
    '''
    rect(screen, BLUE, ((0, 0), (500, y_backgraund)))
    rect(screen, GREEN, ((0, y_backgraund), (500, 700)))
    circle(screen, GREY, (x_moon, y_moon), r_moon)
    pass

def draw_aliens(x_alien, y_alien, height_alien, wide_alien):
    '''
    draw aliens on screen since left of lower part (x_alien, y_alien)
    with full height and wide = 'height_alien', 'wide_alien'
    x_alien - horizontal coordinate
    y_alien - vertical coordinate
    height_alien - full hight
    wide_alien - full wide
    '''
    draw_body(x_alien, y_alien, height_alien, wide_alien)
    draw_had()
    draw_apple()
    pass


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

def draw_clouds(N_clouds, visibility):
    '''
    draw N clouds with 'visibility' visibility
    N_clouds - quantity clouds
    visibility - noticeability
    '''
    pass

def draw_body(x_alien, y_alien, height_alien, wide_alien):
    r_leg = int(height_alien/27)  # = r_arm
    x_leg, y_leg = int(wide_alien/10), int(2*height_alien/5)
    x_body, y_body = int(3*wide_alien/10), int(height_alien/3)
    x_arm, y_arm = int(wide_alien/2), int(height_alien/9)
    # left leg
    circle(screen, WHITE, (x_alien, 700 - y_alien - r_leg), r_leg)
    ellipse(screen, WHITE, ((x_alien + 0.2 * r_leg, 700 - y_alien - 0.5 * y_leg),
                            (x_leg, y_leg/2.5)))
    ellipse(screen, WHITE, ((x_alien + 0.2 * r_leg + 0.25 *x_leg,
                             700 - y_alien - 0.5 * y_leg - 0.2 * y_leg),
                            (1.1 * x_leg, y_leg/3.5)))
    # body
    ellipse(screen, WHITE, ((x_alien + 0.07 * wide_alien, 700 - y_alien - 1.35 * y_leg),
                            (3*wide_alien/10, y_body)))
    # right leg
    circle(screen, WHITE, (x_alien + 0.4 * wide_alien, 700 - y_alien + 0.2 * r_leg), r_leg)
    ellipse(screen, WHITE, ((x_alien + 0.4 * wide_alien - 1.8 * r_leg,
                             700 - y_alien - 4.5 * r_leg),
                            (x_leg, y_leg/2.5)))
    ellipse(screen, WHITE, ((x_alien + 0.2 * r_leg + 0.25 * x_leg + 0.25 * wide_alien,
                             700 - y_alien - 0.5 * y_leg - 0.2 * y_leg + 0.45 * r_leg),
                            (1.1 * x_leg, y_leg/3.5)))
    # left arm
    circle(screen, WHITE, (x_arm + 2 * r_leg,700 - 0.85 * height_alien), r_leg)
    ellipse(screen, WHITE, ((x_arm - 0.2 * r_leg, 700 - 0.83 * height_alien),
                            (2 * r_leg, 1.5 * r_leg)))
    ellipse(screen, WHITE, ((x_arm - 1 * r_leg, 700 - 0.76 * height_alien),
                            (r_leg, 1.5 * r_leg)))
    # right arm
    circle(screen, WHITE, (x_arm + 2 * r_leg + 0.3 * wide_alien,700 - 0.85 * height_alien), r_leg)
    ellipse(screen, WHITE, ((x_arm + 0.44 * wide_alien, 700 - 0.85 * height_alien),
                            (2 * r_leg, 1.5 * r_leg)))
    ellipse(screen, WHITE, ((x_arm + 0.55 * wide_alien, 700 - 0.82 * height_alien),
                            (2.5 * r_leg, 1.5 * r_leg)))

def draw_had():
    pass

def draw_apple():
    pass

screen = pygame.display.set_mode((500, 700))
FPS = 30
WHITE = (255, 255, 255)
GREY = (169, 169, 169)
GREEN = (0, 100, 0)
RED = (178, 34, 34)
BLUE = (25, 25, 112)
BLACK = (0, 0, 0)

main()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
