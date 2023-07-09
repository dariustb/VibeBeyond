''' song_utils.py - Utility functions for song.py '''

# pylint: disable = W0401, W0614

from re import sub
from pydub import AudioSegment
from py.constants import *

def get_chord_intervals_list(chord_prog) -> list:
    ''' Returns a list of chord intervals in the progression '''
    chord_intervals_list = []

    for chord in chord_prog:
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

def get_root_note_list(key, chord_prog) -> list:
    ''' Returns a list of root notes in the progression '''
    root_note_list = []

    for chord in chord_prog:
        # Evaluate key value as root note
        root_note = {
            'Gb': 54, 'G': 55,
            'Ab': 56, 'A': 57,
            'Bb': 58, 'B': 59,
            'C': 60,
            'Db': 61, 'D': 62,
            'Eb': 63, 'E': 64,
            'F': 65
        }[key]

        # Evaluate scale degree + add interval to root note
        chord_degree = sub(r'b|#|7|dim|aug|m|M', '', chord).lower()
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

def coordinate_sample(audio, segment, pattern, bpm_in_ms):
    ''' coordinates sample audio to the rhythmic pattern passed in'''
    for _ in range(SONG_LENGTH):
        for note in pattern:
            note_length_in_ms = ((note + 1)/BASE_NOTE) * bpm_in_ms
            if len(audio) < note_length_in_ms:
                segment.append(audio)
                segment.append(AudioSegment.silent(note_length_in_ms - len(audio)))
            elif len(audio) > note_length_in_ms:
                shortened_audio = audio[:len(audio) - note_length_in_ms]
                segment.append(shortened_audio)

def coordinate_snare(audio, segment, bpm_in_ms):
    ''' coordinates snare to the 2 and 4 of the beat '''
    note_length_in_ms = ((HALF_NOTE + 1)/BASE_NOTE) * bpm_in_ms
    segment.append(AudioSegment.silent(note_length_in_ms/2))
    for _ in range(SONG_LENGTH - 1):
        segment.append(audio)
        segment.append(AudioSegment.silent(note_length_in_ms - len(audio)))
        segment.append(audio)
        segment.append(AudioSegment.silent(note_length_in_ms - len(audio)))
    segment.append(audio)
    segment.append(AudioSegment.silent(note_length_in_ms - len(audio)))
    segment.append(audio)
    segment.append(AudioSegment.silent(note_length_in_ms/2))
