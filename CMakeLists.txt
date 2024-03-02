cmake_minimum_required(VERSION 3.22)
project(groovegen
    VERSION 1.0
    LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

include(FetchContent)

# Find ALSA
find_package(ALSA REQUIRED)
include_directories(${ALSA_INCLUDE_DIRS})

# Fetch RtMidi
FetchContent_Declare(
  rtmidi
  GIT_REPOSITORY https://github.com/thestk/rtmidi.git
  GIT_TAG        master
)
FetchContent_MakeAvailable(rtmidi)

# Fetch VST3 SDK
FetchContent_Declare(
  vst3sdk
  GIT_REPOSITORY https://github.com/steinbergmedia/vst3sdk.git
  GIT_TAG        master
)
FetchContent_MakeAvailable(vst3sdk)
include_directories(${vst3sdk_SOURCE_DIR}/pluginterfaces)
include_directories(${vst3sdk_SOURCE_DIR}/public.sdk/source)

# Fetch gtests
# https://google.github.io/googletest/quickstart-cmake.html
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

enable_testing()

add_subdirectory(src)
add_subdirectory(tests)
