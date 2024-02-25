target_include_directories(groovegen_core PUBLIC ./)

target_sources(groovegen_core
    PRIVATE
    groovegen_elements.cpp
    groovegen_midi.cpp
)
