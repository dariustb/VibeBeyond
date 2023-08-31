''' '''

import random

from pydub import AudioSegment
from string import ascii_lowercase as letters

from py.seg_gen import SongSegmentGen
from py.constants import *

class SongCombine:
    ''' This class is for combining all the song segments into final audio '''
    def __init__(self) -> None:
        ''' All the song's final attributes will be kept here '''

        # Metadata
        self.title:  str = ''.join(random.choice(letters) for _ in range(8)).title()
        self.artist: str = 'example artist'.title()

        # Audio segment
        self.song_segment: AudioSegment = None

        # Audio file paths
        self.song_path: str = AUDIO_FOLDER + self.title + AUDIO_FILE_TYPE

    def combine_segments(self, Segments:SongSegmentGen) -> AudioSegment:
        ''' Combines segments into one whole segment '''
        song_duration = len(Segments.drum_segment)
        self.song_segment = AudioSegment.silent(song_duration)

        if Segments.ambient_segment is not None:
            self.song_segment = self.song_segment.overlay(Segments.ambient_segment,0)
        if Segments.melody_segment is not None:
            self.song_segment = self.song_segment.overlay(Segments.melody_segment,0)
        if Segments.cmelody_segment is not None:
            self.song_segment = self.song_segment.overlay(Segments.cmelody_segment,0)
        if Segments.chords_segment is not None:
            self.song_segment = self.song_segment.overlay(Segments.chords_segment,0)
        if Segments.drum_segment is not None:
            self.song_segment = self.song_segment.overlay(Segments.drum_segment,0)

        return self.song_segment

    # EXPORT FUNCTIONS
    def export_audio_from_segment(self) -> str:
        ''' creates an audio file with all the AudioSegments combined '''        
        self.song_segment.export(self.song_path, format=AUDIO_TYPE)
        return self.song_path
