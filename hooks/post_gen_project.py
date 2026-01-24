import textwrap

msg = textwrap.dedent(
    """
    Project '{{ cookiecutter.project_name }}' generated successfully!

    Next steps (Windows):
      1) Set up vcpkg (one-time):
         - git clone https://github.com/microsoft/vcpkg.git
         - cd vcpkg && .\\bootstrap-vcpkg.bat
         - set "VCPKG_ROOT=C:\\path\\to\\vcpkg"
         - set PATH=%VCPKG_ROOT%;%PATH%

      2) Initialize vcpkg in project:
         - vcpkg new --application

      3) Build and run tests:
         - .\\cnb.bat  (or F5 in VS Code)

    Requirements:
      - CMake {{ cookiecutter.cmake_min_version }}+
      - C++ compiler with C++{{ cookiecutter.cpp_standard }} support
      - vcpkg

    Documentation: See README.md for more details
    """
)
print(msg)
