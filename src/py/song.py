''' song_gen.py - Everything to do with song and song meta info generation '''

# ------------------------------------------------
#           Pylint Messages
# ------------------------------------------------
# pylint: disable = no-member

# ------------------------------------------------
#           Import Libraries
# ------------------------------------------------
import random   # choice, choices
import string   # ascii_letters
import json     # load

import queue    # QUEUE_FOLDER_PATH

# ------------------------------------------------
#           Global Variables
# ------------------------------------------------
class SongClass:
    ''' Class related to a single song, its audio, and meta '''
    def __init__(self, file_ext:str = '.mp3'):
        self.name   :str = self.set_name()
        self.artist :str = self.set_artist()
        self.len    :str = '03:42' #get_song_len()
        self.path   :str = queue.QUEUE_FOLDER_PATH + self.name.replace(' ','_') + file_ext

    def set_name(self) -> str:
        ''' Returns a string with a mocked song name '''
        with open('backend/json/words.json', encoding="utf8") as words_file:
            words = json.loads(words_file.read())
            adj = random.choice(words['adjs'])
            noun = random.choice(words['nouns'])
        return f'{adj} {noun}'.title()

    def set_artist(self) -> str:
        ''' Returns a string with a mocked artist name '''
        return ''.join(random.choices(string.ascii_letters, k=10)).title()

# ------------------------------------------------
#           Function Implementation
# ------------------------------------------------
def generate_song():
    ''' Makes the song, sends to queue folder, returns true when done ''' 

# ------------------------------------------------
#           Testing Driver
# ------------------------------------------------
if __name__ == '__main__':
    SongObj = SongClass()
    print(SongObj)
