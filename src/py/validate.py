''' validate.py - Used to hold the validation functions '''

# pylint: disable = W0401, W0614

import os
from py.constants import *

def validate_assets():
    ''' quits if assets folders are missing files '''

    is_missing_files = False
    missing_list = []

    asset_folders = [
        KEYS_FOLDER,
        LEAD_FOLDER,
        KICK_FOLDER,
        HAT_FOLDER,
        SNARE_FOLDER,
        IMAGE_FOLDER
    ]

    # Check for empty folders
    for folder in asset_folders:
        if (not os.path.isdir(folder)) or (os.listdir(folder) == []):
            is_missing_files = True
            missing_list.append(folder)

    # Log information and quit if found
    if is_missing_files:
        print('[VIBE BEYOND]'
              '\n\tEmpty/missing asset folders found.'
              '\n\tView readme in src/assets/ to find more information.'
              '\n\tAsset folders:', missing_list)
        quit()
