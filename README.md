# Cookiecutter vcpkg C++ Library

A cookiecutter template for creating pure C++ libraries with vcpkg and CMake.

## Features

- **CMake** - Modern C++ build system
- **vcpkg** - Cross-platform C++ package manager
- **Google Test (GTest)** - Unit testing framework
- **VS Code Integration** - Ready for VS Code with CMake Tools
- **Windows Batch Scripts** - Quick build and git push helpers

## Usage

### Installation

```bash
pip install cookiecutter
```

### Create a new C++ library

```bash
cookiecutter gh:scottchiunyc/cookiecutter-cpp-vcpkg
```

Or with `uv`:

```bash
uvx cookiecutter gh:scottchiunyc/cookiecutter-cpp-vcpkg
```

### Answer the prompts

- `project_name`: Name of your library (e.g., "My Cool Library")
- `project_slug`: Lowercase underscore-separated identifier (auto-generated)
- `project_description`: Short description
- `author_name`: Your name
- `author_email`: Your email
- `cpp_standard`: C++ standard version (default: 17)
- `cmake_min_version`: Minimum CMake version (default: 3.15)

## Project Structure

```
my_project/
├── src/                    # Library source files
│   ├── CMakeLists.txt     # Library build configuration
│   ├── example.cpp
│   └── ...
├── include/
│   └── my_project/        # Public headers
│       ├── example.h
│       └── ...
├── tests/                 # Unit tests
│   ├── CMakeLists.txt
│   ├── example_test.cpp
│   └── ...
├── examples/              # Example programs
│   ├── CMakeLists.txt
│   ├── demo.cpp
│   └── ...
├── .vscode/               # VS Code configuration
├── CMakeLists.txt         # Root CMake configuration
├── CMakePresets.json      # CMake presets
├── vcpkg.json             # vcpkg dependencies
├── vcpkg-configuration.json
├── cnb.bat                # Build and test script
├── cnp.bat                # Git push script
├── LICENSE
└── README.md
```

## Getting Started

1. **Initialize vcpkg** (one-time):
   ```bash
   git clone https://github.com/microsoft/vcpkg.git
   cd vcpkg && .\bootstrap-vcpkg.bat
   set "VCPKG_ROOT=C:\path\to\vcpkg"
   set PATH=%VCPKG_ROOT%;%PATH%
   ```

2. **Initialize in project**:
   ```bash
   vcpkg new --application
   ```

3. **Build**:
   ```bash
   .\cnb.bat  # Windows
   ```

4. **In VS Code**:
   - Press `F5` to build and debug
   - CMake Tools extension is recommended

## Adding Dependencies

```bash
vcpkg add port fmt
vcpkg add port spdlog
```

This automatically updates `vcpkg.json` and downloads dependencies.

## Building

- **Debug**: `cmake --build build --config Debug`
- **Release**: `cmake --build build --config Release`
- **Quick build & test**: `cnb.bat`

## Running Tests

```bash
.\build\tests\Debug\my_project_test.exe
```

Or with CTest:

```bash
cd build
ctest --output-on-failure
```

## Notes

- Targets are named after `project_slug` (e.g., `my_project`)
- Static library: `my_project`
- Shared library: `my_project_shared`
- Test executable: `my_project_test`
- Each subdirectory (`src`, `tests`, `examples`) has its own `CMakeLists.txt`

## License

This cookiecutter template is MIT licensed.

## Author

{{ cookiecutter.author_name }}

