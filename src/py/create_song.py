''' create_song.py - houses the create_song function to prevent cycling in song.py '''

# pylint: disable = W0401, W0614, C0103

from py import song
from py import debug as dbg
from py.constants import *

# The feast de resistance
def create_song(debug: bool = False):
    ''' create_song - builds song and returns the song file path '''

    # Create Midi and Sf2 objects
    SongObj = song.Song()

    # Print debug information
    if debug:
        dbg.print_info(SongObj)

    # Create midi file of the song
    SongObj.gen_chord_prog()
    SongObj.gen_drum_loop()
    SongObj.save_midi_file(SongObj.mid_prog_track, SongObj.keys_midi)

    # Convert midi file to audio file with soundfont
    SongObj.midi_to_audio()

    SongObj.export_song()

    return SongObj.song_path
