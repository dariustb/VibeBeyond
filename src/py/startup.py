''' validate.py - Used to hold the validation functions '''

# pylint: disable = W0401, W0614

import os
import sys
from py.constants import *

ESSENTIAL_FOLDERS = [
    GEN_FOLDER,
    ASSETS_FOLDER,
    AUDIO_FOLDER,
    MIDI_FOLDER,
    SF2_FOLDER,
    KEYS_FOLDER,
    LEAD_FOLDER,
    KICK_FOLDER,
    HAT_FOLDER,
    SNARE_FOLDER
]

def startup_prep():
    ''' creates missing essential folders for first run '''
    for folder in ESSENTIAL_FOLDERS:
        if not os.path.isdir(folder):
            os.mkdir(folder)

def startup_check():
    ''' checks essential folders & quits if folders are empty '''

    startup_prep()

    is_missing_files = False
    missing_list = []

    # Check for empty folders
    for folder in ESSENTIAL_FOLDERS:
        if folder in (AUDIO_FOLDER, MIDI_FOLDER):
            continue
        if os.listdir(folder) == []:
            is_missing_files = True
            missing_list.append(folder)

    # Log information and quit if found
    if is_missing_files:
        print('[VIBE BEYOND]'
              '\n\tEmpty/missing asset folders found.'
              '\n\tView docs in src/assets/ to find more information.'
              '\n\tAsset folders:', missing_list)
        sys.exit()
