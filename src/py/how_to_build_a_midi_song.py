''' how_to_build_a_midi_song.py - Instructions for making a working midi file '''

import mido

def read_song(midi_song_name = 'Example_Electric_Piano.mid'):
    ''' Shows song information '''
    song = mido.MidiFile('src/static/midi/' + midi_song_name)
    for i, track in enumerate(song.tracks):
        print('Track', i, ':', track.name)
        for msg in track:
            print(msg)

def build_song(midi_song_name = 'song.mid'):
    ''' Creates a full midi melody (this case being a major scale pattern) '''
    # Set the values for the song
    instrument_name = 'Electric Piano'
    beats_per_minute = 90
    key = 'C'
    key_note = 60 # Middle-C
    ma_scale = [key_note,
             key_note + 2,
             key_note + 4,
             key_note + 5,
             key_note + 7,
             key_note + 9,
             key_note + 11,
             key_note + 12,
             ]

    # Note durations (or "time") relative to the 90bpm
    qtr_note = 479
    eigth_note = 239
    # whole_note = 1919

    # Create a new MIDI file
    mid = mido.MidiFile()

    # Add a track to the MIDI file
    track = mido.MidiTrack()

    # Add MetaMessages to file
    track.append(mido.MetaMessage('track_name', name=instrument_name, time=0))
    track.append(mido.MetaMessage('time_signature', numerator=4, denominator=4, time=0))
    track.append(mido.MetaMessage('key_signature', key=key, time=0))
    track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(beats_per_minute), time=0))

    # Not sure why yet, but MuseScore does this, and it allows the sound to play
    track.append(mido.Message('control_change', channel=0, control=121, value=0, time=0))
    track.append(mido.Message('program_change', channel=0, program=4, time=0))
    track.append(mido.Message('control_change', channel=0, control=7, value=100, time=0))
    track.append(mido.Message('control_change', channel=0, control=10, value=64, time=0))
    track.append(mido.Message('control_change', channel=0, control=91, value=0, time=0))
    track.append(mido.Message('control_change', channel=0, control=93, value=0, time=0))
    track.append(mido.MetaMessage('midi_port', port=0, time=0))

    # Make the C major scale pattern
    # NOTE: 'time' is has to do with the note duration
    # (quarter note, eighth note, etc) relative to the tempo
    # NOTE: 'time' is measured in ticks inside a track

    track.append(mido.Message('note_on', channel=0, note=ma_scale[0], velocity=80, time=1))
    track.append(mido.Message('note_off', channel=0, note=ma_scale[0], velocity=0, time=qtr_note))

    track.append(mido.Message('note_on', channel=0, note=ma_scale[1], velocity=80, time=1))
    track.append(mido.Message('note_off', channel=0, note=ma_scale[1], velocity=0, time=eigth_note))

    track.append(mido.Message('note_on', channel=0, note=ma_scale[2], velocity=80, time=1))
    track.append(mido.Message('note_off', channel=0, note=ma_scale[2], velocity=0, time=eigth_note))

    track.append(mido.Message('note_on', channel=0, note=ma_scale[3], velocity=80, time=1))
    track.append(mido.Message('note_off', channel=0, note=ma_scale[3], velocity=0, time=eigth_note))

    track.append(mido.Message('note_on', channel=0, note=ma_scale[4], velocity=80, time=1))
    track.append(mido.Message('note_off', channel=0, note=ma_scale[4], velocity=0, time=eigth_note))

    track.append(mido.Message('note_on', channel=0, note=ma_scale[5], velocity=80, time=1))
    track.append(mido.Message('note_off', channel=0, note=ma_scale[5], velocity=0, time=eigth_note))

    track.append(mido.Message('note_on', channel=0, note=ma_scale[6], velocity=80, time=1))
    track.append(mido.Message('note_off', channel=0, note=ma_scale[6], velocity=0, time=eigth_note))

    track.append(mido.Message('note_on', channel=0, note=ma_scale[7], velocity=80, time=1))
    track.append(mido.Message('note_off', channel=0, note=ma_scale[7], velocity=0, time=qtr_note))

    # Manually add end_of_track (so the time is 1 instead of 0)
    track.append(mido.MetaMessage('end_of_track', time=1))

    # Save the MIDI file
    mid.tracks.append(track)
    mid.save('src/static/midi/' + midi_song_name)

if __name__ == '__main__':
    MIDI_FILE_NAME = 'my_song.mid'

    build_song(MIDI_FILE_NAME)
    read_song(MIDI_FILE_NAME)
