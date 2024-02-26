#include <gtest/gtest.h>
#include <groovegen_midi.h>

using namespace std;

TEST(GrooveGenMidi, DefaultConstructorHasValidVariableValues) {
    // Given
    MidiGen Test;

    // When
    // Then
}

TEST(GrooveGenMidi, BuildChordsReturnsValidMidiTrackOfChordProgression) {
    // Given
    Elements T_Elements;
    MidiGen T_Midi;

    // When
    const bool t_chords = T_Midi.buildChords(T_Elements);

    // Then
    EXPECT_TRUE(t_chords);
}
