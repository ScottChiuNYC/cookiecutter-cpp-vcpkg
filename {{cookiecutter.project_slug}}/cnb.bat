cmake --preset=vcpkg
@REM cmake --build build --config Release
@REM .\build\tests\Release\{{ cookiecutter.project_slug }}_test.exe
cmake --build build --config Debug
.\build\tests\Debug\{{ cookiecutter.project_slug }}_test.exe
