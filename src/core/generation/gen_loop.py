""" gen_loop_inst - This file will convert midi into audio clips/loops """

import os
import random

import sf2_loader
from mido import MidiTrack
from pydub import AudioSegment

from . import gen_midi

# Constant variables
AUDIO_TYPE: str = "wav"
AUDIO_FOLDER: str = "src/gen/audio/"
CHORDS_FOLDER: str = "src/assets/sf2/chords/"
MELODY_FOLDER: str = "src/assets/sf2/melody/"

KICK_FOLDER: str = "src/assets/drums/kick/"
HAT_FOLDER: str = "src/assets/drums/hat/"
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

    # Getter Functions
    def get_sf2_preset_number(self, sf2_instrument: str) -> int:
        """Returns the sf2's current instrument's preset number"""
        loader = sf2_loader.sf2_loader(sf2_instrument)
        return loader.current_preset

    # Export Functions
    def export_loop_from_midi(
        self, midi_path: str, midi_track: MidiTrack, loop_path: str, sf2_instrument: str
    ) -> str:
        """midi_to_audio - Convert any given MIDI track file to audio files"""

        # NOTE: sf2-loader/pydub requires ffmpeg or libav installed
        # for non-wav files (https://pypi.org/project/sf2-loader/#Windows)

        if midi_track is None:
            return None

        loader = sf2_loader.sf2_loader(sf2_instrument)
        if len(loader.all_instruments()) > 0:
            loader < loader.get_current_instrument()  # < changes instrument in loader
            loader.export_midi_file(
                midi_path, decay=0.0, name=loop_path, format=AUDIO_TYPE
            )
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

    # Generation Functions
    def gen_drum_loop(self, prog: tuple, bpm: int) -> AudioSegment:
        """Adds a midi drum loop to the class variable"""

        bpm_in_ms = int(60 / bpm * 1000)  # milliseconds per beat

        # Load drum samples
        kick_audio = AudioSegment.from_file(self.kick_name)
        hat_audio = AudioSegment.from_file(self.hat_name) - 10
        snare_audio = AudioSegment.from_file(self.snare_name)

        # Create drum pattern for midi
        kick_pattern = (
            gen_midi.MIDI_HALF_NOTE + gen_midi.MIDI_8TH_NOTE,
            gen_midi.MIDI_DOT_QTR_NOTE,
        )
        hat_pattern = (gen_midi.MIDI_8TH_NOTE for _ in range(8))

        # Coordinate audio samples to note values
        kick_segment = []
        snare_segment = []
        hat_segment = []

        for _ in range(len(prog)):
            coordinate_sample(kick_audio, kick_segment, kick_pattern, bpm_in_ms)
            coordinate_sample(hat_audio, hat_segment, hat_pattern, bpm_in_ms)
            coordinate_snare(snare_audio, snare_segment, bpm_in_ms)

        # Combine sample and silences (per instrument)
        kick_segment = sum(kick_segment)
        snare_segment = sum(snare_segment)
        hat_segment = sum(hat_segment)

        # Combine all the drum instruments
        drum_segment = kick_segment
        drum_segment = drum_segment.overlay(snare_segment, 0)
        drum_segment = drum_segment.overlay(hat_segment, 0)

        # return the segment to mix with other instruments for export later
        return drum_segment

    # Export Functions
    def export_loop_from_segment(self, segment: AudioSegment, loop_path: str) -> str:
        """creates an audio file with all the AudioSegments combined"""
        if segment is None:
            return None

        segment.export(out_f=loop_path, format=AUDIO_TYPE)
        return loop_path


# Free Functions
def coordinate_sample(
    audio: AudioSegment, segment: AudioSegment, pattern: tuple, bpm_in_ms: int
) -> None:
    """coordinates sample audio to the rhythmic pattern passed in"""
    for note in pattern:
        note_length_in_ms = ((note + 1) / gen_midi.MIDI_BASE_NOTE) * bpm_in_ms
        if len(audio) < note_length_in_ms:
            segment.append(audio)
            segment.append(AudioSegment.silent(note_length_in_ms - len(audio)))
        elif len(audio) > note_length_in_ms:
            shortened_audio = audio[:note_length_in_ms]
            segment.append(shortened_audio)


def coordinate_snare(
    audio: AudioSegment, segment: AudioSegment, bpm_in_ms: int
) -> None:
    """coordinates snare to the 2 and 4 of the beat"""
    note_length_in_ms = (
        (gen_midi.MIDI_HALF_NOTE + 1) / gen_midi.MIDI_BASE_NOTE
    ) * bpm_in_ms  # half note length
    segment.append(AudioSegment.silent(note_length_in_ms / 2))
    segment.append(audio)
    segment.append(AudioSegment.silent(note_length_in_ms - len(audio)))
    segment.append(audio)
    segment.append(AudioSegment.silent(note_length_in_ms / 2 - len(audio)))
