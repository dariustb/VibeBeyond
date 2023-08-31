'''seg_gen.py - This file will generate song segments'''

# pylint: disable = W0401, W0614, E0611

import os
import random

from pydub import AudioSegment
from ..    import constants as const

class SongSegmentGen: # pylint: disable = R0903
    ''' This class is for generating song segments (excluding drum loop) '''
    def __init__(self) -> None:
        ''' All the song's segment attributes will be kept here '''

        # Song structure
        self.song_structure: tuple = random.choice(const.SONG_STRUCTURES)

        # Pydub audio segments
        self.ambient_segment: AudioSegment = None
        self.melody_segment:  AudioSegment = None
        self.cmelody_segment: AudioSegment = None
        self.chords_segment:  AudioSegment = None
        self.drum_segment:    AudioSegment = None

    def gen_segment(self, track_structure: tuple, audio_path: str,
                    volume: int = const.NO_VOLUME_CHANGE):
        ''' Builds the segments based on the track's structure '''
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
