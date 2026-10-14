# Copier C++ vcpkg Library

A pure C++17 library with independent static/shared targets, CMake, vcpkg and GoogleTest. This repository is migrated in place from Cookiecutter; it now uses the `copier-` repository name.

## Generate and update a project

```bash
pip install copier==9.19.1
copier copy gh:ScottChiuNYC/copier-cpp-vcpkg my-project
cd my-project
git init
git add .
git commit -m "Generate project"
# After committing your project changes, update to the latest template revision:
copier update
```

Copier records answers and the template version in `.copier-answers.yml`; commit it. Release versions are Git tags. The template lives under `template/`, so template metadata and its Git history are not copied into generated projects. Existing Cookiecutter-generated projects need deliberate adoption and review before using Copier updates; this migration does not rewrite those projects.

## Fresh Work / Codex / developer setup

Prerequisites: Python 3.12+, Git, and a C++17 compiler. Linux needs GCC or Clang plus curl, zip, unzip and tar. Windows needs Visual Studio 2022 with Desktop development with C++ and a Windows SDK (the `windows-2022` Actions image supplies them). Native compilers are platform prerequisites, not installed by pip.

From a fresh clone, on either Windows or Linux:

```bash
python scripts/bootstrap.py
python scripts/validate_template.py
```

Bootstrap installs the exact tool versions in `template/scripts/tool-requirements.txt` into `.dev-tools/venv`, checks out the vcpkg baseline declared in `template/vcpkg-configuration.json`, and bootstraps it. Validation needs no activation, manual PATH changes, or exported variables. Both platforms supply the installed Ninja path to nested vcpkg processes; Linux also pins the parent configure path. Compiler tracking stays enabled, and Windows retains the Visual Studio preset.

To reuse an already pinned vcpkg checkout:

```bash
python scripts/bootstrap.py --vcpkg-root /absolute/path/to/vcpkg
```

That checkout must already match the declared baseline and is not checked out to another version. Re-running bootstrap reuses installed tools and downloads. Use `--work-dir .validation` on validation to keep generated artifacts; that directory must be empty. The two repositories maintain their own scripts and their independent project architectures.

## Validation and CI

The validation script exercises default/custom Copier copy, real `v1.0.0` → `v1.1.0` updates in an isolated fixture, preservation of local README edits, answer/version persistence, identifier rejection and GitHub expression rendering. It then configures/builds the updated sample and runs its original tests. The static and shared libraries, example and GoogleTest executable are all built.

`.github/workflows/template-acceptance.yml` runs these same two commands on Linux and Windows. Generated projects include their own bootstrap/validation scripts and a Windows/Linux workflow using those scripts. The vcpkg GoogleTest overlay remains local and validation checks that `pkgconf` was not installed or acquired.

Generated projects build automatically on push and pull request, with a manual workflow trigger also available. Their workflow is the ordinary file `template/.github/workflows/build-and-test.yml`, copied unchanged by Copier. Bootstrap and validation scripts are ordinary Python files under `scripts/`; `.jinja` is used only for project-specific substitution. Template validation checks both workflows' triggers, platform matrix and script entry points before executing the sample build/tests.

No Docker, services, shell activation, personal vcpkg registry or custom infrastructure is needed. The first run downloads tools and compiles dependencies; later runs reuse local caches. Template acceptance on push allows Windows/Linux checks to finish before opening the migration PR.

## Generated C++ packages

Generated projects now install public headers, compiled libraries, and relocatable CMake config/version/target files. With default answers, the port is `my-project`, the CMake package is `my_project`, and the consumer target is `my_project::my_project`. `vcpkg_port_name` is a separate lowercase/hyphenated Copier answer; it does not rename the CMake API or the root dependency manifest. `version` supplies the CMake package version (numeric `major.minor.patch`).

The generated README contains exact Linux/PowerShell commands for installing the local port and consuming it in an independent project. The port remains inside the generated source checkout; it builds that working tree, with no registry, upload, release workflow, Python tooling, or test dependency required by the C++ consumer. Run `python scripts/validate_vcpkg.py` after bootstrap to exercise just packaging; the normal generated validation invokes it automatically.

Packaging acceptance installs into a fresh consumer manifest, disables binary caching for mutable local sources, relocates the installed prefix, hides source headers, checks imported include/library/config paths, and compiles/links/runs both Release and Debug consumers. It tests static and shared linkage on both platforms; regular preset builds still build both independent targets. Windows function exports use `WINDOWS_EXPORT_ALL_SYMBOLS`; global data or certain virtual-class interfaces need explicit DLL import/export annotations when introduced.

The existing tagged `v1.0.0` → `v1.1.0` fixture remains. A separate fixture generates from the pre-packaging master commit, updates through isolated `v2.0.0` → `v2.1.0` tags, retains user source edits/files and existing answers, then runs the installed consumer. Acceptance checkouts include Git history for this fixture. No real downstream repository is updated.
