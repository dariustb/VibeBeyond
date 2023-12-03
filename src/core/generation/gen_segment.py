""" gen_segment - This file will generate song segments"""

import os
import random

from pydub import AudioSegment

# Constant variables
NO_VOLUME_CHANGE: int = 0
SONG_STRUCTURES: tuple = (
    {
        "melody": (0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1),
        "chords": (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        "drums": (0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1),
    },
    {
        "melody": (0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0),
        "chords": (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        "drums": (0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0),
    },
    {
        "melody": (0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1),
        "chords": (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        "drums": (0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1),
    },
    {
        "melody": (0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1),
        "chords": (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        "drums": (0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0),
    },
    {
        "melody": (0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        "chords": (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        "drums": (0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0),
    },
)


class SongSegmentGen:  # pylint: disable = R0903
    """This class is for generating song segments (excluding drum loop)"""

    def __init__(self) -> None:
        """All the song's segment attributes will be kept here"""

        # Song structure
        self.song_structure: dict = random.choice(SONG_STRUCTURES)

        # Pydub audio segments
        self.melody_segment: AudioSegment = None
        self.chords_segment: AudioSegment = None
        self.drum_segment: AudioSegment = None

    def gen_segment(
        self,
        track_structure: tuple,
        audio_path: str,
        volume: int = NO_VOLUME_CHANGE,
    ) -> AudioSegment:
        """Builds the segments based on the track's structure"""
        if not os.path.isfile(audio_path):
            return None

        audio = AudioSegment.from_file(audio_path) + volume
        segment = []
        for value in track_structure:
            if value:
                segment.append(audio)
            else:
                segment.append(AudioSegment.silent(len(audio)))
        segment = sum(segment)
        return segment
