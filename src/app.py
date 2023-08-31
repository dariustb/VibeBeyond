''' app.py - driver program for the application '''

# pylint: disable = W0401, W0614, C0103, C0413

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from py                 import constants as const
from py.mem.startup     import Startup
from py.gen.create_song import create_song

if __name__ == '__main__':
    # Confirm necessary files/folders
    Startup()

    # Start pygame
    pygame.init()

    # Set up app window
    pygame.display.set_caption(const.APP_NAME)
    pygame.display.set_icon(pygame.image.load(const.APP_ICON))
    pygame.display.set_mode(const.SCREEN_SIZE).fill(const.SCREEN_BKGD)
    pygame.display.update()

    # Set up music player
    pygame.mixer.init()
    pygame.mixer.music.set_volume(const.DEFAULT_VOLUME)
    pygame.mixer.music.set_endevent(const.SONG_ENDED)
    pygame.mixer.music.load(create_song())
    pygame.mixer.music.play()

    # Main program loop
    is_window_open: bool = True
    while is_window_open:
        for event in pygame.event.get():
            # User closes window -> end loop
            if event.type == pygame.QUIT:
                is_window_open = False

            # Song ends -> build/load/play next one
            if event.type == const.SONG_ENDED:
                pygame.mixer.music.load(create_song())
                pygame.mixer.music.play()
