cmake_minimum_required(VERSION {{ cookiecutter.cmake_min_version }})
project({{ cookiecutter.project_slug }})

include(CTest)
enable_testing()

set(CMAKE_CXX_STANDARD {{ cookiecutter.cpp_standard }})
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_subdirectory(src)
add_subdirectory(examples)
add_subdirectory(tests)
