''' song.py - This file will be used to generate a song '''

# pylint: disable = W0401, W0613, W0614, R0902, R0913, R0914, C0103

import os

from py.midi_gen import SongMidiGen
from py.loop_gen import SongLoopGen
from py.constants import *

def delete_loops(Midi: SongMidiGen, Loop: SongLoopGen) -> bool:
    ''' deletes audio/midi files of the song loops '''
    for loop_file in (
        Midi.ambient_midi_path,
        Midi.melody_midi_path,
        Midi.cmelody_midi_path,
        Midi.chords_midi_path,
        Midi.bass_midi_path,
        Loop.ambient_loop_path,
        Loop.melody_loop_path,
        Loop.cmelody_loop_path,
        Loop.chords_loop_path,
        Loop.bass_loop_path,
        Loop.drum_loop_path,
    ):
        if os.path.isfile(loop_file):
            os.remove(loop_file)
    return True
