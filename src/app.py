''' app.py - driver program for the application '''

# pylint: disable = W0401, W0614, C0103, C0413

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from py.validate import prep_assets, validate_assets
from py.create_song import create_song
from py.constants import *

if __name__ == '__main__':
    # Confirm necessary files/folders
    prep_assets()
    validate_assets()

    # Start pygame
    pygame.init()

    # Set up app window
    pygame.display.set_caption(APP_NAME)
    pygame.display.set_icon(pygame.image.load(APP_ICON))
    pygame.display.set_mode(SCREEN_SIZE).fill(SCREEN_BKGD)
    pygame.display.update()

    # Set up music player
    pygame.mixer.init()
    pygame.mixer.music.set_volume(DEFAULT_VOLUME)
    pygame.mixer.music.set_endevent(SONG_ENDED)
    pygame.mixer.music.load(create_song(debug=True))
    pygame.mixer.music.play()

    # Main program loop
    is_window_open: bool = True
    while is_window_open:
        for event in pygame.event.get():
            # User closes window -> end loop
            if event.type == pygame.QUIT:
                is_window_open = False

            # Song ends -> build/load/play next one
            if event.type == SONG_ENDED:
                pygame.mixer.music.load(create_song(debug=True))
                pygame.mixer.music.play()
