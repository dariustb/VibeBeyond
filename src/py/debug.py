''' debug.py - Python module for printing test/debug information '''

# pylint: disable = W0401, W0614

from py import song
from py.constants import *

# PRINT FUNCTIONS
def print_info(song_mid: song.Song):
    ''' Prints the class variables to console '''
    print()
    print('--------------- DEBUG: SONG INFORMATION ---------------')

    if not song_mid:
        print('print_info: No information available')

    else:
        print()
        print('Title:\t',  song_mid.title)
        print('Artist:\t', song_mid.artist)

        print()
        print('Key:\t',    song_mid.key)
        print('BPM:\t',    song_mid.bpm)
        print('Time:\t',   song_mid.time_sig)
        print('Chords:\t', song_mid.prog)

        print()
        print('Keys:\t',  song_mid.keys_name.replace(KEYS_FOLDER, ''))
        print('Lead:\t',  song_mid.lead_name.replace(LEAD_FOLDER, ''))

        print()
        print('Kick:\t',  song_mid.kick_name.replace(KICK_FOLDER, ''))
        print('Hat:\t',   song_mid.hat_name.replace(HAT_FOLDER, ''))
        print('Snare:\t', song_mid.snare_name.replace(SNARE_FOLDER, ''))

    print('-------------------------------------------------------')
    print()

def print_chords(song_mid: song.Song):
    ''' Prints the chord progression to console '''
    print()
    print('Chords:\t',      song_mid.mid_prog_track)
