""" gen_elements - This file will produce elements for song creation """

import random

# Constant variables
MIN_BPM: int = 75
MAX_BPM: int = 100
VALID_KEYS: tuple = ("A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab")
VALID_TIME_SIGNATURES: tuple = (4, 4), (4, 4)
VALID_CHORD_PROGRESSIONS: tuple = (
    ("ii", "V", "I", "IV"),
    ("ii7", "V", "I7", "I7"),
    ("ii", "V7", "iii", "vi"),
    ("iii", "vi", "IV", "I"),
    ("IV", "I", "ii", "vi"),
    ("IV", "I", "iii", "IV"),
    ("IV", "I", "V", "vi"),
    ("IV", "IV", "I", "V"),
    ("IV", "vi", "I", "V"),
    ("IV", "vi", "iii", "I"),
    ("V", "I", "vi", "V"),
    ("V", "IV", "vi", "I"),
    ("V", "vi", "IV", "I"),
    ("vi", "bVI", "bVII", "I"),
    ("vi", "ii", "V", "I"),
    ("vi", "IV", "I", "V"),
    ("vi", "V", "IV", "V"),
    ("vi", "vii", "V", "vi"),
)


class SongElements:
    """This class will hold the song's musical elements + setters/getters"""

    def __init__(self) -> None:
        """All the song's elements will be kept here"""

        # Song generation info
        self.key: str = self.set_key()
        self.time: str = self.set_time()
        self.bpm: int = self.set_bpm()  # tempo = mido.bpm2tempo(bpm) =/= bpm
        self.prog: tuple = self.set_prog()

    # Setter Functions
    def set_key(self):
        """Returns randomly chosen key"""
        return random.choice(VALID_KEYS)

    def set_time(self):
        """Returns randomly chosen time signature"""
        return random.choice(VALID_TIME_SIGNATURES)

    def set_bpm(self):
        """Returns randomly chosen BPM"""
        return random.randint(MIN_BPM, MAX_BPM)

    def set_prog(self):
        """Returns randomly chosen chord progression"""
        return random.choice(VALID_CHORD_PROGRESSIONS)
