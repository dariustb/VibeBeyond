add_executable(
    groovegen
    groovegen.m.cpp
)
add_library(groovegen_core)
add_subdirectory(core)

target_link_libraries(groovegen PRIVATE 
    ${ALSA_LIBRARIES}
    rtmidi
    groovegen_core
)
