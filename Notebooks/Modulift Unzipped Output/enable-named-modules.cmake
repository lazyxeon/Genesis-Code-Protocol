# Enable named modules only where supported; header units are handled separately.
cmake_minimum_required(VERSION 3.28)
set(CMAKE_CXX_STANDARD 20)
# Let CMake ask the compiler to scan module deps (P1689) when supported.
set(CMAKE_CXX_SCAN_FOR_MODULES ON)  # see cmake-cxxmodules(7)
# Generators that support scanning: Ninja (>=1.11), Ninja Multi-Config, VS 2022.
# Limitations per docs: Header units are NOT supported by CMake; no builtin import std;.
