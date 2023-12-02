""" gen_create - houses the create_song function """

from .gen_elements import SongElements


# The feast de resistance
def create_song() -> str:
    """create_song - builds song and returns the song file path"""

    # 1. RNG Song Elements
    Elements = SongElements()

    # 2. Generate MIDI Loops

    # 3. Generate Audio Loops

    # 4. Generate Song Segments

    # 5. Combine Segments into Final Audio

    # 6. Clean up

    return "src/assets/vb_example_song.wav"
