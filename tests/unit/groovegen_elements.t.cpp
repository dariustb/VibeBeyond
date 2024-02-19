#include <gtest/gtest.h>
#include <groovegen_elements.h>

using namespace std;

TEST(GrooveGenElements, DefaultConstructorHasValidVariableValues) {
    // Given
    Elements Test;

    // When
    const int      t_bpm  = Test.bpm();
    const string   t_key  = Test.key();
    const ProgType t_prog = Test.prog();

    // Then
    EXPECT_GE(t_bpm, MIN_BPM);
    EXPECT_LE(t_bpm, MAX_BPM);

    EXPECT_FALSE(t_key.empty());

    EXPECT_EQ(4, t_prog.size());
    EXPECT_FALSE(t_prog[0].empty());
    EXPECT_FALSE(t_prog[1].empty());
    EXPECT_FALSE(t_prog[2].empty());
    EXPECT_FALSE(t_prog[3].empty());
}

TEST(GrooveGenElements, ParamConstructorHasMatchingVariableValues) {
    // Given
    const int      t_bpm  = 90;
    const string   t_key  = "Ab";
    const ProgType t_prog = {"ii7", "V", "I7", "I7"};

    // When
    Elements Test(t_bpm, t_key, t_prog);

    // Then
    EXPECT_EQ(90,   Test.bpm());
    EXPECT_EQ("Ab", Test.key());
    EXPECT_EQ(4,    Test.prog().size());
}
