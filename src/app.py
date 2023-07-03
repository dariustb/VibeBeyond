''' app.py - driver program for the application '''

# pylint: disable = invalid-name, no-member

import pygame

pygame.init()

APP_NAME: str = "Vibe Beyond"
SCREEN_SIZE: tuple = 800, 600

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

        screen.fill((181, 126, 220))
        pygame.display.update()
