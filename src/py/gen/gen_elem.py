''' elements.py - This file will produce elements to make the song '''

# pylint: disable = W0401, W0614

import random
from py.constants import *

class SongElements:
    ''' This class will hold the song's musical elements + setters/getters '''
    def __init__(self):
        ''' All the song's element attributes will be kept here '''

        # Song generation info
        self.key:  str = self.set_key()
        self.time: str = self.set_time()
        self.bpm:  str = self.set_bpm() # tempo = mido.bpm2tempo(bpm) =/= bpm
        self.prog: str = self.set_prog()

    # SETTER FUNCTIONS
    def set_key(self):
        ''' Returns randomly chosen key '''
        return random.choice(VALID_KEYS)

    def set_time(self):
        ''' Returns randomly chosen time signature '''
        return random.choice(TIME_SIGNATURES)

    def set_bpm(self):
        ''' Returns randomly chosen bpm '''
        return random.randint(MIN_BPM, MAX_BPM)

    def set_prog(self):
        ''' Returns randomly chosen chord progression '''
        return random.choice(CHORD_PROGRESSIONS)
