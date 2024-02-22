add_executable(test_groovegen)
target_link_libraries(test_groovegen
  PUBLIC
    GTest::gtest_main
    groovegen_core
)

target_sources(test_groovegen
    PRIVATE
    groovegen_elements.t.cpp
)

include(GoogleTest)
gtest_discover_tests(test_groovegen)
