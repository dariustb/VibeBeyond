""" test_gen_create - Unit tests for gen_create """


from unittest.mock import patch


def test_create_song():
    """test create_song()"""
    # Given
    test_song_path = "example/song.wav"
    with patch("src.core.generation.gen_create.create_song") as mock_create_song:
        # Mock function
        mock_create_song.return_value = test_song_path

        # When
        test_song = mock_create_song()

        # Then
        assert isinstance(test_song, str)
        assert test_song == "example/song.wav"
        mock_create_song.assert_called_once()
