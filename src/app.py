''' app.py - Python driver for Flask server '''

from flask import Flask, render_template
from py import song
from py import soundfont as sf2
from py import info

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

    # Create Midi and Sf2 objects
    SongMid = song.Song()
    SongSf2 = sf2.SoundFont()

    # Create midi file of the song
    SongMid.gen_chord_prog()
    MIDI_PATH = SongMid.save_midi_file()

    info.print_info(SongMid, SongSf2)

    # Convert midi file to audio
    SongSf2.midi_to_audio(
        midi_path   = MIDI_PATH,
        output_path = 'src/gen/audio/output.wav'
    )
