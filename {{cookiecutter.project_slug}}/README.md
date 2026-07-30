# {{ cookiecutter.project_name }}

A cross-platform C++{{ cookiecutter.cpp_standard }} library using CMake, vcpkg, and GoogleTest.

## Requirements

- CMake {{ cookiecutter.cmake_min_version }}+
- a vcpkg checkout referenced by `VCPKG_ROOT`
- Visual Studio 2022 on Windows
- Ninja and a compatible C++ compiler on Linux

## Windows

```powershell
cmake --preset windows-vcpkg
cmake --build --preset windows-release
ctest --preset windows-release-tests
```

For a Debug developer build, `cnb.bat` configures, builds, and runs CTest.

## Linux

```bash
cmake --preset linux-vcpkg-release
cmake --build --preset linux-release
ctest --preset linux-release-tests
```

## Dependencies and overlay ports

`vcpkg.json` declares project dependencies. The generated `vcpkg-configuration.json` uses Microsoft vcpkg as the only package registry and declares the repository-local `vcpkg-ports` directory as an overlay.

The `gtest` dependency is resolved from `vcpkg-ports/gtest` before registry lookup. This local port preserves the official GoogleTest build and standard `GTest::*` CMake targets, but configures pkg-config metadata with `SKIP_CHECK`, so vcpkg does not acquire or execute `pkgconf`.

No personal vcpkg registry is required. When the custom recipe changes, update the files under `vcpkg-ports/gtest` and validate the project on Windows and Linux. All other package names continue to resolve from the Microsoft default registry.

## Continuous integration

`.github/workflows/build-and-test.yml` builds the library, examples, and tests on Windows and Linux, confirms that `pkgconf` was neither installed nor acquired, and runs CTest. Changes under `vcpkg-ports` also trigger the workflow.

To add another dependency:

```bash
vcpkg add port <package-name>
```

The package resolves from Microsoft vcpkg unless a same-named local port exists under `vcpkg-ports`.
