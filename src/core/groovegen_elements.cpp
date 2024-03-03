#include <groovegen_elements.h>
#include <cstdlib>

// Constructors
Elements::Elements()
: Elements(genBPM(), genKey(), genProg())
{
}

Elements::Elements(const int bpm, const std::string key, const ProgType prog)
: d_bpm(bpm), d_key(key), d_prog(prog)
{
}

// Generators
int Elements::genBPM()
{
    return MIN_BPM + (rand() % (MAX_BPM - MIN_BPM)); 
}

std::string Elements::genKey()
{
    return VALID_KEYS[rand() % VALID_KEYS.size()];
}

ProgType Elements::genProg()
{
    return VALID_CHORD_PROGRESSIONS[rand() % VALID_CHORD_PROGRESSIONS.size()];
}
