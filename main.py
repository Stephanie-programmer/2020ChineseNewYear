import pygame
SCREEN_SIZE = (int(800 * 1.5), int(450 * 1.5))
BULL_BG_COLOR = (0.8471 * 255, 0.22157 * 255, 0.1765 * 255)



def draw():
    screen.fill(BULL_BG_COLOR)



pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw()
    pygame.display.update()