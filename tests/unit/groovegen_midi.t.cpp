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
    MidiGen Test;

    // When
    const bool t_chords = Test.build_chords();

    // Then
    EXPECT_TRUE(t_chords);
}
