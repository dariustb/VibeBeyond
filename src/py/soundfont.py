''' soundfont.py - SoundFont file handling '''

import sf2_loader

AUDIO_FILE_TYPE = 'wav' # See note on midi_to_audio() before changing

def midi_to_audio(midi_path: str, output_path: str,
                  sf2_path: str, sf2_preset: str,) -> bool:
    ''' midi_to_audio - Convert a MIDI file to an audio file
    
    NOTE: sf2-loader/pydub requires ffmpeg or libav installed
    to deal with non-wav files (https://pypi.org/project/sf2-loader/#Windows)
    '''
    # Load the soundfont file
    loader = sf2_loader.sf2_loader(sf2_path)
    if not loader.get_current_instrument():
        return False

    # Set the soundfont instrument
    # https://pypi.org/project/sf2-loader/#Change-current-channel-soundfont-id-bank-number-and-preset-number
    loader < sf2_preset # pylint: disable = pointless-statement

    # render a MIDI file with current soundfont files and export as a wav file
    loader.export_midi_file(midi_path, name=output_path, format=AUDIO_FILE_TYPE)

    return True

if __name__ == '__main__':
    pass
