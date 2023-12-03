""" test_gen_segment - Unit tests for test_gen_segment """

from pydub import AudioSegment

from src.core.generation import gen_segment


def test_SongSegmentGen_gen_segment():
    # Given
    test_SSG = gen_segment.SongSegmentGen()
    test_track_structure = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    test_audio_path = "tests/test_files/audio/test_chords.wav"
    test_volume = 0

    # When
    test_segment = test_SSG.gen_segment(
        test_track_structure, test_audio_path, test_volume
    )

    # Then
    assert isinstance(test_segment, AudioSegment)
    assert len(test_segment) > 0


def test_SongSegmentGen_gen_segment_with_invalid_audio_path():
    # Given
    test_SSG = gen_segment.SongSegmentGen()
    test_track_structure = (1, 1, 1, 1)
    test_bad_audio_path = "this/path/does/not/exist"
    test_volume = 0

    # When
    test_segment = test_SSG.gen_segment(
        test_track_structure, test_bad_audio_path, test_volume
    )

    # Then
    assert test_segment is None
