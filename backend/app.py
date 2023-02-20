''' app.py - Python driver for Flask server '''
from flask import Flask, jsonify
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})



# song gen route
@app.route('/song_gen', methods=['GET'])
def send_song():
    ''' Generate song and return the song info for frontend '''
    # The idea at this point is to make & send the song somewhere
    # either in backend, or in a mutually accessible folder
    # and return the *path* to that song to get added to the queue
    song_dict = {
        'name':'Dancing Droplets',
        'artist':'Leavv',
        'length':'3:14',
        'path':'/src/assets/gigi.mp3'
    }
    return jsonify(song_dict)

if __name__ == '__main__':
    app.run()
