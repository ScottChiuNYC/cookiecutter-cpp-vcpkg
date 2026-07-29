import textwrap

msg = textwrap.dedent(
    """
    Project '{{ cookiecutter.project_name }}' generated successfully!

    Windows:
      1) Set VCPKG_ROOT to a vcpkg checkout.
      2) Configure: cmake --preset windows-vcpkg
      3) Build: cmake --build --preset windows-release
      4) Run tests: ctest --preset windows-release-tests

    Linux:
      1) Set VCPKG_ROOT to a vcpkg checkout and install Ninja.
      2) Configure: cmake --preset linux-vcpkg-release
      3) Build: cmake --build --preset linux-release
      4) Run tests: ctest --preset linux-release-tests

    Dependencies:
      - gtest is resolved from ScottChiuNYC/vcpkg-registry so it does not acquire pkgconf.
      - all other packages continue to use the Microsoft vcpkg registry by default.

    Requirements:
      - CMake {{ cookiecutter.cmake_min_version }}+
      - Visual Studio 2022 on Windows, or Ninja plus a C++{{ cookiecutter.cpp_standard }} compiler on Linux
      - vcpkg

    Documentation: See README.md for more details.
    """
)
print(msg)
