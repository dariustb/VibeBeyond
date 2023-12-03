""" test_gen_create - Unit tests for gen_create """

from unittest.mock import patch

from pydub import AudioSegment

from src.core.generation import gen_combine, gen_segment


def test_SongCombine_combine_segments():
    # Given
    test_SC = gen_combine.SongCombine()
    test_SSG = gen_segment.SongSegmentGen()

    test_chords_loop_path = "tests/test_files/audio/test_chords.wav"
    test_melody_loop_path = "tests/test_files/audio/test_melody.wav"
    test_drum_loop_path = "tests/test_files/audio/test_drums.wav"
    test_song_structure = (1, 1, 1, 1)
    test_loop_audio = AudioSegment.from_file(test_chords_loop_path)

    test_SSG.chords_segment = test_SSG.gen_segment(
        test_song_structure, test_chords_loop_path
    )
    test_SSG.melody_segment = test_SSG.gen_segment(
        test_song_structure, test_melody_loop_path
    )
    test_SSG.drum_segment = test_SSG.gen_segment(
        test_song_structure, test_drum_loop_path
    )

    # When
    test_combined_segments = test_SC.combine_segments(test_SSG)

    # Then
    assert test_combined_segments is not None
    assert isinstance(test_combined_segments, AudioSegment)
    assert len(test_combined_segments) == len(test_loop_audio) * 4


def test_SongCombine_export_audio_from_segment():
    # Given
    test_song_path = "example/song.wav"
    with patch(
        "src.core.generation.gen_combine.SongCombine.export_audio_from_segment"
    ) as mock_export_audio:
        # Mock function
        mock_export_audio.return_value = test_song_path

        # When
        test_song = mock_export_audio()

        # Then
        assert isinstance(test_song, str)
        assert test_song == "example/song.wav"
        mock_export_audio.assert_called_once()
