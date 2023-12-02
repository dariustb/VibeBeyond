""" test_gen_elements - Unit tests for gen_elements """

from src.core.generation.gen_elements import SongElements


def test_SongElements_set_key():
    """Confirm valid keys returned"""
    # Given
    test_SE = SongElements()

    # When
    test_key = test_SE.set_key()

    # Then
    assert isinstance(test_key, str)
    assert test_key in ("A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab")


def test_SongElements_set_time():
    """Confirm valid time signature returned"""
    # Given
    test_SE = SongElements()

    # When
    test_time = test_SE.set_time()

    # Then
    assert isinstance(test_time, tuple)
    assert test_time[0] > 0 and test_time[1] > 0
    assert test_time[1] % 4 == 0


def test_SongElements_set_bpm():
    """Confirm valid BPM returned"""
    # Given
    test_SE = SongElements()

    # When
    test_bpm = test_SE.set_bpm()

    # Then
    assert isinstance(test_bpm, int)
    assert 75 <= test_bpm <= 100


def test_SongElements_set_prog():
    """Confirm valid chord progression returned"""
    # Given
    test_SE = SongElements()

    # When
    test_prog = test_SE.set_prog()

    # Then
    assert isinstance(test_prog, tuple)
    assert len(test_prog) % 4 == 0
