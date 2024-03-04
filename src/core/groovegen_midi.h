#ifndef INCLUDED_GROOVEGEN_MIDI
#define INCLUDED_GROOVEGEN_MIDI

#include <groovegen_elements.h>
#include <string>
#include <array>

typedef std::array<int, 4> ChordIntType;

namespace {
    // Midi Note Lengths
    const int MIDI_BASE_NOTE    = 480; // note length in ticks (480 ticks per beat)
    const int MIDI_QTR_NOTE     = (MIDI_BASE_NOTE) - 1;
    const int MIDI_HALF_NOTE    = (MIDI_BASE_NOTE * 2) - 1;
    const int MIDI_WHOLE_NOTE   = (MIDI_BASE_NOTE * 4) - 1;
    const int MIDI_8th_NOTE     = (MIDI_BASE_NOTE / 2) - 1;
    const int MIDI_16TH_NOTE    = (MIDI_BASE_NOTE / 4) - 1;
    const int MIDI_DOT_QTR_NOTE = (MIDI_BASE_NOTE / 2 * 3) - 1;
    const int MIDI_DOT_8TH_NOTE = (MIDI_BASE_NOTE / 4 * 3) - 1;

    // Midi Chord Intervals
    const ChordIntType CHORD_INTERVALS_7TH = {0, 4, 7, 10}; // dominant 7
    const ChordIntType CHORD_INTERVALS_DIM = {0, 3, 6, 9};  // diminished
    const ChordIntType CHORD_INTERVALS_AUG = {0, 4, 8, 10}; // augmented
    const ChordIntType CHORD_INTERVALS_MIN = {0, 3, 7, 10}; // minor 7
    const ChordIntType CHORD_INTERVALS_MAJ = {0, 4, 7, 11}; // major 7
}

class MidiGen {
    public:
        // Midi Generators
        bool buildChords(const Elements& elements);
    private:
};

#endif