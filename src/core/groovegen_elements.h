#ifndef INCLUDED_GROOVEGEN_ELEMENTS
#define INCLUDED_GROOVEGEN_ELEMENTS

#include <string>
#include <array>

const int PROG_SIZE = 4;

typedef std::array<std::string, PROG_SIZE> ProgType;

namespace
{
    const int MIN_BPM = 75;
    const int MAX_BPM = 100;
    
    const std::array<std::string, 12> VALID_KEYS = {"A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"};
    const std::array<ProgType, 18>    VALID_CHORD_PROGRESSIONS = {{
        {"ii", "V", "I", "IV"},
        {"ii7", "V", "I7", "I7"},
        {"ii", "V7", "iii", "vi"},
        {"iii", "vi", "IV", "I"},
        {"IV", "I", "ii", "vi"},
        {"IV", "I", "iii", "IV"},
        {"IV", "I", "V", "vi"},
        {"IV", "IV", "I", "V"},
        {"IV", "vi", "I", "V"},
        {"IV", "vi", "iii", "I"},
        {"V", "I", "vi", "V"},
        {"V", "IV", "vi", "I"},
        {"V", "vi", "IV", "I"},
        {"vi", "bVI", "bVII", "I"},
        {"vi", "ii", "V", "I"},
        {"vi", "IV", "I", "V"},
        {"vi", "V", "IV", "V"},
        {"vi", "vii", "V", "vi"}
    }};
}

class Elements {
    public:
        // Constructors
        Elements();
        Elements(const int bpm, const std::string key, const ProgType prog);

        // Getters
        int         const bpm()  { return d_bpm; }
        std::string const key()  { return d_key; }
        ProgType    const prog() { return d_prog; }

    private:
        // Data Members
        int         d_bpm;
        std::string d_key;
        ProgType    d_prog;

        // RNG Gens
        int         gen_bpm();
        std::string gen_key();
        ProgType    gen_prog();

};

#endif
