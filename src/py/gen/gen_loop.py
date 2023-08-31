''' loop_gen.py - This file will generate AudioSegment loops '''

# pylint: disable = W0401, W0614, R0902

import os
import random
import sf2_loader
import mido

from pydub import AudioSegment
from .     import gen_util
from ..    import constants as const

class SongLoopGen:
    ''' This class is for generating Audio loop files '''
    def __init__(self) -> None:
        ''' All the song's loop attributes will be kept here '''

        # Instruments/Sample names
        self.ambient_name: str = self.set_name(const.AMBIENT_FOLDER)
        self.melody_name:  str = self.set_name(const.MELODY_FOLDER)
        self.cmelody_name: str = self.set_name(const.CMELODY_FOLDER)
        self.chords_name:  str = self.set_name(const.CHORDS_FOLDER)
        self.bass_name:    str = self.set_name(const.BASS_FOLDER)
        self.kick_name:    str = self.set_name(const.KICK_FOLDER)
        self.hat_name:     str = self.set_name(const.HAT_FOLDER)
        self.snare_name:   str = self.set_name(const.SNARE_FOLDER)

        # Audio file paths
        self.ambient_loop_path: str = self.set_path('ambient')
        self.melody_loop_path:  str = self.set_path('melody')
        self.cmelody_loop_path: str = self.set_path('cmelody')
        self.chords_loop_path:  str = self.set_path('chords')
        self.bass_loop_path:    str = self.set_path('bass')
        self.drum_loop_path:    str = self.set_path('drum')

    # SETTER FUNCTIONS
    def set_name(self, folder) -> str:
        ''' Returns soundfont/sample name '''
        if not os.path.isdir(folder) or os.listdir(folder) == []:
            return ''
        return folder + random.choice(os.listdir(folder))

    def set_path(self, name: str) -> str:
        ''' Returns a file path based on parameters '''
        return const.AUDIO_FOLDER + name + '_loop' + const.AUDIO_FILE_TYPE

    # GENERATION FUNCTIONS
    def gen_drum_loop(self, prog, bpm) -> AudioSegment:
        ''' Adds a midi drum loop to the class variable '''

        bpm_in_ms = int(60 / bpm * 1000) # milliseconds per beat

        # Load drum samples
        kick_audio  = AudioSegment.from_file(self.kick_name)  + const.KICK_VOLUME
        hat_audio   = AudioSegment.from_file(self.hat_name)   + const.HAT_VOLUME
        snare_audio = AudioSegment.from_file(self.snare_name) + const.SNARE_VOLUME

        # Create drum pattern for midi
        kick_pattern = [const.HALF_NOTE + const.EIGHTH_NOTE, const.DOT_QTR_NOTE]
        hat_pattern  = [const.EIGHTH_NOTE for _ in range(8)]

        # Coordinate audio samples to note values
        kick_segment  = []
        snare_segment = []
        hat_segment   = []

        for _ in range(len(prog)):
            gen_util.coordinate_sample(kick_audio, kick_segment, kick_pattern, bpm_in_ms)
            gen_util.coordinate_sample(hat_audio, hat_segment, hat_pattern, bpm_in_ms)
            gen_util.coordinate_snare(snare_audio, snare_segment, bpm_in_ms)

        # Combine sample and silences (per instrument)
        kick_segment  = sum(kick_segment)
        snare_segment = sum(snare_segment)
        hat_segment   = sum(hat_segment)

        # Combine all the drum instruments
        drum_segment = kick_segment
        drum_segment = drum_segment.overlay(snare_segment, 0)
        drum_segment = drum_segment.overlay(hat_segment, 0)

        # return the segment to mix with other instruments for export later
        return drum_segment

    # EXPORT FUNCTIONS
    def export_loop_from_midi(self,
                              midi_path: str, midi_track: mido.MidiTrack,
                              loop_path: str, sf2_name: str) -> str:
        ''' midi_to_audio - Convert any given MIDI track file to audio files '''

        # NOTE: sf2-loader/pydub requires ffmpeg or libav installed
        # for non-wav files (https://pypi.org/project/sf2-loader/#Windows)

        if midi_track is None:
            return None

        loader = sf2_loader.sf2_loader(sf2_name)
        loader < loader.get_current_instrument() # pylint: disable = W0106
        loader.export_midi_file(midi_path,
            decay=0.0,
            name=loop_path,
            format=const.AUDIO_TYPE)

        return loop_path

    def export_loop_from_segment(self, segment: AudioSegment, loop_path: str) -> str:
        ''' creates an audio file with all the AudioSegments combined '''        
        segment.export(loop_path, format=const.AUDIO_TYPE)
        return loop_path
