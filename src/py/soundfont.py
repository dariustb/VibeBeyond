''' soundfont.py - SoundFont file handling '''

import os
import sf2_loader

SF2_FOLDER = 'src/static/sf2/'
AUDIO_FILE_TYPE = 'wav' # See note on midi_to_audio() before changing

def get_sf2_names() -> list:
    ''' get_sf2_list - Get a list of all soundfont files in the sf2 folder '''
    return tuple(sf2 for sf2 in os.listdir(SF2_FOLDER) if sf2.endswith('.sf2'))

def midi_to_audio(midi_path: str, output_path: str,
                  sf2_path: str, sf2_preset: str = None,) -> bool:
    ''' midi_to_audio - Convert a MIDI file to an audio file
    
    NOTE: sf2-loader/pydub requires ffmpeg or libav installed
    to deal with non-wav files (https://pypi.org/project/sf2-loader/#Windows)
    '''
    # Load the soundfont file
    loader = sf2_loader.sf2_loader(sf2_path)
    if not loader.get_current_instrument():
        return False

    if not sf2_preset:
        sf2_preset = loader.get_current_instrument()

    # Set the soundfont instrument
    # https://pypi.org/project/sf2-loader/#Change-current-channel-soundfont-id-bank-number-and-preset-number
    loader < sf2_preset # pylint: disable = pointless-statement

    # render a MIDI file with current soundfont files and export as a wav file
    loader.export_midi_file(midi_path, name=output_path, format=AUDIO_FILE_TYPE)

    return True
