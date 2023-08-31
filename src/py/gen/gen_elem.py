''' elements.py - This file will produce elements to make the song '''

# pylint: disable = W0401, W0614

import random
from .. import constants as const

class SongElements:
    ''' This class will hold the song's musical elements + setters/getters '''
    def __init__(self):
        ''' All the song's element attributes will be kept here '''

        # Song generation info
        self.key:  str        = self.set_key()
        self.time: tuple(int) = self.set_time()
        self.bpm:  int        = self.set_bpm() # tempo = mido.bpm2tempo(bpm) =/= bpm
        self.prog: tuple(str) = self.set_prog()

    # SETTER FUNCTIONS
    def set_key(self):
        ''' Returns randomly chosen key '''
        return random.choice(const.VALID_KEYS)

    def set_time(self):
        ''' Returns randomly chosen time signature '''
        return random.choice(const.TIME_SIGNATURES)

    def set_bpm(self):
        ''' Returns randomly chosen bpm '''
        return random.randint(const.MIN_BPM, const.MAX_BPM)

    def set_prog(self):
        ''' Returns randomly chosen chord progression '''
        return random.choice(const.CHORD_PROGRESSIONS)
