""" gen_combine - This file will combine song segments """

from pydub import AudioSegment

from .gen_segment import SongSegmentGen

# Constant variables
AUDIO_FOLDER: str = "src/gen/audio"
AUDIO_FILE_TYPE: str = ".wav"
AUDIO_TYPE: str = "wav"


class SongCombine:
    """This class is for combining all the song segments into final audio"""

    def __init__(self) -> None:
        """All the song's final attributes will be kept here"""

        # Audio segment
        self.song_segment: AudioSegment = None

        # Audio file paths
        self.song_path: str = AUDIO_FOLDER + "song" + AUDIO_FILE_TYPE

    def combine_segments(self, Segments: SongSegmentGen) -> AudioSegment:
        """Combines segments into one whole segment"""
        song_duration = len(Segments.drum_segment)
        self.song_segment = AudioSegment.silent(song_duration)

        if Segments.ambient_segment is not None:
            self.song_segment = self.song_segment.overlay(Segments.ambient_segment, 0)
        if Segments.melody_segment is not None:
            self.song_segment = self.song_segment.overlay(Segments.melody_segment, 0)
        if Segments.cmelody_segment is not None:
            self.song_segment = self.song_segment.overlay(Segments.cmelody_segment, 0)
        if Segments.chords_segment is not None:
            self.song_segment = self.song_segment.overlay(Segments.chords_segment, 0)
        if Segments.drum_segment is not None:
            self.song_segment = self.song_segment.overlay(Segments.drum_segment, 0)

        return self.song_segment

    # EXPORT FUNCTIONS
    def export_audio_from_segment(self) -> str:
        """creates an audio file with all the AudioSegments combined"""
        self.song_segment.export(self.song_path, format=AUDIO_TYPE)
        return self.song_path
