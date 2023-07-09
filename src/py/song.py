''' song.py - This file will be used to generate a song '''

# pylint: disable = W0401, W0614, R0902

import random
import os
from string import ascii_lowercase as letters

import mido
from pydub import AudioSegment
from py import info
from py import soundfont as sf2
from py import song_utils as util
from py.constants import *

class Song:
    ''' This class will be used to generate a song'''
    def __init__(self):
        ''' All the song's static variables will be kept here '''

        # Metadata
        self.title:  str = ''.join(random.choice(letters) for _ in range(8)).title()
        self.artist: str = 'example Artist'.title()

        # Song generation info
        self.key:      str = random.choice(VALID_KEYS)
        self.bpm:      str = random.randint(MIN_BPM, MAX_BPM) # tempo = mido.bpm2tempo(bpm) =/= bpm
        self.time_sig: str = random.choice(TIME_SIGNATURES)
        self.prog:     str = random.choice(CHORD_PROGRESSIONS)

        # Midi tracks
        self.mid_prog_track: mido.MidiTrack = self.set_track_prefix()
        self.mid_lead_track: mido.MidiTrack = None
        self.mid_bass_track: mido.MidiTrack = None

        # Pydub audio segments
        self.prog_segment: AudioSegment = None
        self.lead_segment: AudioSegment = None
        self.drum_segment: AudioSegment = None

        # File info
        self.mid: mido.MidiFile = mido.MidiFile()
        self.mid_path:  str = MIDI_FOLDER + self.title + MIDI_FILE_TYPE
        self.song_path: str = AUDIO_FOLDER + 'song.' + AUDIO_FILE_TYPE

    # SETTER FUNCTIONS
    def set_track_prefix(self) -> mido.MidiTrack:
        ''' Add necessary info to the beginnning of midi track '''

        # Create track
        track = mido.MidiTrack()

        # Add Messages / MetaMessages to file
        # Not sure why yet, but MuseScore does this, and it allows the sound to play
        track.append(mido.MetaMessage('track_name', name='song_track', time=0))
        track.append(mido.MetaMessage('time_signature',
                                    numerator = self.time_sig[0], denominator = self.time_sig[1],
                                    clocks_per_click = 24, notated_32nd_notes_per_beat = 8,
                                    time = 0
                                    ))
        track.append(mido.MetaMessage('key_signature', key=self.key, time=0))
        track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(self.bpm), time=0))
        track.append(mido.Message('control_change', channel=0, control=121, value=0, time=0))
        track.append(mido.Message('program_change', channel=0, program=4, time=0))
        track.append(mido.Message('control_change', channel=0, control=7, value=100, time=0))
        track.append(mido.Message('control_change', channel=0, control=10, value=64, time=0))
        track.append(mido.Message('control_change', channel=0, control=91, value=0, time=0))
        track.append(mido.Message('control_change', channel=0, control=93, value=0, time=0))
        track.append(mido.MetaMessage('midi_port', port=0, time=0))

        return track

    # GENERATION FUNCTIONS
    def gen_chord_prog(self) -> bool:
        ''' Adds a chord progression to the class variable '''

        # Get chord progression variables
        chord_intervals_list    = util.get_chord_intervals_list(self.prog)
        root_note_list          = util.get_root_note_list(self.key, self.prog)

        # Repeat chord progression for length of song
        for _ in range(SONG_LENGTH):

            # Add notes in chord to midi track
            for root_note in root_note_list:

                # Get chord intervals
                temp_list = chord_intervals_list.copy() # copy list so we don't pop from original
                chord_intervals = temp_list.pop(0)

                # Add note_on: sets the attack time for note (time=0 is instant)
                for i, note_interval in enumerate(chord_intervals):
                    note_start_time = 1 if i == 0 else 0
                    self.mid_prog_track.append(mido.Message(
                        'note_on',
                        note = root_note + note_interval,
                        velocity = 80,
                        time = note_start_time
                    ))

                # Add note_off: sets the release time for note (time=0 is instant)
                for i, note_interval in enumerate(chord_intervals):
                    note_stop_time = WHOLE_NOTE if i == 0 else 0
                    self.mid_prog_track.append(mido.Message(
                    'note_off',
                    note = root_note + note_interval,
                    velocity = 0,
                    time = note_stop_time
                    ))

        return True

    def gen_drum_loop(self) -> bool:
        ''' Adds a midi drum loop to the class variable '''

        bpm_in_ms = int(60 / self.bpm * 1000) # milliseconds per beat

        # Load drum samples
        kick_file  = random.choice(os.listdir(KICK_FOLDER))
        hat_file   = random.choice(os.listdir(HAT_FOLDER))
        snare_file = random.choice(os.listdir(SNARE_FOLDER))

        kick_audio  = AudioSegment.from_file(KICK_FOLDER + kick_file)
        hat_audio   = AudioSegment.from_file(HAT_FOLDER + hat_file) - 6
        snare_audio = AudioSegment.from_file(SNARE_FOLDER + snare_file) - 3

        print('\n\n\nkick:', kick_file, '\nhat:', hat_file, '\nsnare:', snare_file)

        # Create drum pattern for midi
        kick_pattern = [HALF_NOTE + EIGHTH_NOTE, DOT_QTR_NOTE]
        hat_pattern  = [EIGHTH_NOTE for _ in range(8)]

        # Coordinate audio samples to note values
        kick_segment  = []
        snare_segment = []
        hat_segment   = []

        for _ in range(len(self.prog)):
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

        # Save the segment to mix with other instruments for export later
        self.drum_segment = drum_segment

        return True

    # EXPORT FUNCTIONS
    def save_midi_file(self, midi_file_name: str = None) -> str:
        ''' Combines the midi tracks into MidiFile & saves to .mid file '''
        if self.mid_prog_track is not None:
            self.mid.tracks.append(self.mid_prog_track)
        if self.mid_lead_track is not None:
            self.mid.tracks.append(self.mid_lead_track)
        if self.mid_bass_track is not None:
            self.mid.tracks.append(self.mid_bass_track)

        if midi_file_name is None:
            midi_file_name = MIDI_FOLDER + self.title + MIDI_FILE_TYPE
        self.mid.save(midi_file_name)

        return midi_file_name

    def export_song(self) -> bool:
        ''' creates an audio file with all the AudioSegments combined '''
        song_duration = len(self.drum_segment)
        final_audio = AudioSegment.silent(song_duration)

        if self.prog_segment is not None:
            final_audio = final_audio.overlay(self.prog_segment,0)
        if self.lead_segment is not None:
            final_audio = final_audio.overlay(self.lead_segment,0)
        if self.drum_segment is not None:
            final_audio = final_audio.overlay(self.drum_segment,0)

        final_audio.export(self.song_path, format=AUDIO_FILE_TYPE)

# The feast de resistance
def create_song(debug: bool = False):
    ''' create_song - builds song and returns the song file path '''

    # Create Midi and Sf2 objects
    SongMid = Song()
    SongSf2 = sf2.SoundFont()

    # Create midi file of the song
    SongMid.gen_chord_prog()
    SongMid.gen_drum_loop()
    song_midi_path = SongMid.save_midi_file()

    # Print debug information
    if debug:
        info.print_info(SongMid, SongSf2)

    # Generate an output path
    song_output_path = AUDIO_FOLDER + SongMid.title + '.' + AUDIO_FILE_TYPE

    # Convert midi file to audio
    SongSf2.midi_to_audio(song_midi_path, song_output_path)

    SongMid.export_song()

    return song_output_path