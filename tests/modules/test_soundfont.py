''' test_soundfont.py - Test the soundfont module '''

import os
from src.py import soundfont as sf2 # pylint: disable = import-error

TEST_FILE_PATH = 'tests/_files/'
TEST_MIDI       = TEST_FILE_PATH + 'test_midi.mid'
TEST_SOUNDFONT  = TEST_FILE_PATH + 'test_soundfont.sf2'

# __init__ ATTRIBUTES TESTS
def test_init_keys_name():
    ''' test_init_keys_name - Test SoundFont.keys_name '''
    test_keys_name = sf2.SoundFont().keys_name

    # Check that the keys name is a string
    assert isinstance(test_keys_name, str)

    # Check that the keys name is not empty
    assert test_keys_name != ''

def test_init_lead_name():
    ''' test_init_lead_name - Test SoundFont.lead_name '''
    test_lead_name = sf2.SoundFont().lead_name

    # Check that the lead name is a string
    assert isinstance(test_lead_name, str)

    # Check that the lead name is not empty
    #assert test_lead_name != ''

def test_init_bass_name():
    ''' test_init_bass_name - Test SoundFont.bass_name '''
    test_bass_name = sf2.SoundFont().bass_name

    # Check that the bass name is a string
    assert isinstance(test_bass_name, str)

    # Check that the bass name is not empty
    #assert test_bass_name != ''

def test_init_drum_name():
    ''' test_init_drum_name - Test SoundFont.drum_name '''
    test_drum_name = sf2.SoundFont().drum_name

    # Check that the drum name is a string
    assert isinstance(test_drum_name, str)

    # Check that the drum name is not empty
    #assert test_drum_name != ''

# METHODS TESTS - SETTERS
def test_set_keys_name():
    ''' test_set_keys_name - Test Song.set_keys_name() '''
    try:
        test_keys_name = sf2.SoundFont().set_keys_name()
        # Check that the keys name is a string
        assert isinstance(test_keys_name, str)

        # Check that the keys name is not empty
        assert test_keys_name != ''

    except ValueError:
        # So Github Actions can run the test without soundfonts
        assert True

    except IndexError:
        assert False

def test_set_lead_name():
    ''' test_set_lead_name - Test Song.set_lead_name() '''
    try:
        test_lead_name = sf2.SoundFont().set_lead_name()
        # Check that the keys name is a string
        assert isinstance(test_lead_name, str)

        # Check that the keys name is not empty
        #assert test_lead_name != ''

    except ValueError:
        # So Github Actions can run the test without soundfonts
        assert True

    except IndexError:
        assert False

def test_set_bass_name():
    ''' test_set_bass_name - Test Song.set_bass_name() '''
    try:
        test_bass_name = sf2.SoundFont().set_bass_name()
        # Check that the keys name is a string
        assert isinstance(test_bass_name, str)

        # Check that the keys name is not empty
        #assert test_bass_name != ''

    except ValueError:
        # So Github Actions can run the test without soundfonts
        assert True

    except IndexError:
        assert False

# METHODS TESTS - CONVERTER FUNCTIONS
def test_midi_to_audio():
    ''' test_midi_to_audio - Test Song.midi_to_audio() '''
    test_sf2 = sf2.SoundFont()

    test_output = 'tests/_files/test_result_midi_to_audio.wav'

    try:
        test_sf2.midi_to_audio(
            midi_path = TEST_MIDI,
            output_path = test_output,
            sf2_path=TEST_SOUNDFONT
        )
        assert True

    except ValueError:
        # So Github Actions can run the test without soundfonts
        assert True

    except IndexError:
        assert False

    finally:
        # Delete the test file
        if os.path.exists(test_output):
            os.remove(test_output)

# NON-METHODS TESTS
def test_get_sf2_names():
    ''' test_get_sf2_names - Test Song.get_sf2_names() '''
    try:
        test_sf2_names = sf2.get_sf2_names()

        # Check that the sf2 names is a list
        assert isinstance(test_sf2_names, tuple)

        # Check that the sf2 names is not empty
        assert test_sf2_names

    except ValueError:
        # So Github Actions can run the test without soundfonts
        assert True

    except IndexError:
        assert False
