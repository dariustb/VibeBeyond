""" test_gen_create - Unit tests for gen_create """

# pylint: disable = E0401

from src.core.generation.gen_create import create_song


def test_create_song():
    """test create_song()"""
    # Given
    # When
    test_song = create_song()

    # Then
    assert isinstance(test_song, str)
