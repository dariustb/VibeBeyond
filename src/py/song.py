''' song.py - This file will be used to generate a song '''

import random
import re
import mido

# Global Vars
MIN_BPM = 75
MAX_BPM = 120

MIDI_FOLDER = 'src/gen/midi/'
MIDI_FILE_TYPE = '.mid'

VALID_KEYS = (
    'A', 'Bb', 'B', 'C', 'Db', 'D',
    'Eb', 'E', 'F', 'Gb', 'G', 'Ab'
) # NOTE: key list - https://mido.readthedocs.io/en/latest/meta_message_types.html#key-signature-0x59
TIME_SIGNATURES = (
    (4,4),(4,4)
)
CHORD_PROGRESSIONS = (
    ('ii', 'V', 'I', 'IV'),
    ('ii7', 'V', 'I7', 'I7'),
    ('ii', 'V7', 'iii', 'vi'),

    ('iii', 'vi', 'IV', 'I'),

    ('IV', 'I', 'ii', 'vi'),
    ('IV', 'I', 'iii', 'IV'),
    ('IV', 'I', 'V', 'vi'),
    ('IV', 'IV', 'I', 'V'),
    ('IV', 'vi', 'I', 'V'),
    ('IV', 'vi', 'iii', 'I'),

    ('V', 'I', 'vi', 'V'),
    ('V', 'IV', 'vi', 'I'),
    ('V', 'vi', 'IV', 'I'),

    ('vi', 'bVIM', 'bVIIM', 'I'),
    ('vi', 'ii', 'V', 'I'),
    ('vi', 'IV', 'I', 'V'),
    ('vi', 'V', 'IV', 'V', 'ii', 'V', 'I', 'I'),
    ('vi', 'V', 'IV', 'V'),
    ('vi', 'vii', 'V', 'vi', '#IVdim', 'V')
)

class Song:
    ''' This class will be used to generate a song'''
    def __init__(self):
        ''' All the song's static variables will be kept here '''

        # Metadata
        self.title      = self.set_title()
        self.artist     = self.set_artist()

        # Song generation info
        self.key        = self.set_key()
        self.bpm        = self.set_bpm() # tempo = mido.bpm2tempo(bpm) =/= bpm
        self.time_sig   = self.set_time_sig()
        self.prog       = self.set_chord_prog()

        # Midi info
        self.mid_prog_track = self.set_track_prefix()
        self.mid_lead_track = None
        self.mid_bass_track = None
        self.mid_drum_track = None

        # File info
        self.mid        = mido.MidiFile()

    # SETTER FUNCTIONS
    def set_title(self) -> str:
        ''' Returns a randomized string of text in Title Case '''
        return 'example song'.title()

    def set_artist(self) -> str:
        ''' Returns a randomized string of text in Title Case '''
        return 'example Artist'.title()

    def set_key(self) -> str:
        '''
        Returns a random Key (based on mido's valid key signatures)
        https://mido.readthedocs.io/en/latest/meta_message_types.html#key-signature-0x59
        '''
        return random.choice(VALID_KEYS)

    def set_bpm(self) -> int:
        ''' Returns a random BPM within the usable range, inclusive '''
        return random.randint(MIN_BPM, MAX_BPM)

    def set_time_sig(self) -> tuple:
        ''' Returns tuple with numer and denom of the time signature '''
        return random.choice(TIME_SIGNATURES)

    def set_chord_prog(self) -> tuple:
        ''' Returns a tuple with the chord identities, not connected to the key '''
        return random.choice(CHORD_PROGRESSIONS)

    def set_track_prefix(self) -> mido.MidiTrack:
        ''' Add necessary info to the beginnning of midi track '''
        # Create track
        track = mido.MidiTrack()

        # Add MetaMessages to file
        track.append(mido.MetaMessage('track_name', name='song_track', time=0))
        track.append(mido.MetaMessage('time_signature',
                                      numerator = self.time_sig[0], denominator = self.time_sig[1],
                                      clocks_per_click = 24, notated_32nd_notes_per_beat = 8,
                                      time = 0
                                      ))
        track.append(mido.MetaMessage('key_signature', key=self.key, time=0))
        track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(self.bpm), time=0))

        # Not sure why yet, but MuseScore does this, and it allows the sound to play
        track.append(mido.Message('control_change', channel=0, control=121, value=0, time=0))
        track.append(mido.Message('program_change', channel=0, program=4, time=0))
        track.append(mido.Message('control_change', channel=0, control=7, value=100, time=0))
        track.append(mido.Message('control_change', channel=0, control=10, value=64, time=0))
        track.append(mido.Message('control_change', channel=0, control=91, value=0, time=0))
        track.append(mido.Message('control_change', channel=0, control=93, value=0, time=0))
        track.append(mido.MetaMessage('midi_port', port=0, time=0))

        return track

    # GENERATION FUNCTIONS
    def get_chord_intervals_list(self):
        ''' Returns a list of chord intervals in the progression '''
        chord_intervals_list = []

        for chord in self.prog:
            # Evaluate chord type as intervals
            chord_no_acc = chord.replace('b','').replace('#','')
            if '7' in chord:
                chord_intervals = (0, 4, 7, 10)  # dominant 7th
            elif 'dim' in chord:
                chord_intervals = (0, 3, 6, 9)   # diminished
            elif 'aug' in chord:
                chord_intervals = (0, 4, 8, 10)  # augmented
            elif chord.lower() == chord:
                chord_intervals = (0, 3, 7, 10)  # minor 7
            elif chord_no_acc.upper() == chord_no_acc:
                chord_intervals = (0, 4, 7, 11)  # major 7
            else:
                raise ValueError('Invalid chord type')

            chord_intervals_list.append(chord_intervals)

        return chord_intervals_list

    def get_root_note_list(self):
        ''' Returns a list of root notes in the progression '''
        root_note_list = []

        for chord in self.prog:
            # Evaluate key value as root note
            root_note = {
                'Gb': 54, 'G': 55,
                'Ab': 56, 'A': 57,
                'Bb': 58, 'B': 59,
                'C': 60,
                'Db': 61, 'D': 62,
                'Eb': 63, 'E': 64,
                'F': 65
            }[self.key]

            # Evaluate scale degree + add interval to root note
            chord_degree = re.sub(r'b|#|7|dim|aug|m|M', '', chord).lower()
            root_note += {
                'i':   0, 'ii': 2,
                'iii': 4, 
                'iv': -7, 'v':  -5,
                'vi': -3, 'vii':-1
            }[chord_degree]

            # Evaluate scale degree modification (flat, sharp, etc.)
            if 'b' in chord:
                root_note -= 1   # flat/lowered half-step
            elif '#' in chord:
                root_note += 1   # sharp/raised half-step

            # Add values to outside lists
            root_note_list.append(root_note)

        return root_note_list

    def gen_chord_prog(self):
        ''' Adds a chord progression to the class variable '''

        # Might need to move this later - note length in ticks (480 ticks per beat)
        qtr_note = 480
        whole_note = qtr_note * 4

        # Get chord progression variables
        chord_intervals_list    = self.get_chord_intervals_list()
        root_note_list          = self.get_root_note_list()

        # Repeat chord progression for length of song
        for _ in range(16):

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
                        velocity=80,
                        time = note_start_time
                    ))

                # Add note_off: sets the release time for note (time=0 is instant)
                for i, note_interval in enumerate(chord_intervals):
                    note_stop_time = whole_note if i == 0 else 0
                    self.mid_prog_track.append(mido.Message(
                    'note_off',
                    note = root_note + note_interval,
                    velocity = 0,
                    time = note_stop_time
                    ))

        return True

    # MIDI UTILITY FUNCTIONS
    def save_midi_file(self):
        ''' Combines the midi tracks into MidiFile & saves to .mid file '''
        if self.mid_prog_track is not None:
            self.mid.tracks.append(self.mid_prog_track)
        if self.mid_lead_track is not None:
            self.mid.tracks.append(self.mid_lead_track)
        if self.mid_bass_track is not None:
            self.mid.tracks.append(self.mid_bass_track)
        if self.mid_drum_track is not None:
            self.mid.tracks.append(self.mid_drum_track)

        midi_file_name = MIDI_FOLDER + self.title + MIDI_FILE_TYPE
        self.mid.save(midi_file_name)

        return midi_file_name
