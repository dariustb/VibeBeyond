''' song.py - This file will be used to generate a song '''

import random
import mido

# Global Vars
MIN_BPM = 75
MAX_BPM = 120

# https://mido.readthedocs.io/en/latest/meta_message_types.html#key-signature-0x59
VALID_KEYS = (
    'A', 'Bb', 'B', 'C', 'Db', 'D',
    'Eb', 'E', 'F', 'Gb', 'G', 'Ab'
)
VALID_TIME_SIGNATURES = (
    (4,4),(6,8)
)
VALID_CHORD_PROGRESSIONS = (
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

KEYBOARD_PATCHES = (
    # Piano
    'Acoustic Grand Piano',
    'Bright Acoustic Piano',
    'Electric Grand Piano',
    'Honky-tonk Piano',
    'Electric Piano 1',
    'Electric Piano 2',
    'Harpsichord',
    'Clavinet',

    # Pad
    'Pad 1 (new age)',
    'Pad 2 (warm)',
    'Pad 3 (polysynth)',
    'Pad 4 (choir)',
    'Pad 5 (bowed)',
    'Pad 6 (metallic)',
    'Pad 7 (halo)',
    'Pad 8 (sweep)'
)
LEAD_PATCHES = (
    'Harpsichord',
    'Clavinet'
)
BASS_PATCHES = (
    # Bass
    'Acoustic Bass',
    'Electric Bass (finger)',
    'Electric Bass (pick)',
    'Fretless Bass',
    'Slap Bass 1',
    'Slap Bass 2',
    'Synth Bass 1',
    'Synth Bass 2'
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
        self.keys_name  = self.set_keys_name()
        self.lead_name  = self.set_lead_name()
        self.bass_name  = self.set_bass_name()
        self.drum_name  = ''

        # Midi info
        self.mid_prog_track = self.set_track_prefix()
        self.mid_lead_track = None
        self.mid_bass_track = None
        self.mid_drum_track = None

        # File info
        self.file_name  = str(self.title + '.mp3').replace(' ', '_')
        self.mid        = mido.MidiFile()

    ## SETTER FUNCTIONS
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
        return random.choice(VALID_TIME_SIGNATURES)

    def set_chord_prog(self) -> tuple:
        ''' Returns a tuple with the chord identities, not connected to the key '''
        return random.choice(VALID_CHORD_PROGRESSIONS)

    def set_keys_name(self) -> str:
        ''' Returns a random piano or pad midi instrument name '''
        return random.choice(KEYBOARD_PATCHES)

    def set_lead_name(self) -> str:
        ''' Returns a random piano/synth/guitar/chromatic perc midi instrument name'''
        return random.choice(LEAD_PATCHES)

    def set_bass_name(self) -> str:
        ''' Returns a random bass midi instrument name'''
        return random.choice(BASS_PATCHES)

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

    # PRINT FUNCTIONS
    def print_info(self):
        ''' Prints the class variables to console '''
        print()
        print('Title:\t',       self.title)
        print('Artist:\t',      self.artist)

        print()
        print('Key:\t',         self.key)
        print('BPM:\t',         self.bpm)
        print('Time:\t',        self.time_sig)
        print('Chords:\t',      self.prog)

        print()
        print('Keys:\t',        self.keys_name)
        print('Lead:\t',        self.lead_name)
        print('Bass:\t',        self.bass_name)
        print('Drum:\t',        self.drum_name)

        print()
        print('File:\t',        self.file_name)

    def print_chords(self):
        ''' Prints the chord progression to console '''
        print()
        print('Chords:\t',      self.mid_prog_track)

    # GENERATION FUNCTIONS
    def gen_chord_prog(self):
        ''' Adds a chord progression to the class variable '''
        root_note  = None
        chord_intervals = None

        for chord in self.prog:
            # Evaluate chord type
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
                chord_intervals = None

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
            root_note += {
                'i':   0, 'ii': 2,
                'iii': 4, 'iv': 5,
                'v':  -5, 'vi': -3,
                'vii':-1
            }[chord.lower().replace('b','').replace('#','').replace('7','')
              .replace('dim','').replace('aug','').replace('m','')]

            # Evaluate scale degree modification (flat, sharp, etc.)
            if 'b' in chord:
                root_note -= 1   # flat/lowered scale degree
            elif '#' in chord:
                root_note += 1   # sharp/raised scale degree

            # Add notes in chord to midi track
            for i, note_interval in enumerate(chord_intervals):
                time = 1 if i == 0 else 0
                self.mid_prog_track.append(mido.Message(
                    'note_on', note=root_note+note_interval, velocity=80, time=time
                    ))
            for i, note_interval in enumerate(chord_intervals):
                time = 1919 if i == 0 else 0
                self.mid_prog_track.append(mido.Message(
                    'note_off', note=root_note+note_interval, velocity=0, time=time
                    ))

            # Reset root note and chord intervals for next chord
            root_note = None
            chord_intervals = None

        return True

    # MIDI UTILITY FUNCTIONS
    def combine_midi_tracks(self):
        ''' Combines the midi tracks into MidiFile '''
        if self.mid_prog_track is not None:
            self.mid.tracks.append(self.mid_prog_track)
        if self.mid_lead_track is not None:
            self.mid.tracks.append(self.mid_lead_track)
        if self.mid_bass_track is not None:
            self.mid.tracks.append(self.mid_bass_track)
        if self.mid_drum_track is not None:
            self.mid.tracks.append(self.mid_drum_track)

    def save_midi_file(self):
        ''' Saves the midi file to the directory '''
        self.mid.save('src/static/midi/' + self.title + '.mid')

if __name__ == '__main__':
    song = Song()
    song.print_info()

    song.gen_chord_prog()
    song.combine_midi_tracks()

    song.print_chords()

    song.save_midi_file()
