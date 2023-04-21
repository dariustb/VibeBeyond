''' app.py - Python driver for Flask server '''

import os
import shutil
import tempfile
from flask import Flask, render_template, send_file

TEMP_DIR = os.path.join(os.getcwd(), 'src/gen/temp')

app = Flask(__name__)

@app.route('/')
def index():
    ''' Renders the index page. '''
    return render_template('index.html')

@app.route('/play')
def play():
    ''' Renders the play page. '''
    # Render the play page
    song_name = 'Some Song?'
    song_artist = 'Some Artist!'
    song_length = '4:20'

    return render_template(
        'play.html',
        song_name = song_name,
        song_artist = song_artist,
        song_length = song_length
    )

@app.route('/song_gen')
def song_gen():
    ''' Generates a song and returns the audio file path. '''
    audio_path = 'src/gen/playlist/SevereWeather.mp3'

    # Create a temporary directory to store the audio file
    os.makedirs(TEMP_DIR, exist_ok=True)

    # Save the audio file to a temporary file
    with tempfile.NamedTemporaryFile(dir=TEMP_DIR, suffix='.mp3', delete=False) as temp_audio_file:
        shutil.copyfile(audio_path, temp_audio_file.name)

    # Send the audio file to the front end
    response = send_file(temp_audio_file.name, as_attachment=False)

    return response

@app.route('/test')
def test():
    ''' Renders the test page. '''

    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)

    # Delete the temporary directory
    try:
        shutil.rmtree(TEMP_DIR)
    except OSError as e:
        print('Error: %s : %s' % (TEMP_DIR, e.strerror))

    print('Done!')

    # # Create Midi and Sf2 objects
    # SongMid = song.Song()
    # SongSf2 = sf2.SoundFont()

    # # Create midi file of the song
    # SongMid.gen_chord_prog()
    # MIDI_PATH = SongMid.save_midi_file()

    # info.print_info(SongMid, SongSf2)

    # # Convert midi file to audio
    # SongSf2.midi_to_audio(
    #     midi_path   = MIDI_PATH,
    #     output_path = 'src/gen/audio/output.wav'
    # )
