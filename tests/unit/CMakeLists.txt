add_executable(test_groovegenie)
target_link_libraries(test_groovegenie
  PUBLIC
    GTest::gtest_main
    groovegen_core
)

target_sources(test_groovegenie
    PRIVATE
    groovegen_elements.t.cpp
)

include(GoogleTest)
gtest_discover_tests(test_groovegenie)
