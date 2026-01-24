cmake_minimum_required(VERSION {{ cookiecutter.cmake_min_version }})
project({{ cookiecutter.project_slug }}_test)

find_package(GTest CONFIG REQUIRED)

# Add all .cpp files in this directory as test sources
file(GLOB TEST_SOURCES *.cpp)
add_executable({{ cookiecutter.project_slug }}_test ${TEST_SOURCES})

target_include_directories({{ cookiecutter.project_slug }}_test PRIVATE
    ${CMAKE_SOURCE_DIR}/include
)

target_link_libraries({{ cookiecutter.project_slug }}_test PRIVATE
    {{ cookiecutter.project_slug }}
    GTest::gtest
    GTest::gtest_main
)

add_test(NAME {{ cookiecutter.project_slug }}_test COMMAND {{ cookiecutter.project_slug }}_test)
