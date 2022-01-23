import pygame

from imageObj import *

SCREEN_SIZE = (int(800 * 1.5), int(450 * 1.5))
BULL_BG_COLOR = (0.8471 * 255, 0.22157 * 255, 0.1765 * 255)
LION_BG_COLOR = (0.8471 * 255, 0.1020 * 255, 0.2039 * 255)


def draw():
    if lion.hidden:
        screen.fill(BULL_BG_COLOR)
        screen.blit(tiger_l.image, tiger_l.pos)
        screen.blit(tiger_r.image, tiger_r.pos)
    else:
        screen.fill(LION_BG_COLOR)
        screen.blit(lion.image, lion.pos)  # draw lion in the middle
        draw_greeting()
        draw_tiger_l_rot()
        draw_tiger_r_rot()


def draw_tiger_r_rot():
    screen.blit(tiger_r.image, tiger_r.image.get_rect(
        center=tiger_r.image.get_rect(topleft=(
            SCREEN_SIZE[0] - tiger_r.image.get_width() - ImageObj.position_offset,
            (SCREEN_SIZE[1] - tiger_r.image.get_height()) / 2)).center).topleft)


def draw_tiger_l_rot():
    screen.blit(tiger_l.image, tiger_l.image.get_rect(
        center=tiger_l.image.get_rect(topleft=(tiger_l.position_offset,
                                               (SCREEN_SIZE[
                                                    1] - tiger_l.image.get_height()) / 2)).center).topleft)


def draw_greeting():
    font = pygame.font.Font('YSHaoShenTi-2.ttf', 100)
    greeting = "新春快乐"
    font_color = (255, 207, 64)
    greeting_pos = (SCREEN_SIZE[0] / 2.7, SCREEN_SIZE[1] * 3 / 4)
    greeting = font.render(greeting, True, font_color)
    screen.blit(greeting, greeting_pos)


def create_tiger_l():
    tiger_l_image = pygame.image.load("tigerL.png")
    tiger_l_image = pygame.transform.scale(tiger_l_image,
                                           (tiger_l_image.get_width() // 3, tiger_l_image.get_height() // 3))
    tiger_l_pos = (0, (SCREEN_SIZE[1] - tiger_l_image.get_height()) / 2)
    return ImageObj(tiger_l_image, tiger_l_pos, "l")


def create_tiger_r():
    tiger_r_image = pygame.image.load("tigerR.png")
    tiger_r_image = pygame.transform.scale(tiger_r_image,
                                           (tiger_r_image.get_width() // 3, tiger_r_image.get_height() // 3))
    tiger_r_pos = (SCREEN_SIZE[0] - tiger_r_image.get_width(), (SCREEN_SIZE[1] - tiger_r_image.get_height()) / 2)
    return ImageObj(tiger_r_image, tiger_r_pos, "l")


def create_lion():
    lion_image = pygame.image.load("lion_middle.jpg")
    lion_image = pygame.transform.scale(lion_image, (lion_image.get_width() // 3, lion_image.get_height() // 3))
    lion_pos = ((SCREEN_SIZE[0] - lion_image.get_width()) / 2, (SCREEN_SIZE[1] - lion_image.get_height()) / 8)
    return ImageObj(lion_image, lion_pos, True)


def update(t_elaps):
    tiger_r.pos = (tiger_r.pos[0] - t_elaps / 10, tiger_r.pos[1])
    tiger_l.pos = (tiger_l.pos[0] + t_elaps / 10, tiger_l.pos[1])
    if tiger_r.pos[0] - tiger_l.pos[0] < tiger_l.image.get_width():
        lion.hidden = False
    if not lion.hidden:
        rotate_tigers(t_elaps)


def rotate_tigers(t_elaps):
    if ImageObj.angle > ImageObj.rotation_offset and ImageObj.direction == "r":
        ImageObj.angle -= t_elaps / 15
        ImageObj.direction = "l"
    elif ImageObj.angle < -1 * ImageObj.rotation_offset and ImageObj.direction == "l":
        ImageObj.angle += t_elaps / 15
        ImageObj.direction = "r"
    else:
        if ImageObj.direction == "r":
            ImageObj.angle += t_elaps / 15
        else:
            ImageObj.angle -= t_elaps / 15
    tiger_l.image = pygame.transform.rotate(tiger_l.originalImage, ImageObj.angle)
    tiger_r.image = pygame.transform.rotate(tiger_r.originalImage, -1 * ImageObj.angle)


def play_bg_music():
    bg_music = pygame.mixer.Sound('Dive Down - VYEN.mp3')
    bg_music.play(-1)


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
play_bg_music()
t_pre = pygame.time.get_ticks()

tiger_l = create_tiger_l()
tiger_r = create_tiger_r()
lion = create_lion()

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
