''' test_soundfont.py - Test the soundfont module '''

from src.py import soundfont as sf2 # pylint: disable = import-error

def test_set_keys_name():
    ''' test_set_keys_name - Test Song.set_keys_name() '''
    try:
        test_keys_name = sf2.SoundFont().set_keys_name()

    except ValueError:
        # In case the test is in Github Actions
        # NOTE: The natural fail is IndexError
        assert True

    except IndexError:
        # This is a valid fail
        assert False

    else:
        # Check that the keys name is a string
        assert isinstance(test_keys_name, str)

        # Check that the keys name is not empty
        assert test_keys_name != ''

def test_set_bass_name():
    ''' test_set_bass_name - Test Song.set_bass_name() '''
    try:
        test_bass_name = sf2.SoundFont().set_bass_name()

    except ValueError:
        # In case the test is in Github Actions
        assert True

    except IndexError:
        # This is a valid fail
        assert False

    else:
        # Check that the keys name is a string
        assert isinstance(test_bass_name, str)

        # Check that the keys name is not empty
        #assert test_bass_name != ''
