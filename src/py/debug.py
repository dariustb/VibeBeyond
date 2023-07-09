''' debug.py - Python module for printing test/debug information '''

from py import song
import py.soundfont as sf2

# PRINT FUNCTIONS
def print_info(song_mid: song.Song = None, song_sf2: sf2.SoundFont = None):
    ''' Prints the class variables to console '''
    print()
    print('--------------- DEBUG: SONG INFORMATION ---------------')

    if not song_mid and not song_sf2:
        print('print_info: No information available')
        return

    if song_mid is not None:
        print()
        print('Title:\t',  song_mid.title)
        print('Artist:\t', song_mid.artist)

        print()
        print('Key:\t',    song_mid.key)
        print('BPM:\t',    song_mid.bpm)
        print('Time:\t',   song_mid.time_sig)
        print('Chords:\t', song_mid.prog)

    if song_sf2 is not None:
        print()
        print('Keys:\t',  song_sf2.keys_name)
        print('Lead:\t',  song_sf2.lead_name)

    if song_mid is not None:
        print('Kick:\t',  song_mid.kick_name)
        print('Hat:\t',   song_mid.hat_name)
        print('Snare:\t', song_mid.snare_name)

    print('-------------------------------------------------------')
    print()

def print_chords(song_mid: song.Song):
    ''' Prints the chord progression to console '''
    print()
    print('Chords:\t',      song_mid.mid_prog_track)
