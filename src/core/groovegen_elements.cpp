#include <groovegen_elements.h>
#include <cstdlib>
#include <iostream>

// Constructors
Elements::Elements()
: Elements(gen_bpm(), gen_key(), gen_prog())
{
}

Elements::Elements(const int bpm, const std::string key, const ProgType prog)
: d_bpm(bpm), d_key(key), d_prog(prog)
{
}

// Generators
int Elements::gen_bpm()
{
    return MIN_BPM + (rand() % (MAX_BPM - MIN_BPM)); 
}

std::string Elements::gen_key()
{
    return VALID_KEYS[rand() % VALID_KEYS.size()];
}

ProgType Elements::gen_prog()
{
    return VALID_CHORD_PROGRESSIONS[rand() % VALID_CHORD_PROGRESSIONS.size()];
}
