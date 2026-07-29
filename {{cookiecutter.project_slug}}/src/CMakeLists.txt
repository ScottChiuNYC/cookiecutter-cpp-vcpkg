file(GLOB CORE_SOURCES CONFIGURE_DEPENDS *.cpp)

add_library({{ cookiecutter.project_slug }} STATIC ${CORE_SOURCES})
target_include_directories(
    {{ cookiecutter.project_slug }}
    PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../include
)

add_library({{ cookiecutter.project_slug }}_shared SHARED ${CORE_SOURCES})
target_include_directories(
    {{ cookiecutter.project_slug }}_shared
    PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../include
)
