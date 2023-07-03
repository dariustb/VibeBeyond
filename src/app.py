''' app.py - driver program for the application '''

# pylint: disable = invalid-name, no-member

import pygame

pygame.init()

SCREEN_SIZE: tuple = 800, 600 # width, height

if __name__ == '__main__':

    screen = pygame.display.set_mode(SCREEN_SIZE)

    is_window_open = True

    while is_window_open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_window_open = False
