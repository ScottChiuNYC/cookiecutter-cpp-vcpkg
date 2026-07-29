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

## Dependencies and registries

`vcpkg.json` declares project dependencies. The generated `vcpkg-configuration.json` uses:

- `ScottChiuNYC/vcpkg-registry` for `gtest`;
- Microsoft vcpkg as the default registry for all other package names.

The custom `gtest` port preserves the official GoogleTest build and CMake targets, but configures pkg-config metadata with `SKIP_CHECK`, so vcpkg does not acquire or execute `pkgconf`.

When the custom registry publishes a new baseline, update the custom registry `baseline` in `vcpkg-configuration.json`. The Microsoft vcpkg checkout remains pinned by the separate `default-registry.baseline`.

## Continuous integration

`.github/workflows/build-and-test.yml` builds the library, examples, and tests on Windows and Linux, confirms that `pkgconf` was neither installed nor acquired, and runs CTest.

To add another dependency:

```bash
vcpkg add port <package-name>
```

Unless that package is explicitly listed under a custom registry's `packages`, it is resolved from the Microsoft default registry.
