set(CMAKE_INCLUDE_CURRENT_DIR ON)

add_executable(
    groovegen
    groovegen.m.cpp
)

add_library(groovegen_core)
add_subdirectory(core)

target_link_libraries(groovegen PUBLIC 
    rtmidi
    groovegen_core
)
