""" midi_gen - This file will generate midi files for song creation """

import random
from re import sub

import mido

# Constant variables
MIDI_FOLDER: str = "src/gen/midi/"
MIDI_FILE_TYPE: str = ".mid"

# MIDI note durations
MIDI_BASE_NOTE: int = 480  # note length in ticks (480 ticks per beat)
MIDI_QTR_NOTE: int = MIDI_BASE_NOTE - 1
MIDI_HALF_NOTE: int = ((MIDI_BASE_NOTE) * 2) - 1
MIDI_WHOLE_NOTE: int = ((MIDI_BASE_NOTE) * 4) - 1
MIDI_8TH_NOTE: int = ((MIDI_BASE_NOTE) // 2) - 1
MIDI_16TH_NOTE: int = ((MIDI_BASE_NOTE) // 4) - 1
MIDI_DOT_QTR_NOTE: int = int((MIDI_BASE_NOTE) * 1.5) - 1
MIDI_DOT_8TH_NOTE: int = int((MIDI_BASE_NOTE) * 0.75) - 1


class SongMidiGen:
    """This class will hold the song's midi generation functions"""

    def __init__(self, sf2_preset: int = None) -> None:
        """All the song's midi attributes will be kept here"""

        # Midi tracks
        self.chords_midi_track: mido.MidiTrack = None
        self.melody_midi_track: mido.MidiTrack = None

        # Midi file paths
        self.chords_midi_path: str = self.set_midi_path("chords")
        self.melody_midi_path: str = self.set_midi_path("melody")

    # Setter Functions
    def set_midi_path(self, name: str) -> str:
        """Returns a file path based on parameters"""
        return MIDI_FOLDER + name + "_midi" + MIDI_FILE_TYPE

    # Generation Functions
    def gen_track_prefix(
        self, key: str, time: tuple, bpm: int, sf2_preset: int
    ) -> mido.MidiTrack:
        """Add necessary info to the beginnning of midi track"""

        # Create track
        track = mido.MidiTrack()

        # Add Messages / MetaMessages to file
        # Not sure why yet, but MuseScore does this, and it allows the sound to play
        track.append(mido.MetaMessage("track_name", name="song_track", time=0))
        track.append(
            mido.MetaMessage(
                "time_signature",
                numerator=time[0],
                denominator=time[1],
                clocks_per_click=24,
                notated_32nd_notes_per_beat=8,
                time=0,
            )
        )
        track.append(mido.MetaMessage("key_signature", key=key, time=0))
        track.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(bpm), time=0))
        track.append(
            mido.Message("control_change", channel=0, control=121, value=0, time=0)
        )
        # This program_change sets the preset num on the sf2 instrument
        track.append(
            mido.Message("program_change", channel=0, program=sf2_preset, time=0)
        )
        track.append(
            mido.Message("control_change", channel=0, control=7, value=100, time=0)
        )
        track.append(
            mido.Message("control_change", channel=0, control=10, value=64, time=0)
        )
        track.append(
            mido.Message("control_change", channel=0, control=91, value=0, time=0)
        )
        track.append(
            mido.Message("control_change", channel=0, control=93, value=0, time=0)
        )
        track.append(mido.MetaMessage("midi_port", port=0, time=0))

        return track

    def gen_chords(
        self, key: str, time: tuple, bpm: int, prog: tuple, sf2_preset: int
    ) -> mido.MidiTrack:
        """Returns a MIDI track of the chord progression"""

        # Get chord progression variables
        chord_intervals_list = get_chord_intervals_list(prog)
        root_note_list = get_root_note_list(key, prog)

        chords = self.gen_track_prefix(key, time, bpm, sf2_preset)

        # Get chord intervals
        temp_list = (
            chord_intervals_list.copy()
        )  # copy list so we don't pop from original

        # Add notes in chord to midi track
        for root_note in root_note_list:
            chord_intervals = temp_list.pop(0)

            # Add note_on: sets the attack time for note (time=0 is instant)
            for chord_note_index, note_interval in enumerate(chord_intervals):
                note_start_time = 1 if chord_note_index == 0 else 0
                chords.append(
                    mido.Message(
                        "note_on",
                        note=root_note + note_interval,
                        velocity=100,
                        time=note_start_time,
                    )
                )

            # Add note_off: sets the release time for note (time=0 is instant)
            for chord_note_index, note_interval in enumerate(chord_intervals):
                note_stop_time = MIDI_WHOLE_NOTE if chord_note_index == 0 else 0
                chords.append(
                    mido.Message(
                        "note_off",
                        note=root_note + note_interval,
                        velocity=0,
                        time=note_stop_time,
                    )
                )

        return chords

    def gen_melody(  # pylint: disable = R0913, R0914
        self,
        key: str,
        time: tuple,
        bpm: int,
        prog: tuple,
        sf2_preset: int,
        complexity: int,
    ) -> mido.MidiTrack:
        """Returns a generated melody"""
        if complexity >= 3:
            note_durations: tuple = (
                MIDI_8TH_NOTE,
                MIDI_QTR_NOTE,
                MIDI_DOT_QTR_NOTE,
                MIDI_HALF_NOTE,
                MIDI_WHOLE_NOTE,
            )
        elif complexity == 2:
            note_durations: tuple = MIDI_QTR_NOTE, MIDI_HALF_NOTE, MIDI_WHOLE_NOTE
        elif complexity == 1:
            note_durations: tuple = MIDI_WHOLE_NOTE, MIDI_WHOLE_NOTE
        shortest_subdivision = note_durations[0]

        intervals = get_chord_intervals_list(prog)
        roots = get_root_note_list(key, prog)

        rhythm = []
        melody = []

        # Set up track
        track: mido.MidiTrack = self.gen_track_prefix(key, time, bpm, sf2_preset)

        # Add melody notes to track
        for _ in range(len(prog)):
            root_note = roots.pop(0)
            chord_intervals = intervals.pop(0)
            scale_notes = chord_intervals  # using chord tones for now
            measure_length = (time[0] * ((MIDI_WHOLE_NOTE + 1) / time[1])) - 1
            while measure_length >= shortest_subdivision:
                # Add note durations to make rhythm
                note_duration = random.choice(note_durations)
                if measure_length < note_duration:
                    continue
                rhythm.append(note_duration)
                measure_length -= note_duration

                # Add notes pitch to make melody
                pitch = root_note + random.choice(scale_notes)
                melody.append(pitch)

                # Check for last length in measure to line up with next beat
                if measure_length < shortest_subdivision:
                    note_duration += int(measure_length)

                # Add MIDI value to track
                track.append(mido.Message("note_on", note=pitch, velocity=100, time=1))
                track.append(
                    mido.Message("note_off", note=pitch, velocity=0, time=note_duration)
                )

        return track

    # Export Functions
    def export_midi_from_tracks(
        self, midi_track: mido.MidiTrack, midi_path: str
    ) -> str:
        """Combines the midi tracks into MidiFile & saves to .mid file"""
        if midi_track is None:
            return None

        file = mido.MidiFile()

        file.tracks.append(midi_track)
        file.save(midi_path)

        return midi_path


def get_chord_intervals_list(chord_prog) -> list:
    """Returns a list of chord intervals in the progression"""
    chord_intervals_list = []

    for chord in chord_prog:
        # Evaluate chord type as intervals
        chord_no_acc = chord.replace("b", "").replace("#", "")
        if "7" in chord and chord != chord.lower():
            chord_intervals = (0, 4, 7, 10)  # dominant 7th
        elif "dim" in chord:
            chord_intervals = (0, 3, 6, 9)  # diminished
        elif "aug" in chord:
            chord_intervals = (0, 4, 8, 10)  # augmented
        elif chord.lower() == chord:
            chord_intervals = (0, 3, 7, 10)  # minor 7
        elif chord_no_acc.upper() == chord_no_acc:
            chord_intervals = (0, 4, 7, 11)  # major 7
        else:
            raise ValueError("Invalid chord type")

        chord_intervals_list.append(chord_intervals)

    return chord_intervals_list


def get_root_note_list(key, chord_prog) -> list:
    """Returns a list of root notes in the progression"""
    root_note_list = []

    for chord in chord_prog:
        # Evaluate key value as root note
        root_note = {
            "Gb": 54,
            "G": 55,
            "Ab": 56,
            "A": 57,
            "Bb": 58,
            "B": 59,
            "C": 60,
            "Db": 61,
            "D": 62,
            "Eb": 63,
            "E": 64,
            "F": 65,
        }[key]

        # Evaluate scale degree + add interval to root note
        chord_degree = sub(r"b|#|7|dim|aug|m|M", "", chord).lower()
        root_note += {
            "i": 0,
            "ii": 2,
            "iii": 4,
            "iv": -7,
            "v": -5,
            "vi": -3,
            "vii": -1,
        }[chord_degree]

        # Evaluate scale degree modification (flat, sharp, etc.)
        if "b" in chord:
            root_note -= 1  # flat/lowered half-step
        elif "#" in chord:
            root_note += 1  # sharp/raised half-step

        # Add values to outside lists
        root_note_list.append(root_note)

    return root_note_list
