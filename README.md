# Cookiecutter vcpkg C++ Library

A cross-platform cookiecutter template for pure C++ libraries using CMake, vcpkg, and GoogleTest.

## Generated project features

- C++17 static and shared libraries by default;
- example and GoogleTest targets;
- Windows Visual Studio 2022 and Linux Ninja presets;
- generated Windows/Linux GitHub Actions build-and-test workflow;
- Microsoft vcpkg as the default registry;
- `gtest` routed to `ScottChiuNYC/vcpkg-registry` so it does not acquire `pkgconf`;
- VS Code tasks and Windows batch helpers aligned with the preset layout.

## Usage

```bash
pip install cookiecutter
cookiecutter gh:scottchiunyc/cookiecutter-cpp-vcpkg
```

Or with `uv`:

```bash
uvx cookiecutter gh:scottchiunyc/cookiecutter-cpp-vcpkg
```

The default prompts include the project name and slug, description, author details, C++ standard, and minimum CMake version. The default CMake requirement is 3.23 because the generated project uses CMake Presets schema version 6.

## Generated build commands

### Windows

```powershell
cmake --preset windows-vcpkg
cmake --build --preset windows-release
ctest --preset windows-release-tests
```

### Linux

```bash
cmake --preset linux-vcpkg-release
cmake --build --preset linux-release
ctest --preset linux-release-tests
```

`VCPKG_ROOT` must reference a bootstrapped vcpkg checkout. The generated workflow reads `default-registry.baseline` from `vcpkg-configuration.json` before checking out vcpkg, so the tool and registry baseline remain aligned.

## Registry policy

Generated projects use two registries:

- `gtest` is resolved from `ScottChiuNYC/vcpkg-registry` at baseline `9e60f2f4c449410bf3b8ccd8fa11b1f3c38cf0f0`;
- all package names not explicitly assigned to that registry are resolved from Microsoft vcpkg.

The custom GoogleTest port retains the official package behavior but uses `vcpkg_fixup_pkgconfig(SKIP_CHECK)`, preventing vcpkg from acquiring or executing `pkgconf`.

## Template acceptance testing

`.github/workflows/template-acceptance.yml` generates a fresh `ci_sample` project independently on Windows and Linux, then:

1. verifies that Cookiecutter/Jinja rendered the generated workflow correctly;
2. verifies the exact custom-registry routing and pinned baselines;
3. configures the generated project through vcpkg;
4. confirms that `pkgconf` was neither installed nor acquired;
5. builds the static library, shared library, examples, and tests;
6. runs CTest.

This validates the template itself rather than relying on one previously generated repository.

## Adding dependencies

Inside a generated project:

```bash
vcpkg add port fmt
vcpkg add port spdlog
```

Additional packages use the Microsoft default registry unless their names are explicitly assigned to another registry in `vcpkg-configuration.json`.

## License

This cookiecutter template is MIT licensed.
