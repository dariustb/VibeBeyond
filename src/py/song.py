''' song.py - This file will be used to generate a song '''

# pylint: disable = W0401, W0613, W0614, R0902, R0913, R0914, C0103

import os
import random
from string import ascii_lowercase as letters

import mido
import sf2_loader
from pydub import AudioSegment

from py import song_utils as util
from py.constants import *

class SongElements:
    ''' This class will hold the song's musical elements + setters/getters '''
    def __init__(self):
        ''' All the song's element attributes will be kept here '''

        # Song generation info
        self.key:  str = self.set_key()
        self.time: str = self.set_time()
        self.bpm:  str = self.set_bpm() # tempo = mido.bpm2tempo(bpm) =/= bpm
        self.prog: str = self.set_prog()

    # SETTER FUNCTIONS
    def set_key(self):
        ''' Returns randomly chosen key '''
        return random.choice(VALID_KEYS)

    def set_time(self):
        ''' Returns randomly chosen time signature '''
        return random.choice(TIME_SIGNATURES)

    def set_bpm(self):
        ''' Returns randomly chosen bpm '''
        return random.randint(MIN_BPM, MAX_BPM)

    def set_prog(self):
        ''' Returns randomly chosen chord progression '''
        return random.choice(CHORD_PROGRESSIONS)

class SongMidiGen:
    ''' This class is for generating MIDI loop files '''
    def __init__(self) -> None:
        ''' All the song's MIDI attributes will be kept here '''

        # Midi Tracks
        self.chords_midi_track:  mido.MidiTrack = None
        self.ambient_midi_track: mido.MidiTrack = None
        self.melody_midi_track:  mido.MidiTrack = None
        self.cmelody_midi_track: mido.MidiTrack = None
        self.bass_midi_track:    mido.MidiTrack = None

        # Midi file paths
        self.ambient_midi_path: str = self.set_path('ambient')
        self.melody_midi_path:  str = self.set_path('melody')
        self.cmelody_midi_path: str = self.set_path('cmelody')
        self.chords_midi_path:  str = self.set_path('chords')
        self.bass_midi_path:    str = self.set_path('bass')

    # SETTER FUNCTIONS
    def set_path(self, name: str) -> str:
        ''' Returns a file path based on parameters '''
        return MIDI_FOLDER + name + '_midi' + MIDI_FILE_TYPE

    # GENERATION FUNCTIONS
    def gen_track_prefix(self, key, time, bpm) -> mido.MidiTrack:
        ''' Add necessary info to the beginnning of midi track '''

        # Create track
        track = mido.MidiTrack()

        # Add Messages / MetaMessages to file
        # Not sure why yet, but MuseScore does this, and it allows the sound to play
        track.append(mido.MetaMessage('track_name', name='song_track', time=0))
        track.append(mido.MetaMessage('time_signature',
                                    numerator = time[0], denominator = time[1],
                                    clocks_per_click = 24, notated_32nd_notes_per_beat = 8,
                                    time = 0
                                    ))
        track.append(mido.MetaMessage('key_signature', key=key, time=0))
        track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(bpm), time=0))
        track.append(mido.Message('control_change', channel=0, control=121, value=0, time=0))
        track.append(mido.Message('program_change', channel=0, program=4, time=0))
        track.append(mido.Message('control_change', channel=0, control=7, value=100, time=0))
        track.append(mido.Message('control_change', channel=0, control=10, value=64, time=0))
        track.append(mido.Message('control_change', channel=0, control=91, value=0, time=0))
        track.append(mido.Message('control_change', channel=0, control=93, value=0, time=0))
        track.append(mido.MetaMessage('midi_port', port=0, time=0))

        return track

    def gen_chords(self, key, time, bpm, prog) -> mido.MidiTrack:
        ''' Returns a MIDI track of the chord progression '''

        # Get chord progression variables
        chord_intervals_list    = util.get_chord_intervals_list(prog)
        root_note_list          = util.get_root_note_list(key, prog)

        chords = self.gen_track_prefix(key, time, bpm)

        # Add notes in chord to midi track
        for root_note in root_note_list:

            # Get chord intervals
            temp_list = chord_intervals_list.copy() # copy list so we don't pop from original
            chord_intervals = temp_list.pop(0)

            # Add note_on: sets the attack time for note (time=0 is instant)
            for i, note_interval in enumerate(chord_intervals):
                note_start_time = 1 if i == 0 else 0
                chords.append(mido.Message(
                    'note_on',
                    note = root_note + note_interval,
                    velocity = 100,
                    time = note_start_time
                ))

            # Add note_off: sets the release time for note (time=0 is instant)
            for i, note_interval in enumerate(chord_intervals):
                note_stop_time = WHOLE_NOTE if i == 0 else 0
                chords.append(mido.Message(
                    'note_off',
                    note = root_note + note_interval,
                    velocity = 0,
                    time = note_stop_time
                ))

        return chords

    def gen_melody(self, key, time, bpm, prog, complexity) -> mido.MidiTrack:
        ''' Returns a generated melody '''
        if complexity >= 3:
            note_durations: tuple = EIGHTH_NOTE, QTR_NOTE, DOT_QTR_NOTE, HALF_NOTE, WHOLE_NOTE
        elif complexity == 2:
            note_durations: tuple = QTR_NOTE, HALF_NOTE, WHOLE_NOTE
        elif complexity == 1:
            note_durations: tuple = WHOLE_NOTE, WHOLE_NOTE
        shortest_subdivision = note_durations[0]

        intervals = util.get_chord_intervals_list(prog)
        roots = util.get_root_note_list(key, prog)

        rhythm = []
        melody = []

        track: mido.MidiTrack = self.gen_track_prefix(key, time, bpm)

        for _ in range(len(prog)):
            root_note = roots.pop()
            chord_intervals = intervals.pop()
            scale_notes = chord_intervals
            measure_length = time[0] * (WHOLE_NOTE / time[1])
            while measure_length >= shortest_subdivision:
                # Add note durations to make rhythm
                note = random.choice(note_durations)
                if measure_length < note:
                    continue
                rhythm.append(note)
                measure_length -= note

                # Add notes pitch to make melody
                pitch = root_note + random.choice(scale_notes)
                melody.append(pitch)

                # Add MIDI value to track
                track.append(mido.Message(
                    'note_on',
                    note = pitch,
                    velocity = 100,
                    time = 1
                ))
                track.append(mido.Message(
                    'note_off',
                    note = pitch,
                    velocity = 0,
                    time = note
                ))

        return track

    # EXPORT FUNCTIONS
    def export_midi_from_tracks(self, midi_track: mido.MidiTrack, midi_path: str) -> str:
        ''' Combines the midi tracks into MidiFile & saves to .mid file '''
        if midi_track is None:
            return None

        file = mido.MidiFile()

        file.tracks.append(midi_track)
        file.save(midi_path)

        return midi_path

class SongLoopGen:
    ''' This class is for generating Audio loop files '''
    def __init__(self) -> None:
        ''' All the song's loop attributes will be kept here '''

        # Instruments/Sample names
        self.ambient_name: str = self.set_name(AMBIENT_FOLDER)
        self.melody_name:  str = self.set_name(MELODY_FOLDER)
        self.cmelody_name: str = self.set_name(CMELODY_FOLDER)
        self.chords_name:  str = self.set_name(CHORDS_FOLDER)
        self.bass_name:    str = self.set_name(BASS_FOLDER)
        self.kick_name:    str = self.set_name(KICK_FOLDER)
        self.hat_name:     str = self.set_name(HAT_FOLDER)
        self.snare_name:   str = self.set_name(SNARE_FOLDER)

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
        return AUDIO_FOLDER + name + '_loop' + AUDIO_FILE_TYPE

    # GENERATION FUNCTIONS
    def gen_drum_loop(self, prog, bpm) -> AudioSegment:
        ''' Adds a midi drum loop to the class variable '''

        bpm_in_ms = int(60 / bpm * 1000) # milliseconds per beat

        # Load drum samples
        kick_audio  = AudioSegment.from_file(self.kick_name)  + KICK_VOLUME
        hat_audio   = AudioSegment.from_file(self.hat_name)   + HAT_VOLUME
        snare_audio = AudioSegment.from_file(self.snare_name) + SNARE_VOLUME

        # Create drum pattern for midi
        kick_pattern = [HALF_NOTE + EIGHTH_NOTE, DOT_QTR_NOTE]
        hat_pattern  = [EIGHTH_NOTE for _ in range(8)]

        # Coordinate audio samples to note values
        kick_segment  = []
        snare_segment = []
        hat_segment   = []

        for _ in range(len(prog)):
            util.coordinate_sample(kick_audio, kick_segment, kick_pattern, bpm_in_ms)
            util.coordinate_sample(hat_audio, hat_segment, hat_pattern, bpm_in_ms)
            util.coordinate_snare(snare_audio, snare_segment, bpm_in_ms)

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
            format=AUDIO_TYPE)

        return loop_path

    def export_loop_from_segment(self, segment: AudioSegment, loop_path: str) -> str:
        ''' creates an audio file with all the AudioSegments combined '''        
        segment.export(loop_path, format=AUDIO_TYPE)
        return loop_path

class SongSegmentGen: # pylint: disable = R0903
    ''' This class is for generating song segments (excluding drum loop) '''
    def __init__(self) -> None:
        ''' All the song's segment attributes will be kept here '''

        # Song structure
        self.song_structure: tuple = random.choice(SONG_STRUCTURES)

        # Pydub audio segments
        self.ambient_segment: AudioSegment = None
        self.melody_segment:  AudioSegment = None
        self.cmelody_segment: AudioSegment = None
        self.chords_segment:  AudioSegment = None
        self.drum_segment:    AudioSegment = None

    def gen_segment(self, track_structure: tuple, audio_path: str, volume: int = NO_VOLUME_CHANGE):
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

def delete_loops(Midi: SongMidiGen, Loop: SongLoopGen) -> bool:
    ''' deletes audio/midi files of the song loops '''
    for loop_file in (
        Midi.ambient_midi_path,
        Midi.melody_midi_path,
        Midi.cmelody_midi_path,
        Midi.chords_midi_path,
        Midi.bass_midi_path,
        Loop.ambient_loop_path,
        Loop.melody_loop_path,
        Loop.cmelody_loop_path,
        Loop.chords_loop_path,
        Loop.bass_loop_path,
        Loop.drum_loop_path,
    ):
        if os.path.isfile(loop_file):
            os.remove(loop_file)
    return True
