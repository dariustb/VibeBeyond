""" gen_create - houses the create_song function """

from .gen_combine import SongCombine
from .gen_elements import SongElements
from .gen_loop import DrumLoopGen, SongLoopGen
from .gen_midi import SongMidiGen
from .gen_segment import SongSegmentGen


# The feast de resistance
def create_song() -> str:
    """create_song - builds song and returns the song file path"""

    # 1. RNG Song Elements
    Elements = SongElements()

    Loop = SongLoopGen()
    chords_preset = Loop.get_sf2_preset_number(Loop.chords_instrument)
    melody_preset = Loop.get_sf2_preset_number(Loop.melody_instrument)

    # 2. Generate MIDI Loops
    Midi = SongMidiGen()

    Midi.chords_midi_track = Midi.gen_chords(
        Elements.key, Elements.time, Elements.bpm, Elements.prog, chords_preset
    )
    Midi.melody_midi_track = Midi.gen_melody(
        Elements.key, Elements.time, Elements.bpm, Elements.prog, melody_preset, 2
    )

    ## 2b. Export Midi Files
    Midi.export_midi_from_tracks(Midi.chords_midi_track, Midi.chords_midi_path)
    Midi.export_midi_from_tracks(Midi.melody_midi_track, Midi.melody_midi_path)

    # 3. Generate Audio Loops
    Loop.export_loop_from_midi(
        Midi.chords_midi_path,
        Midi.chords_midi_track,
        Loop.chords_loop_path,
        Loop.chords_instrument,
    )
    Loop.export_loop_from_midi(
        Midi.melody_midi_path,
        Midi.melody_midi_track,
        Loop.melody_loop_path,
        Loop.melody_instrument,
    )

    ## 3b. Generate Drum loops
    Drums = DrumLoopGen()
    drum_loop_segment = Drums.gen_drum_loop(Elements.prog, Elements.bpm)
    Drums.export_loop_from_segment(drum_loop_segment, Drums.drum_loop_path)

    # 4. Generate Song Segments
    Segments = SongSegmentGen()

    Segments.chords_segment = Segments.gen_segment(
        Segments.song_structure["chords"], Loop.chords_loop_path
    )
    Segments.melody_segment = Segments.gen_segment(
        Segments.song_structure["melody"], Loop.melody_loop_path
    )

    # 5. Combine Segments into Final Audio
    Combine = SongCombine()
    Combine.combine_segments(Segments)
    Combine.export_audio_from_segment()

    # 6. Clean up

    return "src/assets/vb_example_song.wav"
