# Add the library from all .cpp files in this directory
file(GLOB CORE_SOURCES *.cpp)
add_library({{ cookiecutter.project_slug }} STATIC ${CORE_SOURCES})

# Include directories for the library
target_include_directories({{ cookiecutter.project_slug }} PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/../include
)

# Optional: Create a shared library version as well
add_library({{ cookiecutter.project_slug }}_shared SHARED ${CORE_SOURCES})
target_include_directories({{ cookiecutter.project_slug }}_shared PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/../include
)
