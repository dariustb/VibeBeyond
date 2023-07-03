''' app.py - driver program for the application '''

# pylint: disable = W0401, W0614, C0103

import pygame
from py.constants import *

if __name__ == '__main__':
    # Start pygame
    pygame.init()

    # Set up app window
    pygame.display.set_caption(APP_NAME)
    pygame.display.set_icon(pygame.image.load(APP_ICON))
    pygame.display.set_mode(SCREEN_SIZE).fill(SCREEN_BKGD)
    pygame.display.update()

    # Set up music player
    pygame.mixer.init()
    pygame.mixer.music.load('src/assets/audio/test_sound.wav')
    pygame.mixer.music.set_volume(DEFAULT_VOLUME)
    pygame.mixer.music.play()

    # Main program loop
    is_window_open = True
    while is_window_open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_window_open = False
