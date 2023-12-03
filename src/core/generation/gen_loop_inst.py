""" gen_loop_inst - This file will convert midi into audio clips/loops """

import os
import random

import sf2_loader
from mido import MidiTrack
from pydub import AudioSegment

# Constant variables
AUDIO_TYPE: str = "wav"
AUDIO_FOLDER: str = "src/gen/audio/"
CHORDS_FOLDER: str = "src/assets/sf2/chords/"
MELODY_FOLDER: str = "src/assets/sf2/melody/"

KICK_FOLDER: str = "src/assets/drums/kicks/"
HAT_FOLDER: str = "src/assets/drums/hats/"
SNARE_FOLDER: str = "src/assets/drums/snare/"


class SongLoopGen:
    """This class is for generation audio loop files"""

    def __init__(self) -> None:
        """All the song's loop attributes will be kept here"""

        # Instrument names
        self.chords_instrument: str = self.set_name(CHORDS_FOLDER)
        self.melody_instrument: str = self.set_name(MELODY_FOLDER)

        # Audio file paths
        self.chords_loop_path: str = self.set_path("chords")
        self.melody_loop_path: str = self.set_path("melody")

    # Setter Functions
    def set_name(self, folder: str) -> str:
        """Returns soundfont name"""
        if not os.path.isdir(folder) or os.listdir(folder) == []:
            return ""
        return folder + random.choice(os.listdir(folder))

    def set_path(self, name: str) -> str:
        """Returns a file path based on parameters"""
        return AUDIO_FOLDER + name + "_loop.wav"

    # Export Functions
    def export_loop_from_midi(
        self, midi_path: str, midi_track: MidiTrack, loop_path: str, sf2_name: str
    ) -> str:
        """midi_to_audio - Convert any given MIDI track file to audio files"""

        # NOTE: sf2-loader/pydub requires ffmpeg or libav installed
        # for non-wav files (https://pypi.org/project/sf2-loader/#Windows)

        if midi_track is None:
            return None

        loader = sf2_loader.sf2_loader(sf2_name)
        if loader.all_instruments():
            loader < loader.get_current_instrument()  # < changes instrument in loader
        loader.export_midi_file(midi_path, decay=0.0, name=loop_path, format=AUDIO_TYPE)

        return loop_path


class DrumLoopGen(SongLoopGen):
    """This class is for generation audio loop files"""

    def __init__(self) -> None:
        """All the Drum's loop attributes will be kept here"""
        SongLoopGen.__init__(self)

        # Drum Samples names
        self.kick_name: str = self.set_name(KICK_FOLDER)
        self.hat_name: str = self.set_name(HAT_FOLDER)
        self.snare_name: str = self.set_name(SNARE_FOLDER)

        # Audio file paths
        self.drum_loop_path: str = self.set_path("drums")

    # Export Functions
    def export_loop_from_segment(self, segment: AudioSegment, loop_path: str) -> str:
        """creates an audio file with all the AudioSegments combined"""
        if segment is None:
            return None

        segment.export(loop_path, format=AUDIO_TYPE)
        return loop_path
