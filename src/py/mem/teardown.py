''' teardown.py - This file will handle memory cleanup during and after execution '''

# pylint: disable = W0401, W0614

import os

from py.gen.gen_midi import SongMidiGen
from py.gen.gen_loop import SongLoopGen
from py.constants import *

def delete_loops(midi: SongMidiGen, loop: SongLoopGen) -> bool:
    ''' deletes audio/midi files of the song loops '''
    for loop_file in (
        midi.ambient_midi_path,
        midi.melody_midi_path,
        midi.cmelody_midi_path,
        midi.chords_midi_path,
        midi.bass_midi_path,
        loop.ambient_loop_path,
        loop.melody_loop_path,
        loop.cmelody_loop_path,
        loop.chords_loop_path,
        loop.bass_loop_path,
        loop.drum_loop_path,
    ):
        if os.path.isfile(loop_file):
            os.remove(loop_file)
    return True
