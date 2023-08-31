''' midi_gen.py - This file will generate midi files'''

# pylint: disable = W0401, W0614, R0902, R0913, R0914

import random
import mido

from py.constants import *
from py import util

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
