''' info.py - Python module for printing test/debug info '''

from . import song
from . import soundfont as sf2

# PRINT FUNCTIONS
def print_info(song_mid: song.Song, song_sf2: sf2.SoundFont):
    ''' Prints the class variables to console '''
    print()
    print('Title:\t',       song_mid.title)
    print('Artist:\t',      song_mid.artist)

    print()
    print('Key:\t',         song_mid.key)
    print('BPM:\t',         song_mid.bpm)
    print('Time:\t',        song_mid.time_sig)
    print('Chords:\t',      song_mid.prog)

    print()
    print('Keys:\t',        song_sf2.keys_name)
    print('Lead:\t',        song_sf2.lead_name)
    print('Bass:\t',        song_sf2.bass_name)
    print('Drum:\t',        song_sf2.drum_name)

def print_chords(song_mid: song.Song):
    ''' Prints the chord progression to console '''
    print()
    print('Chords:\t',      song_mid.mid_prog_track)
