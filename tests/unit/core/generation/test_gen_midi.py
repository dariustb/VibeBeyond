""" test_gen_midi - Unit tests for gen_midi """

from mido import MidiTrack, bpm2tempo

from src.core.generation import gen_midi
from src.core.generation.gen_midi import SongMidiGen


def test_get_chord_intervals_list_with_major_and_minor_chords():
    # Given
    test_prog = ("ii", "V", "I", "IV")

    # When
    test_intervals = gen_midi.get_chord_intervals_list(test_prog)

    # Then
    assert isinstance(test_intervals, list)
    assert test_intervals == [
        (0, 3, 7, 10),  # Minor (ii)
        (0, 4, 7, 11),  # Major (V)
        (0, 4, 7, 11),  # Major (I)
        (0, 4, 7, 11),  # Major (IV)
    ]


def test_get_chord_intervals_list_with_dominant_and_minor7_chords():
    # Given
    test_prog = ("ii7", "V", "I7", "I7")

    # When
    test_intervals = gen_midi.get_chord_intervals_list(test_prog)

    # Then
    assert isinstance(test_intervals, list)
    assert test_intervals == [
        (0, 3, 7, 10),  # Minor (ii7)
        (0, 4, 7, 11),  # Major (V)
        (0, 4, 7, 10),  # Dominant (I7)
        (0, 4, 7, 10),  # Dominant (I7)
    ]


def test_get_chord_intervals_list_with_accidentals():
    # Given
    test_prog = ("vi", "bVI", "bVII", "I")

    # When
    test_intervals = gen_midi.get_chord_intervals_list(test_prog)

    # Then
    assert isinstance(test_intervals, list)
    assert test_intervals == [
        (0, 3, 7, 10),  # Minor (vi)
        (0, 4, 7, 11),  # Major (bVI)
        (0, 4, 7, 11),  # Major (bVII)
        (0, 4, 7, 11),  # Major (I)
    ]


def test_get_chord_intervals_list_with_diminished_chord():
    # Given
    test_prog = ("#viidim", "i", "VI", "III")

    # When
    test_intervals = gen_midi.get_chord_intervals_list(test_prog)

    # Then
    assert isinstance(test_intervals, list)
    assert test_intervals == [
        (0, 3, 6, 9),  # Diminished (#viidim)
        (0, 3, 7, 10),  # Minor (i)
        (0, 4, 7, 11),  # Major (VI)
        (0, 4, 7, 11),  # Major (III)
    ]


def test_get_chord_intervals_list_with_augmented_chord():
    # Given
    test_prog = ("I", "Iaug", "vi", "Iaug")

    # When
    test_intervals = gen_midi.get_chord_intervals_list(test_prog)

    # Then
    assert isinstance(test_intervals, list)
    assert test_intervals == [
        (0, 4, 7, 11),  # Major (I)
        (0, 4, 8, 10),  # Augmented (Iaug)
        (0, 3, 7, 10),  # Minor (vi)
        (0, 4, 8, 10),  # Augmented (Iaug)
    ]


def test_get_root_note_list():
    # Given
    test_key = "C"  # C = 60
    test_prog = ("ii", "V", "I", "IV")  # D, G, C, F -> 62, 55, 60, 53

    # When
    test_roots = gen_midi.get_root_note_list(test_key, test_prog)

    # Then
    assert isinstance(test_roots, list)
    assert test_roots == [62, 55, 60, 53]


def test_SongMidiGen_set_midi_path():
    # Given
    test_SMG = SongMidiGen()
    test_name = "example"

    # When
    test_midi_path = test_SMG.set_midi_path(test_name)

    # Then
    assert isinstance(test_midi_path, str)
    assert test_midi_path == "src/gen/midi/example_midi.mid"


def test_SongMidiGen_gen_track_prefix():
    # Given
    test_SMG = SongMidiGen()
    test_key = "C"
    test_time = (4, 4)
    test_bpm = 90
    test_preset = 38

    # When
    test_prefix = test_SMG.gen_track_prefix(test_key, test_time, test_bpm, test_preset)

    # Then
    assert isinstance(test_prefix, MidiTrack)
    assert len(test_prefix) >= 11  # the function appends 11 Messages/MetaMessages

    assert test_prefix[0].type == "track_name"
    assert test_prefix.name == "song_track"

    assert test_prefix[1].type == "time_signature"
    assert test_prefix[1].numerator == test_time[0]
    assert test_prefix[1].denominator == test_time[0]
    assert test_prefix[1].clocks_per_click == 24
    assert test_prefix[1].notated_32nd_notes_per_beat == 8

    assert test_prefix[2].type == "key_signature"
    assert test_prefix[2].key == test_key

    assert test_prefix[3].type == "set_tempo"
    assert test_prefix[3].tempo == bpm2tempo(test_bpm)

    assert test_prefix[4].type == "control_change"

    assert test_prefix[5].type == "program_change"
    assert test_prefix[5].program == test_preset

    assert test_prefix[6].type == "control_change"
    assert test_prefix[7].type == "control_change"
    assert test_prefix[8].type == "control_change"
    assert test_prefix[9].type == "control_change"
    assert test_prefix[10].type == "midi_port"


def test_SongMidiGen_gen_chords():
    # Given
    test_SMG = SongMidiGen()
    test_key = "C"
    test_time = (4, 4)
    test_bpm = 90
    test_preset = 38
    test_prog = ("ii", "V7", "I", "IV")
    test_note_list = (
        62,  # D (Dmin)
        65,  # F
        69,  # A
        72,  # C
        55,  # G (G7)
        59,  # B
        62,  # D
        65,  # F
        60,  # C (Cmaj7)
        64,  # E
        67,  # G
        71,  # B
        53,  # F (Fmaj7)
        57,  # A
        60,  # C
        64,  # E
    )

    # When
    test_chords = test_SMG.gen_chords(
        test_key, test_time, test_bpm, test_prog, test_preset
    )

    # Then
    assert isinstance(test_chords, MidiTrack)
    assert len(test_chords) >= 11

    # Check actual notes in the chord progression
    note_index = 0
    for message in test_chords:
        if message.type != "note_on":
            continue
        assert message.note == test_note_list[note_index]
        note_index += 1


def test_SongMidiGen_gen_melody():
    # Given
    test_SMG = SongMidiGen()
    test_key = "C"
    test_time = (4, 4)
    test_bpm = 90
    test_preset = 38
    test_prog = ("ii", "V7", "I", "IV")
    test_complexity = 2

    MIDI_WHOLE_NOTE = 1919
    measure_duration = MIDI_WHOLE_NOTE
    note_duration = 0
    test_roots = [62, 55, 60, 53]
    test_intervals = [
        (0, 3, 7, 10),  # Minor (ii)
        (0, 4, 7, 10),  # Dominant (V7)
        (0, 4, 7, 11),  # Major (I)
        (0, 4, 7, 11),  # Major (IV)
    ]
    chord_root = test_roots.pop(0)
    chord_intervals = test_intervals.pop(0)

    # When
    test_melody = test_SMG.gen_melody(
        test_key, test_time, test_bpm, test_prog, test_preset, test_complexity
    )

    # Then
    assert isinstance(test_melody, MidiTrack)

    for message in test_melody:
        if message.type != "note_off":
            continue

        # Confirm note is in the scale for chord (chord tones for now)
        assert (
            message.note - chord_root in chord_intervals
            or (message.note + 12 - chord_root) in chord_intervals
        )

        # Confirm notes fit in each measure
        note_duration = message.time
        measure_duration -= note_duration
        assert measure_duration >= 0

        # Update check info at the end of measure
        if measure_duration == 0:
            measure_duration = MIDI_WHOLE_NOTE
            chord_intervals = test_intervals.pop(0) if len(test_intervals) > 0 else ()
            chord_root = test_roots.pop(0) if len(test_roots) > 0 else ()


def test_SongMidiGen_export_midi_from_tracks():
    # Given
    test_SMG = SongMidiGen()
    test_track = None
    test_path = "example"

    # When
    test_export = test_SMG.export_midi_from_tracks(test_track, test_path)

    # Then
    assert test_export is None
