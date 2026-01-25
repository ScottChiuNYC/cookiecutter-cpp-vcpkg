# {{ cookiecutter.project_name }}

CMake + vcpkg + GTest

## One-time setup for vcpkg

1. Clone vcpkg:
   ```
   git clone https://github.com/microsoft/vcpkg.git
   cd vcpkg && .\bootstrap-vcpkg.bat
   ```

2. Set environment variables:
   ```
   set "VCPKG_ROOT=C:\path\to\vcpkg"
   set PATH=%VCPKG_ROOT%;%PATH%
   ```

3. In project root, initialize vcpkg:
   ```
   vcpkg new --application
   ```

## Developer Guide

### Building and Testing

- Run `cnb.bat` to configure, build, and run tests
- Or use `F5` in VS Code (with CMake Tools extension)
- To add a dependency: `vcpkg add port <package-name>`

## Requirements

- CMake {{ cookiecutter.cmake_min_version }}+
- C++ compiler with C++{{ cookiecutter.cpp_standard }} support
- vcpkg
- Windows if you wnant to run batch scripts
