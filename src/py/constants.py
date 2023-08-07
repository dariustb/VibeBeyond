''' constants.py - File to contain all important constant values for the application '''

# pylint: disable = E0611

from pygame import USEREVENT

# App metadata
APP_NAME:    str = 'Vibe Beyond'
APP_VERSION: str = '1.0.0'
APP_ICON:    str = 'src/assets/images/icon256x256.png'

# Folders
GEN_FOLDER:     str = 'src/gen/'
AUDIO_FOLDER:   str = 'src/gen/audio/'
MIDI_FOLDER:    str = 'src/gen/midi/'
ASSETS_FOLDER:  str = 'src/assets/'
SF2_FOLDER:     str = 'src/assets/sf2/'
KEYS_FOLDER:    str = SF2_FOLDER
AMBIENT_FOLDER: str = 'src/assets/sf2/ambient/'
LEAD_FOLDER:    str = 'src/assets/sf2/lead/'
MELODY_FOLDER:  str = LEAD_FOLDER
CMELODY_FOLDER: str = LEAD_FOLDER
CHORDS_FOLDER:  str = 'src/assets/sf2/chords/'
BASS_FOLDER:    str = 'src/assets/sf2/bass/'
DRUMS_FOLDER:   str = 'src/assets/drums/'
KICK_FOLDER:    str = 'src/assets/drums/kicks/'
HAT_FOLDER:     str = 'src/assets/drums/hats/'
SNARE_FOLDER:   str = 'src/assets/drums/snares/'
IMAGE_FOLDER:   str = 'src/assets/images/'

# File types
AUDIO_TYPE:      str = 'wav' # See note on soundfonts.py:midi_to_audio() before changing
AUDIO_FILE_TYPE: str = '.' + AUDIO_TYPE
MIDI_FILE_TYPE:  str = '.mid'
SF2_FILE_TYPE:   str = '.sf2'

# Pygame window
SCREEN_WIDTH:  int = 800
SCREEN_HEIGHT: int = 600
SCREEN_SIZE: tuple = SCREEN_WIDTH, SCREEN_HEIGHT
SCREEN_BKGD: tuple = 181, 126, 220

# Pygame mixer
DEFAULT_VOLUME: float = 0.7
SONG_ENDED:       int = USEREVENT + 616

# Music generation defaults
MIN_BPM:           int = 75
MAX_BPM:           int = 100
VALID_KEYS:      tuple = 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab'
TIME_SIGNATURES: tuple = (4,4),(4,4)

# Instrument volume adjustments
KICK_VOLUME:      int = -3
HAT_VOLUME:       int = -10
SNARE_VOLUME:     int = -3
NO_VOLUME_CHANGE: int = 0

# MIDI note durations
BASE_NOTE:      int = 480 - 1 # note length in ticks (480 ticks per beat)
QTR_NOTE:       int = BASE_NOTE
HALF_NOTE:      int = BASE_NOTE * 2
WHOLE_NOTE:     int = BASE_NOTE * 4
EIGHTH_NOTE:    int = BASE_NOTE // 2
SIXTEENTH_NOTE: int = BASE_NOTE // 4
DOT_QTR_NOTE:   int = int(BASE_NOTE * 1.5)
DOT_8TH_NOTE:   int = int(BASE_NOTE * 0.75)

# Melody complexities
BASS_COMPLEXITY:    int = 1
AMBIENT_COMPLEXITY: int = 2
CMELODY_COMPLEXITY: int = 3
MELODY_COMPLEXITY:  int = 4

# Music structures
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
    ('vi', 'V', 'IV', 'V'),
    ('vi', 'vii', 'V', 'vi')
)
SONG_STRUCTURES:    tuple = (
    (
        (0,0,0,0,0,1,1,1,1,1,1),    # Ambient
        (0,0,0,1,1,0,0,1,1,1,1),    # Melody
        (0,0,0,0,0,0,0,1,1,1,1),    # Countermelody
        (1,1,1,1,1,1,1,1,1,1,1),    # Chords
        (0,1,1,1,1,0,1,1,1,1,1),    # Bass
        (0,1,1,1,1,0,1,1,1,1,1)     # Drums
    ),
    (
        (0,0,1,1,0,0,1,1,1,1,1,1,0,0),
        (0,0,0,0,1,1,0,0,1,1,1,1,0,0),
        (0,0,0,0,0,0,0,0,0,0,0,0,0,0),
        (1,1,1,1,1,1,1,1,1,1,1,1,1,1),
        (0,0,1,1,1,1,1,1,1,1,1,1,0,0),
        (0,1,1,1,1,1,0,0,1,1,1,1,0,0)
    ),
    (
        (0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1),
        (0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1),
        (0,0,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1),
        (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),
        (1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1),
        (0,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1)
    ),
    (
        (0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0),
        (0,0,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1),
        (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
        (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),
        (0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0),
        (0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0)
    ),
    (
        (0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0),
        (0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1),
        (0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0),
        (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),
        (0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0),
        (0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0)
    )
)
