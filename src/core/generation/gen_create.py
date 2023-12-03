""" gen_create - houses the create_song function """

from .gen_elements import SongElements
from .gen_midi import SongMidiGen


# The feast de resistance
def create_song() -> str:
    """create_song - builds song and returns the song file path"""

    # 1. RNG Song Elements
    Elements = SongElements()

    # 2. Generate MIDI Loops
    Midi = SongMidiGen()

    Midi.chords_midi_track = Midi.gen_chords(
        Elements.key, Elements.time, Elements.bpm, Elements.prog
    )
    Midi.melody_midi_track = Midi.gen_melody(
        Elements.key, Elements.time, Elements.bpm, Elements.prog, 2
    )

    # 3. Generate Audio Loops

    # 4. Generate Song Segments

    # 5. Combine Segments into Final Audio

    # 6. Clean up

    return "src/assets/vb_example_song.wav"
