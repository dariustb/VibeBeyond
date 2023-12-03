""" test_gen_loop_inst - Unit tests for test_gen_loop_inst """

from src.core.generation.gen_loop_inst import SongLoopGen


def test_SongLoopGen_set_name():
    # Given
    test_SLG = SongLoopGen()
    test_folder = "tests/test_files/sf2/"

    # When
    test_name = test_SLG.set_name(test_folder)

    # Then
    assert isinstance(test_name, str)
    assert test_name == "tests/test_files/sf2/dummy_1.sf2"


def test_SongLoopGen_set_path():
    # Given
    test_SLG = SongLoopGen()
    test_name = "chords"

    # When
    test_path = test_SLG.set_path(test_name)

    # Then
    assert isinstance(test_path, str)
    assert test_path == "src/gen/audio/chords_loop.wav"


def test_SongLoopGen_export_loop_from_midi():
    # Given
    test_SLG = SongLoopGen()
    test_midi_path = "example/midi.mid"
    test_midi_track = None
    test_loop_path = "example/loop.wav"
    test_sf2_name = "Example Instrument"

    # When
    test_export = test_SLG.export_loop_from_midi(
        test_midi_path, test_midi_track, test_loop_path, test_sf2_name
    )

    # Then
    assert test_export is None
