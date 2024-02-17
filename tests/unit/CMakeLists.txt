add_executable(test_vibebeyond)
target_link_libraries(test_vibebeyond
  PUBLIC
    GTest::gtest_main
    # vibebeyond_core
)

add_subdirectory(core)

include(GoogleTest)
gtest_discover_tests(test_vibebeyond)
