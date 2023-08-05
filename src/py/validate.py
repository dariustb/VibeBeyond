''' validate.py - Used to hold the validation functions '''

# pylint: disable = W0401, W0614

import os
import sys
from py.constants import *

SET_FOLDERS = [
    GEN_FOLDER,
    ASSETS_FOLDER,
    AUDIO_FOLDER,
    MIDI_FOLDER,
    SF2_FOLDER,
    KEYS_FOLDER,
    LEAD_FOLDER,
    KICK_FOLDER,
    HAT_FOLDER,
    SNARE_FOLDER,
    IMAGE_FOLDER
]

def prep_assets():
    ''' Creates missing asset folders for first run '''
    for folder in SET_FOLDERS:
        if not os.path.isdir(folder):
            os.mkdir(folder)

def validate_assets():
    ''' quits if assets folders are missing files '''

    is_missing_files = False
    missing_list = []

    # Check for empty folders
    for folder in SET_FOLDERS:
        if folder in (AUDIO_FOLDER, MIDI_FOLDER):
            continue
        if os.listdir(folder) == []:
            is_missing_files = True
            missing_list.append(folder)

    # Log information and quit if found
    if is_missing_files:
        print('[VIBE BEYOND]'
              '\n\tEmpty/missing asset folders found.'
              '\n\tView readme in src/assets/ to find more information.'
              '\n\tAsset folders:', missing_list)
        sys.exit()
