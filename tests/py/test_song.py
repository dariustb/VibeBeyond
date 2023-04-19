''' test_song.py - Test Song Class functions '''

import os
import mido
from src.py import song # pylint: disable = import-error

# __init__ ATTRIBUTES TESTS
def test_init_title():
    ''' test_init_title - Test Song.title '''
    test_title = song.Song().title

    # Check that the title is a string
    assert isinstance(test_title, str)

    # Check that the title is not empty
    assert test_title != ''

def test_init_artist():
    ''' test_init_artist - Test Song.artist '''
    test_artist = song.Song().artist

    # Check that the artist is a string
    assert isinstance(test_artist, str)

    # Check that the artist is not empty
    assert test_artist != ''

def test_init_key():
    ''' test_init_key - Test Song.key '''
    test_key = song.Song().key

    # Check that the key is a string
    assert isinstance(test_key, str)

    # Check that the key is not empty
    assert test_key != ''

    # Check that the key is a valid key
    assert test_key in song.VALID_KEYS

def test_init_bpm():
    ''' test_init_bpm - Test Song.bpm '''
    test_bpm = song.Song().bpm

    # Check that the bpm is an integer
    assert isinstance(test_bpm, int)

    # Check that the bpm is within the range
    assert song.MIN_BPM <= test_bpm <= song.MAX_BPM

def test_init_time_signature():
    ''' test_init_time_signature - Test Song.time_signature '''
    test_time_signature = song.Song().time_sig

    # Check that the time signature is a string
    assert isinstance(test_time_signature, tuple)

    # Check that the time signature is a valid time signature
    assert test_time_signature in song.TIME_SIGNATURES

def test_init_chord_prog():
    ''' test_init_chord_prog - Test Song.chord_prog '''
    test_chord_prog = song.Song().prog

    # Check that the chord prog is a string
    assert isinstance(test_chord_prog, tuple)

    # Check that the chord prog is a valid chord prog
    assert test_chord_prog in song.CHORD_PROGRESSIONS

def test_init_midi_file():
    ''' test_init_midi_file - Test Song.midi_file '''
    test_midi_file = song.Song().mid

    # Check that the midi_file is a mido.MidiFile object
    assert isinstance(test_midi_file, mido.MidiFile)

# METHODS TESTS - SETTERS
def test_set_title():
    ''' test_set_title - Test Song.set_title() '''
    test_title = song.Song().set_title()

    # Check that the title is a string
    assert isinstance(test_title, str)

    # Check that the title is not empty
    assert test_title != ''

def test_set_artist():
    ''' test_set_artist - Test Song.set_artist() '''
    test_artist = song.Song().set_artist()

    # Check that the artist is a string
    assert isinstance(test_artist, str)

    # Check that the artist is not empty
    assert test_artist != ''

def test_set_key():
    ''' test_set_key - Test Song.set_key() '''
    test_key = song.Song().set_key()

    # Check that the key is a string
    assert isinstance(test_key, str)

    # Check that the key is not empty
    assert test_key != ''

    # Check that the key is a valid key
    assert test_key in song.VALID_KEYS

def test_set_bpm():
    ''' test_set_bpm - Test Song.set_bpm() '''
    test_bpm = song.Song().set_bpm()

    # Check that the bpm is an integer
    assert isinstance(test_bpm, int)

    # Check that the bpm is within the range
    assert song.MIN_BPM <= test_bpm <= song.MAX_BPM

def test_set_time_signature():
    ''' test_set_time_signature - Test Song.set_time_signature() '''
    test_time_signature = song.Song().set_time_sig()

    # Check that the time signature is a string
    assert isinstance(test_time_signature, tuple)

    # Check that the time signature is a valid time signature
    assert test_time_signature in song.TIME_SIGNATURES

def test_set_chord_prog():
    ''' test_set_chords_prog - Test Song.set_chords_prog() '''
    test_chord_prog = song.Song().set_chord_prog()

    # Check that the chords progression is a list
    assert isinstance(test_chord_prog, tuple)

    # Check that the chords progression is not empty
    assert test_chord_prog != ()

    # Check that the chords progression is valid
    assert test_chord_prog in song.CHORD_PROGRESSIONS

def test_set_track_prefix():
    ''' test_set_track_prefix - Test Song.set_track_prefix() '''
    test_track_prefix = song.Song().set_track_prefix()

    # Check that the track prefix is a string
    assert isinstance(test_track_prefix, mido.MidiTrack)

# METHODS TESTS - GENERATION FUNCTIONS
def test_get_chord_intervals_list():
    ''' test_get_chord_intervals_list - Test Song.get_chord_intervals_list() '''
    test_chord_intervals_list = song.Song().get_chord_intervals_list()

    # Check that the chord intervals list is a list
    assert isinstance(test_chord_intervals_list, list)

    # Check that the chord intervals list is not empty
    assert test_chord_intervals_list

    # Check that the chord intervals list contains valid chord intervals tuples
    for chord_intervals in test_chord_intervals_list:
        assert isinstance(chord_intervals , tuple)

def test_get_root_note_list():
    ''' test_get_root_note_list - Test Song.get_root_note_list() '''
    test_root_note_list = song.Song().get_root_note_list()

    # Check that the root note list is a list
    assert isinstance(test_root_note_list, list)

    # Check that the root note list is not empty
    assert test_root_note_list

    # Check that the root note list has valid root notes
    for root_note in test_root_note_list:
        assert isinstance(root_note, int)

def test_gen_chord_prog():
    ''' test_gen_chord_prog - Test Song.gen_chord_prog() '''
    assert song.Song().gen_chord_prog()

# METHODS TESTS - MIDI UTILITY FUNCTIONS
def test_save_midi_file():
    ''' test_save_midi_file - Test Song.save_midi_file() '''
    test_song = song.Song()
    test_song.gen_chord_prog()
    test_midi_file_name = test_song.save_midi_file()

    try:
        # Check that the midi file name is a string
        assert isinstance(test_midi_file_name, str)

        # Check that the saved midi file exists
        assert os.path.isfile(test_midi_file_name)

        # Check that the saved midi file is a midi file
        assert test_midi_file_name.endswith('.mid')
    finally:
        # Delete the saved midi file
        if os.path.isfile(test_midi_file_name):
            os.remove(test_midi_file_name)
