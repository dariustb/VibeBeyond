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
    SongObj = song.Song()

    # Print debug information
    if debug:
        dbg.print_info(SongObj)

    # Create MIDI loops for all sf2 elements
    SongObj.gen_chord_prog()
    SongObj.save_midi_file(SongObj.mid_prog_track, SongObj.keys_midi)

    # Create audio loops for each song element
    SongObj.midi_to_audio()
    SongObj.gen_drum_loop()
    SongObj.drum_segment.export(
        SongObj.drum_path, format=AUDIO_TYPE
    )

    # Create song-length track segments based on the structure
    SongObj.prog_segment = util.build_structured_segment(
        SongObj.song_structure[3],
        SongObj.keys_path,
        KEYS_VOLUME
    )
    SongObj.drum_segment = util.build_structured_segment(
        SongObj.song_structure[5],
        SongObj.drum_path,
        NO_VOLUME_CHANGE
    )

    # Combine track segments
    song_segment = SongObj.drum_segment
    song_segment = song_segment.overlay(SongObj.prog_segment, 0)

    # Export final song
    song_segment.export(SongObj.song_path, format=AUDIO_TYPE)

    # Clean up loop files
    SongObj.delete_loops()

    return SongObj.song_path
