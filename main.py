import pygame
from imageObj import *

SCREEN_SIZE = (int(800 * 1.5), int(450 * 1.5))
BULL_BG_COLOR = (0.8471 * 255, 0.22157 * 255, 0.1765 * 255)


def draw():
    screen.fill(BULL_BG_COLOR)
    screen.blit(tiger_l.image, tiger_l.pos)
    screen.blit(tiger_r.image, tiger_r.pos)


def create_tiger_l():
    tiger_l_image = pygame.image.load("tigerL.png")
    tiger_l_image = pygame.transform.scale(tiger_l_image,
                                           (tiger_l_image.get_width() // 3, tiger_l_image.get_height() // 3))
    tiger_l_pos = (0, (SCREEN_SIZE[1] - tiger_l_image.get_height()) / 2)
    return ImageObj(tiger_l_image, tiger_l_pos, 0, "l")


def create_tiger_r():
    tiger_r_image = pygame.image.load("tigerR.png")
    tiger_r_image = pygame.transform.scale(tiger_r_image,
                                           (tiger_r_image.get_width() // 3, tiger_r_image.get_height() // 3))
    tiger_r_pos = (SCREEN_SIZE[0] - tiger_r_image.get_width(), (SCREEN_SIZE[1] - tiger_r_image.get_height()) / 2)
    return ImageObj(tiger_r_image, tiger_r_pos, 0, "l")


def update(t_elaps):
    tiger_r.pos = (tiger_r.pos[0] - t_elaps / 10, tiger_r.pos[1])
    tiger_l.pos = (tiger_l.pos[0] + t_elaps / 10, tiger_l.pos[1])


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
t_pre = pygame.time.get_ticks()
tiger_l = create_tiger_l()
tiger_r = create_tiger_r()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    t_cur = pygame.time.get_ticks()
    update(t_cur - t_pre)
    t_pre = t_cur
    draw()
    pygame.display.update()
