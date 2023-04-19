''' test_audio_manip.py - Unit tests for audio_manip.py '''

import os
from src.py import audio_manip # pylint: disable = import-error

TEST_FILE_PATH = 'tests/_files/'
TEST_DRUMS = TEST_FILE_PATH + 'test_drums.wav'
TEST_CHORDS = TEST_FILE_PATH + 'test_chord_prog.wav'

def test_combine_audios():
    ''' test_combine_audios - Tests the combine_audios function '''
    test_output = TEST_FILE_PATH + 'test_result_combine_audio.wav'
    try:
        assert audio_manip.combine_audios(
            audio_paths=(
                TEST_CHORDS,
                TEST_DRUMS,
            ),
            output_path = test_output
        )
    finally:
        if os.path.exists(test_output):
            os.remove(test_output)

def test_loop_audio():
    ''' test_loop_audio - Tests the loop_audio function '''
    test_output = TEST_FILE_PATH + 'test_result_loop_audio.wav'
    try:
        assert audio_manip.loop_audio(
            audio_path  = TEST_DRUMS,
            output_path = test_output,
            loop_count  = 4
        )
    finally:
        if os.path.exists(test_output):
            os.remove(test_output)
