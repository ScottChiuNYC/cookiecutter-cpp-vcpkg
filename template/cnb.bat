@echo off
setlocal

cmake --preset windows-vcpkg
if errorlevel 1 exit /b %errorlevel%

cmake --build --preset windows-debug
if errorlevel 1 exit /b %errorlevel%

ctest --preset windows-debug-tests
exit /b %errorlevel%
