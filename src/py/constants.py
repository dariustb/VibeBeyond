''' constants.py - File to contain all important constant values for the application '''

# pylint: disable = E0611

from pygame import USEREVENT

# App metadata
APP_NAME: str = 'Vibe Beyond'
APP_VERSION: str = '2.0.0'
APP_ICON: str = 'src/assets/images/icon256x256.png'

# Folders
MIDI_FOLDER: str = 'src/gen/midi/'
SF2_FOLDER: str = 'src/assets/sf2/'

# File types
MIDI_FILE_TYPE: str = '.mid'
AUDIO_FILE_TYPE: str = 'wav' # See note on soundfonts.py:midi_to_audio() before changing

# Pygame window
SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCREEN_SIZE: tuple = SCREEN_WIDTH, SCREEN_HEIGHT
SCREEN_BKGD: tuple = 181, 126, 220

# Pygame mixer
DEFAULT_VOLUME: float = 0.7
SONG_ENDED: int = USEREVENT + 616

# Music Generation Defaults
MIN_BPM: int = 75
MAX_BPM: int = 120
VALID_KEYS: tuple = 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab'
TIME_SIGNATURES: tuple = (4,4),(4,4)
CHORD_PROGRESSIONS: tuple = (
    ('ii', 'V', 'I', 'IV'),
    ('ii7', 'V', 'I7', 'I7'),
    ('ii', 'V7', 'iii', 'vi'),

    ('iii', 'vi', 'IV', 'I'),

    ('IV', 'I', 'ii', 'vi'),
    ('IV', 'I', 'iii', 'IV'),
    ('IV', 'I', 'V', 'vi'),
    ('IV', 'IV', 'I', 'V'),
    ('IV', 'vi', 'I', 'V'),
    ('IV', 'vi', 'iii', 'I'),

    ('V', 'I', 'vi', 'V'),
    ('V', 'IV', 'vi', 'I'),
    ('V', 'vi', 'IV', 'I'),

    ('vi', 'bVIM', 'bVIIM', 'I'),
    ('vi', 'ii', 'V', 'I'),
    ('vi', 'IV', 'I', 'V'),
    ('vi', 'V', 'IV', 'V', 'ii', 'V', 'I', 'I'),
    ('vi', 'V', 'IV', 'V'),
    ('vi', 'vii', 'V', 'vi', '#IVdim', 'V')
)
