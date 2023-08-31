''' validate.py - Used to hold the validation functions '''

# pylint: disable = W0401, W0614

import os
import sys
from py.constants import *

class Startup:
    ''' This class will create essential folders for first-time runs '''
    def __init__(self):
        ''' All the Startup's attributes will be kept here '''
        self.essential_folders = [
            GEN_FOLDER,
            ASSETS_FOLDER,
            AUDIO_FOLDER,
            MIDI_FOLDER,
            SF2_FOLDER,
            KEYS_FOLDER,
            LEAD_FOLDER,
            DRUMS_FOLDER,
            KICK_FOLDER,
            HAT_FOLDER,
            SNARE_FOLDER
        ]
        self.prep()
        self.check()

    def prep(self) -> None:
        ''' creates missing essential folders for first run '''
        for folder in self.essential_folders:
            if not os.path.isdir(folder):
                os.mkdir(folder)

    def check(self) -> None:
        ''' checks essential folders & quits if folders are empty '''

        is_missing_files = False
        missing_list = []

        # Check for empty folders
        for folder in self.essential_folders:
            if folder in (AUDIO_FOLDER, MIDI_FOLDER):
                continue
            if os.listdir(folder) == []:
                is_missing_files = True
                missing_list.append(folder)

        # Log information and quit if found
        if is_missing_files:
            print('Empty asset folders found: \n\t%s',
                             str(missing_list))
            print('Go to https://dariustb.github.io/VibeBeyond/faq for more information')
            sys.exit()
