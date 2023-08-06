''' create_song.py - houses the create_song function to prevent cycling in song.py '''

# pylint: disable = W0401, W0614, C0103

from py import song
from py import debug as dbg
from py import song_utils as util
from py.constants import *

# The feast de resistance
def create_song(debug: bool = False):
    ''' create_song - builds song and returns the song file path '''

    # Create Song Elements to build song with
    Elements = song.SongElements()

    # Print debug information
    if debug:
        dbg.print_debug_song_info(Elements)

    # Create MIDI loops for all sf2 elements
    Elements.gen_chord_prog()
    Elements.save_midi_file(Elements.mid_prog_track, Elements.keys_midi)

    # Create audio loops for each song element
    Elements.midi_to_audio()
    Elements.gen_drum_loop()
    Elements.drum_segment.export(
        Elements.drum_path, format=AUDIO_TYPE
    )

    # Create song-length track segments based on the structure
    Elements.prog_segment = util.gen_track_segment(
        Elements.song_structure[3],
        Elements.keys_path,
        KEYS_VOLUME
    )
    Elements.drum_segment = util.gen_track_segment(
        Elements.song_structure[5],
        Elements.drum_path,
        NO_VOLUME_CHANGE
    )

    # Combine track segments
    song_segment = Elements.drum_segment
    song_segment = song_segment.overlay(Elements.prog_segment, 0)

    # Export final song
    song_segment.export(Elements.song_path, format=AUDIO_TYPE)

    # Clean up loop files
    Elements.delete_loops()

    return Elements.song_path
