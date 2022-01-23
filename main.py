import pygame

SCREEN_SIZE = (int(800 * 1.5), int(450 * 1.5))
BULL_BG_COLOR = (0.8471 * 255, 0.22157 * 255, 0.1765 * 255)


def draw():
    screen.fill(BULL_BG_COLOR)
    screen.blit(tiger_l_image, tiger_l_pos)
    screen.blit(tiger_r_image, tiger_r_pos)


def import_tiger_l():
    tiger_l_image = pygame.image.load("tigerL.png")
    tiger_l_image = pygame.transform.scale(tiger_l_image,
                                           (tiger_l_image.get_width() // 3, tiger_l_image.get_height() // 3))
    tiger_l_pos = (0, (SCREEN_SIZE[1] - tiger_l_image.get_height()) / 2)
    return tiger_l_image, tiger_l_pos


def import_tiger_r():
    tiger_r_image = pygame.image.load("tigerR.png")
    tiger_r_image = pygame.transform.scale(tiger_r_image,
                                           (tiger_r_image.get_width() // 3, tiger_r_image.get_height() // 3))
    tiger_r_pos = (SCREEN_SIZE[0] - tiger_r_image.get_width(), (SCREEN_SIZE[1] - tiger_r_image.get_height()) / 2)
    return tiger_r_image, tiger_r_pos


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
tiger_l_image, tiger_l_pos = import_tiger_l()
tiger_r_image, tiger_r_pos = import_tiger_r()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw()
    pygame.display.update()
