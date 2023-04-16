''' test_sf2_files.py - Test all soundfont files in the sf2 folder '''

import sf2_loader
from src.py import soundfont as sf2 # pylint: disable = import-error

def test_sf2_files():
    ''' test_sf2_files - Test all soundfont files in the sf2 folder '''
    print('=============================== Testing SoundFont Files ===============================')

    success = True

    for instrument in sf2.get_sf2_names():
        print('TESTING',instrument,'............', end=' ')

        loader = sf2_loader.sf2_loader(sf2.SF2_FOLDER + instrument)

        # Check that the soundfonts have presets
        if not loader.get_all_instrument_names():
            print('ERROR: no Soundfont presets listed')
            success = False
            continue

        midi_path = 'src/gen/midi/test_Example_Electric_Piano.mid'
        output_path = 'src/gen/audio/test_'+instrument[:-4]+'.wav'

        # Confirm that a song can be rendered with the soundfont
        loader.export_midi_file(midi_path, name=output_path, format=sf2.AUDIO_FILE_TYPE)

        print('OK')

        assert success
