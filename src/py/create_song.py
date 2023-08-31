''' create_song.py - houses the create_song function to prevent cycling in song.py '''

# pylint: disable = W0401, W0614, C0103, E1128

from py import song
from py.constants import *

from py.elements import SongElements
from py.midi_gen import SongMidiGen
from py.loop_gen import SongLoopGen
from py.seg_gen  import SongSegmentGen
from py.combine  import SongCombine

# The feast de resistance
def create_song():
    ''' create_song - builds song and returns the song file path '''

    # 1. RNG Song Elements
    Elements = SongElements()

    # 2. Generate MIDI Loop Files
    ## 2a. Generate chords using `key` and `prog`
    Midi = SongMidiGen()
    Midi.chords_midi_track  = Midi.gen_chords(Elements.key,
                                              Elements.time,
                                              Elements.bpm,
                                              Elements.prog)

    ## 2b. Use chords to make melodic/harmonic parts
    Midi.ambient_midi_track = Midi.gen_melody(Elements.key, Elements.time,
                                              Elements.bpm, Elements.prog, AMBIENT_COMPLEXITY)
    Midi.melody_midi_track  = Midi.gen_melody(Elements.key, Elements.time,
                                              Elements.bpm, Elements.prog, MELODY_COMPLEXITY)
    Midi.cmelody_midi_track = Midi.gen_melody(Elements.key, Elements.time,
                                              Elements.bpm, Elements.prog, CMELODY_COMPLEXITY)
    Midi.bass_midi_track    = Midi.gen_melody(Elements.key, Elements.time,
                                              Elements.bpm, Elements.prog, BASS_COMPLEXITY)

    ## 2c. Export MIDI files
    Midi.export_midi_from_tracks(Midi.ambient_midi_track, Midi.ambient_midi_path)
    Midi.export_midi_from_tracks(Midi.melody_midi_track,  Midi.melody_midi_path)
    Midi.export_midi_from_tracks(Midi.cmelody_midi_track, Midi.cmelody_midi_path)
    Midi.export_midi_from_tracks(Midi.chords_midi_track,  Midi.chords_midi_path)
    Midi.export_midi_from_tracks(Midi.bass_midi_track,    Midi.bass_midi_path)

    # 3. Generate Audio Loop Files
    ## 3a. RNG Sf2 Instruments & Drum Kit Samples
    Loop = SongLoopGen()

    ## 3b. Produce Audio Loops from Sf2 Name and MIDI Loop
    Loop.export_loop_from_midi(Midi.ambient_midi_path, Midi.ambient_midi_track,
                               Loop.ambient_loop_path, Loop.ambient_name)
    Loop.export_loop_from_midi(Midi.melody_midi_path,  Midi.melody_midi_track,
                               Loop.melody_loop_path,  Loop.melody_name)
    Loop.export_loop_from_midi(Midi.cmelody_midi_path, Midi.cmelody_midi_track,
                               Loop.cmelody_loop_path, Loop.cmelody_name)
    Loop.export_loop_from_midi(Midi.chords_midi_path,  Midi.chords_midi_track,
                               Loop.chords_loop_path,  Loop.chords_name)
    Loop.export_loop_from_midi(Midi.bass_midi_path,    Midi.bass_midi_track,
                               Loop.bass_loop_path,    Loop.bass_name)

    ## 3c. Produce Drum Loop from Samples and BPM
    drum_loop_segment = Loop.gen_drum_loop(Elements.prog, Elements.bpm)
    Loop.export_loop_from_segment(drum_loop_segment, Loop.drum_loop_path)

    # 4. Generate Song Segments
    ## 4a. RNG Song Structure
    Segments = SongSegmentGen()

    ## 4b. Produce Segments from Loop and Song Structure
    Segments.ambient_segment = Segments.gen_segment(Segments.song_structure[0],
                                                    Loop.ambient_loop_path)
    Segments.melody_segment  = Segments.gen_segment(Segments.song_structure[1],
                                                    Loop.melody_loop_path)
    Segments.cmelody_segment = Segments.gen_segment(Segments.song_structure[2],
                                                    Loop.cmelody_loop_path)
    Segments.chords_segment  = Segments.gen_segment(Segments.song_structure[3],
                                                    Loop.chords_loop_path)
    Segments.bass_segment    = Segments.gen_segment(Segments.song_structure[4],
                                                    Loop.bass_loop_path)
    Segments.drum_segment    = Segments.gen_segment(Segments.song_structure[5],
                                                    Loop.drum_loop_path)

    # 5. Combine segments into final song audio
    Combine = SongCombine()
    Combine.combine_segments(Segments)
    Combine.export_audio_from_segment()

    # Clean up loops files
    song.delete_loops(Midi, Loop)

    return Combine.song_path
