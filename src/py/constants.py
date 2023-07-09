''' constants.py - File to contain all important constant values for the application '''

# pylint: disable = E0611

from pygame import USEREVENT

# App metadata
APP_NAME:    str = 'Vibe Beyond'
APP_VERSION: str = '1.0.0'
APP_ICON:    str = 'src/assets/images/icon256x256.png'

# Folders
AUDIO_FOLDER: str = 'src/gen/audio/'
MIDI_FOLDER:  str = 'src/gen/midi/'
SF2_FOLDER:   str = 'src/assets/sf2/'
SF3_FOLDER:   str = 'src/assets/sf3/'
KEYS_FOLDER:  str = 'src/assets/sf2/'
LEAD_FOLDER:  str = 'src/assets/sf2/'
KICK_FOLDER:  str = 'src/assets/drums/kicks/'
HAT_FOLDER:   str = 'src/assets/drums/hats/'
SNARE_FOLDER: str = 'src/assets/drums/snares/'

# File types
AUDIO_TYPE:      str = 'wav' # See note on soundfonts.py:midi_to_audio() before changing
AUDIO_FILE_TYPE: str = '.' + AUDIO_TYPE
MIDI_FILE_TYPE:  str = '.mid'
SF2_FILE_TYPE:   str = '.sf2'
SF3_FILE_TYPE:   str = '.sf3'

# Pygame window
SCREEN_WIDTH:  int = 800
SCREEN_HEIGHT: int = 600
SCREEN_SIZE: tuple = SCREEN_WIDTH, SCREEN_HEIGHT
SCREEN_BKGD: tuple = 181, 126, 220

# Pygame mixer
DEFAULT_VOLUME: float = 0.7
SONG_ENDED: int = USEREVENT + 616

# Music Generation Defaults
MIN_BPM: int = 75
MAX_BPM: int = 100
VALID_KEYS:         tuple = 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab'
TIME_SIGNATURES:    tuple = (4,4),(4,4)
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
SONG_LENGTH:    int = 4 # number of chord progression repeats in a song
BASE_NOTE:      int = 480 # note length in ticks (480 ticks per beat)
QTR_NOTE:       int = BASE_NOTE - 1
HALF_NOTE:      int = BASE_NOTE * 2 - 1
WHOLE_NOTE:     int = BASE_NOTE * 4 - 1
EIGHTH_NOTE:    int = BASE_NOTE // 2 - 1
SIXTEENTH_NOTE: int = BASE_NOTE // 4 - 1
DOT_QTR_NOTE:   int = int(BASE_NOTE * 1.5) - 1
DOT_8TH_NOTE:   int = int(BASE_NOTE * 0.75) - 1
