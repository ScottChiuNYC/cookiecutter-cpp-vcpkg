add_executable(demo demo.cpp)

target_link_libraries(demo PRIVATE {{ cookiecutter.project_slug }})
