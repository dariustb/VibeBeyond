""" vibebeyond - driver program for the application """

import pygame

from core.generation.gen_create import create_song

# Global variables
APP_NAME: str = "Vibe Beyond"
APP_VERSION: str = "1.0.0"
APP_ICON: str = "src/assets/vb_icon.png"

DEFAULT_SCREEN_WIDTH: int = 600
DEFAULT_SCREEN_HEIGHT: int = 150
DEFAULT_SCREEN_SIZE: tuple = (DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
DEFAULT_SCREEN_BKGD: tuple = (242, 218, 201)  # Champagne Pink
DEFAULT_MIXER_VOLUME: float = 0.7

PLAY_BUTTON_LOCATION: tuple = (65, 44)  # X-Y coords from Figma
PUASE_BUTTON_LOCATION: tuple = (60, 45)
VOLUME_SLIDER_LOCATION: tuple = (
    (213, 71),
    (245, 71),
    (277, 71),
    (309, 71),
    (341, 71),
)

EVENT_SONG_ENDED: int = pygame.USEREVENT + 616  # pylint: disable = E1101

if __name__ == "__main__":
    # Start pygame
    pygame.init()

    # Set up app window
    scrn = pygame.display.set_mode(DEFAULT_SCREEN_SIZE)
    scrn.fill(DEFAULT_SCREEN_BKGD)
    pygame.display.set_caption(APP_NAME)
    pygame.display.set_icon(pygame.image.load(APP_ICON))
    pygame.display.update()

    # Set up app screen
    skin_screen = pygame.image.load("src/assets/_media/vb_skin_400x150.png")
    play_button = pygame.image.load("src/assets/_media/vb_play_button_54x62.png")
    pause_button = pygame.image.load("src/assets/_media/vb_pause_button_48x61.png")
    inactive_vol = pygame.image.load(
        "src/assets/_media/vb_volume_button_inactive_10x10.png"
    )
    active_vol = pygame.image.load(
        "src/assets/_media/vb_volume_button_active_10x10.png"
    )

    volume_index = 2
    scrn.blit(skin_screen, (0, 0))
    scrn.blit(play_button, PLAY_BUTTON_LOCATION)
    for index, location in enumerate(VOLUME_SLIDER_LOCATION):
        if index == volume_index:
            scrn.blit(active_vol, location)
        else:
            scrn.blit(inactive_vol, location)

    pygame.display.flip()

    # Set up music player
    pygame.mixer.init()
    pygame.mixer.music.set_volume(DEFAULT_MIXER_VOLUME)
    pygame.mixer.music.set_endevent(EVENT_SONG_ENDED)
    pygame.mixer.music.load(create_song())
    pygame.mixer.music.play()

    # Main program loop
    is_window_open: bool = True
    while is_window_open:
        for event in pygame.event.get():
            # User closes window -> end loop
            if event.type == pygame.QUIT:
                is_window_open = False

            # Song ends -> build/load/play next song
            if event.type == EVENT_SONG_ENDED:
                pygame.mixer.music.load(create_song())
                pygame.mixer.music.play()

    # Deactivate pygame library
    pygame.quit()
