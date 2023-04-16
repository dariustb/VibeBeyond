''' app.py - Python driver for Flask server '''

from flask import Flask, render_template
from py import song
from py import soundfont as sf2

app = Flask(__name__)

@app.route('/')
def index():
    ''' Renders the index page. '''
    return render_template('index.html')

@app.route('/play')
def play():
    ''' Renders the play page. '''
    song_name = 'Some Song?'
    song_artist = 'Some Artist!'
    song_length = '4:20'
    return render_template(
        'play.html',
        song_name = song_name,
        song_artist = song_artist,
        song_length = song_length
    )

if __name__ == '__main__':
    # app.run(debug=True)

    # Create song
    song = song.Song()

    # Create midi file of the song
    song.gen_chord_prog()
    MIDI_PATH = song.save_midi_file()

    song.print_info()

    # Convert midi file to audio
    sf2.midi_to_audio(
        midi_path   = MIDI_PATH,
        output_path = 'src/gen/audio/output.wav',
        sf2_path    = 'src/static/sf2/rhodes.sf2',
    )
