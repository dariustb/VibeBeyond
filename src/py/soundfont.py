''' soundfont.py - SoundFont file handling '''

import os
import random
import sf2_loader

SF2_FOLDER = 'src/static/sf2/'
AUDIO_FILE_TYPE = 'wav' # See note on midi_to_audio() before changing

class SoundFont:
    ''' SoundFont - Class for handling SoundFont files '''
    def __init__(self):

        # Sf2 file name (NOTE: using default patches)
        self.keys_name  = self.set_keys_name()
        self.lead_name  = self.set_lead_name()
        self.bass_name  = self.set_bass_name()
        self.drum_name  = ''

    # SETTER FUNCTIONS
    def set_keys_name(self) -> str:
        ''' Returns a random piano or pad soundfont name '''
        if not get_sf2_names():
            raise ValueError(
                "No soundfonts found in src/static/sf2/. View readme in folder to download soundfonts." # pylint: disable = line-too-long
            )

        return random.choice(get_sf2_names())

    def set_lead_name(self) -> str:
        ''' Returns a random piano/synth/guitar/chromatic perc soundfont name'''
        return ''

    def set_bass_name(self) -> str:
        ''' Returns a random bass soundfont name'''
        return ''

    # CONVERTER FUNCTIONS
    def midi_to_audio(self, midi_path: str, output_path: str,
                  sf2_path: str = None, sf2_preset: str = None,) -> bool:
        ''' midi_to_audio - Convert a *single* MIDI track file to an audio file

        NOTE: sf2-loader/pydub requires ffmpeg or libav installed
        to deal with non-wav files (https://pypi.org/project/sf2-loader/#Windows)
        '''
        # Load the soundfont file & preset
        if not sf2_path:
            sf2_path = SF2_FOLDER + self.keys_name

        loader = sf2_loader.sf2_loader(sf2_path)
        if not loader.get_current_instrument():
            print('ERROR: Soundfont instrument not found')
            return False

        if not sf2_preset:
            sf2_preset = loader.get_current_instrument()

        # Set the soundfont instrument
        # https://pypi.org/project/sf2-loader/#Change-current-channel-soundfont-id-bank-number-and-preset-number
        loader < sf2_preset # pylint: disable = pointless-statement

        # render a MIDI file with current soundfont files and export as a wav file
        loader.export_midi_file(midi_path, name=output_path, format=AUDIO_FILE_TYPE)

        return True

def get_sf2_names() -> tuple:
    ''' get_sf2_list - Get a list of all soundfont files in the sf2 folder '''
    return tuple(sf2 for sf2 in os.listdir(SF2_FOLDER) if sf2.lower().endswith('.sf2'))
