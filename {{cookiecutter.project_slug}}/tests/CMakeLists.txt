find_package(GTest CONFIG REQUIRED)

file(GLOB TEST_SOURCES CONFIGURE_DEPENDS *.cpp)
add_executable({{ cookiecutter.project_slug }}_test ${TEST_SOURCES})

target_include_directories(
    {{ cookiecutter.project_slug }}_test
    PRIVATE ${CMAKE_SOURCE_DIR}/include
)

target_link_libraries(
    {{ cookiecutter.project_slug }}_test
    PRIVATE
        {{ cookiecutter.project_slug }}
        GTest::gtest_main
)

add_test(
    NAME {{ cookiecutter.project_slug }}_test
    COMMAND {{ cookiecutter.project_slug }}_test
)
