''' audio_manip.py - Audio file manipulation '''

# pylint: disable = W0401, W0614

from pydub import AudioSegment
from py.constants import *
import py.soundfont as sf2


def combine_audios(audio_paths: tuple, output_path: str):
    ''' combine_audios - Layers multiple audio files toegther into one audio file '''
    audio_layers = []
    mixed_audio = None

    try:
        # Load the audio files
        for i, audio_path in enumerate(audio_paths):
            audio_layers.append(AudioSegment.from_file(audio_path, format=sf2.AUDIO_FILE_TYPE))
            audio_path = audio_path[:len(audio_paths[0])]

            if i:
                # Overlay the layer audio on top of the base audio
                mixed_audio = audio_layers[i-1].overlay(audio_layers[i])

        # Export the mixed audio as a new file
        mixed_audio.export(output_path, format=sf2.AUDIO_FILE_TYPE)
    except FileNotFoundError:
        print('ERROR: Audio file not found')
        return False

    return True

def loop_audio(audio_path: str, output_path: str, loop_count: int):
    ''' loop_audio - Loops an audio file a specified number of times '''
    try:
        audio = AudioSegment.from_file(audio_path, format=sf2.AUDIO_FILE_TYPE)
        looped_audio = audio * loop_count
        looped_audio.export(output_path, format=sf2.AUDIO_FILE_TYPE)
    except FileNotFoundError:
        print('ERROR: Audio file not found')
        return False

    return True

if __name__ == "__main__":
    # Make longer drum loop
    loop_audio(
        audio_path='src/static/audio/90bpm.wav',
        output_path='src/static/audio/90bpm_looped.wav',
        loop_count=4
    )

    # Combine audio files
    combine_audios(
        audio_paths=(
            'src/gen/audio/90bpm_chords_1.wav',
            'src/static/audio/90bpm_looped.wav',
        ),
        output_path='src/gen/audio/90bpm_beat_3.wav'
    )
