''' app.py - driver program for the application '''

# pylint: disable = invalid-name, no-member
# pylint: disable = wildcard-import, unused-wildcard-import

import pygame
from constants import *

pygame.init()

if __name__ == '__main__':

    icon = pygame.image.load('src/assets/icon256x256.png')

    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(APP_NAME)
    pygame.display.set_icon(icon)

    is_window_open = True

    while is_window_open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_window_open = False

        screen.fill(SCREEN_BKGD)
        pygame.display.update()
