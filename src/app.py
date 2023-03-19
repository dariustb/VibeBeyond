''' app.py - Python driver for Flask server '''

from flask import Flask, render_template

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
    app.run(debug=True)
