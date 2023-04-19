''' test_info.py - Unit tests for info.py '''

import pytest
from src.py import info # pylint: disable = import-error
from src.py import song # pylint: disable = import-error
from src.py import soundfont as sf2 # pylint: disable = import-error

@pytest.mark.skip(reason="still accesses src/static/sf2/")
def test_print_info():
    ''' test_print_info - Tests the print_info function '''
    test_song = song.Song()
    test_sf2 = sf2.SoundFont()

    # Check that no variables have changes from the default
    test_values = (
        test_song.title,
        test_song.artist,
        test_song.key,
        test_song.bpm,
        test_song.time_sig,
        test_song.prog,
        test_sf2.keys_name,
        test_sf2.lead_name,
        test_sf2.bass_name,
        test_sf2.drum_name
    )

    info.print_info(test_song, test_sf2)

    assert test_values == (
        test_song.title,
        test_song.artist,
        test_song.key,
        test_song.bpm,
        test_song.time_sig,
        test_song.prog,
        test_sf2.keys_name,
        test_sf2.lead_name,
        test_sf2.bass_name,
        test_sf2.drum_name
    )

@pytest.mark.skip(reason="still accesses src/static/sf2/")
def test_print_chords():
    ''' test_print_chords - Tests the print_chords function '''
    test_song = song.Song()

    # Check that no variables have changes from the default
    test_values = test_song.mid_prog_track

    info.print_chords(test_song)

    assert test_values == test_song.mid_prog_track
