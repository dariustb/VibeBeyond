''' app.py - driver program for the application '''

# pylint: disable = W0401, W0614, C0103

import pygame
from py import info
from py import song
from py import soundfont as sf2
from py.constants import *

def create_song():
    ''' create_song - builds song and returns the song file path '''

    # Create Midi and Sf2 objects
    SongMid = song.Song()
    SongSf2 = sf2.SoundFont()

    # Create midi file of the song
    SongMid.gen_chord_prog()
    SongMid.gen_drum_loop()
    song_midi_path = SongMid.save_midi_file()

    info.print_info(SongMid, SongSf2)

    # Generate an output path
    song_output_path = AUDIO_FOLDER + SongMid.title + '.' + AUDIO_FILE_TYPE

    # Convert midi file to audio
    SongSf2.midi_to_audio(song_midi_path, song_output_path)

    SongMid.export_song()

    return song_output_path

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
    pygame.mixer.music.set_volume(DEFAULT_VOLUME)
    pygame.mixer.music.set_endevent(SONG_ENDED)
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
            if event.type == SONG_ENDED:
                pygame.mixer.music.load(create_song())
                pygame.mixer.music.play()
