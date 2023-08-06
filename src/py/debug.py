''' debug.py - Python module for printing test/debug information '''

# pylint: disable = W0401, W0614

import logging
from py import song
from py.constants import *

logging.basicConfig(filename="vb_log.log",
            format='%(asctime)s %(message)s',
            filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# PRINT FUNCTIONS
def print_debug_song_info(song_mid: song.SongElements):
    ''' Prints the class variables to console '''
    if not song_mid:
        logger.error('(%s) No song information available', print_debug_song_info.__name__)

    else:
        logger.debug('(%s)', print_debug_song_info.__name__)
        logger.debug('--------------- DEBUG: SONG INFORMATION ---------------')
        logger.debug('Title:\t%s',  song_mid.title)
        logger.debug('Artist:\t%s', song_mid.artist)

        logger.debug('Key:\t%s',    song_mid.key)
        logger.debug('BPM:\t%s',    song_mid.bpm)
        logger.debug('Time:\t%s',   song_mid.time_sig)
        logger.debug('Chords:\t%s', song_mid.prog)

        logger.debug('Keys:\t%s',   song_mid.keys_name.replace(KEYS_FOLDER, ''))
        logger.debug('Lead:\t%s',   song_mid.lead_name.replace(LEAD_FOLDER, ''))

        logger.debug('Kick:\t%s',   song_mid.kick_name.replace(KICK_FOLDER, ''))
        logger.debug('Hat:\t%s',    song_mid.hat_name.replace(HAT_FOLDER, ''))
        logger.debug('Snare:\t%s',  song_mid.snare_name.replace(SNARE_FOLDER, ''))

        logger.debug('-------------------------------------------------------')

def print_debug_midi_track(song_mid: song.SongElements):
    ''' Prints the chord progression to console '''
    logger.debug('Chords:\t%s', song_mid.mid_prog_track)
