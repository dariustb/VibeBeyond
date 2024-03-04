target_include_directories(groovegen_core PUBLIC ./)

target_link_libraries(groovegen_core PRIVATE
    rtmidi
)

target_sources(groovegen_core PRIVATE
    groovegen_elements.cpp
    groovegen_midi.cpp
    groovegen_vst.cpp
)
