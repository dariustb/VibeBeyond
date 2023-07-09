''' create_song.py - houses the create_song function to prevent cycling in song.py '''

# pylint: disable = W0401, W0614, C0103

from py import song
from py import soundfont as sf2
from py import debug as dbg
from py.constants import *

# The feast de resistance
def create_song(debug: bool = False):
    ''' create_song - builds song and returns the song file path '''

    # Create Midi and Sf2 objects
    SongMid = song.Song()
    SongSf2 = sf2.SoundFont()

    # Create midi file of the song
    SongMid.gen_chord_prog()
    SongMid.gen_drum_loop()
    song_midi_path = SongMid.save_midi_file()

    # Print debug information
    if debug:
        dbg.print_info(SongMid, SongSf2)

    # Generate an output path
    song_output_path = AUDIO_FOLDER + SongMid.title + '.' + AUDIO_FILE_TYPE

    # Convert midi file to audio
    SongSf2.midi_to_audio(song_midi_path, song_output_path)

    SongMid.export_song()

    return song_output_path
