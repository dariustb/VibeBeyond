''' test_song.py - Test Song Class functions '''

import mido
from src.py import song # pylint: disable = import-error

# NOTE: Not testing the following functions:
#   - Song.__init__()
#   - Song.print_info()
#   - Song.print_chords()
#   - Song.combine_midi_tracks()
#   - Song.save_midi_file()

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
