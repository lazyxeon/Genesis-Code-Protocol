
# ModuLift v0.1 — Header-Unit First, Modules When Ready

ModuLift is a **drop-in, no-rewrite** accelerator for C++ developer experience (DX):
- Enables **Header Units** today (MSVC/Clang/GCC) using compiler-driven flows.
- Opportunistically enables **Named Modules** when your environment supports it (CMake ≥ 3.28 with module scanning; Ninja ≥ 1.11 or VS generators).
- Ships a tiny **diagnostics explainer** for common concept/template errors.
- Includes a **benchmark harness** and **CI workflow** to capture p50 build-time deltas **with vs without** ModuLift.

> CMake **does not support header units** (as of 3.28+). We drive HU via compiler flags and prebuilt CMIs/IFCs. Named Modules use CMake's module scanning + file sets when available.

## Quick Start (5 steps)

1. Copy the `cmake/`, `scripts/`, and `tools/` folders into your repo.
2. In your `CMakeLists.txt`, include the ModuLift wiring and toggle:
   ```cmake
   option(MODULIFT_ENABLE "Enable ModuLift header-units/modules glue" ON)
   include(cmake/modulift/enable-named-modules.cmake) # safe everywhere

   if (MSVC)
     include(cmake/modulift/hu-msvc.cmake)
     modulift_target_use_hus(<your-targets>)
   elseif (CMAKE_CXX_COMPILER_ID STREQUAL "Clang" OR CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
     include(cmake/modulift/hu-clang-gcc.cmake)
     modulift_target_use_hus(<your-targets>)
   endif()
   ```
3. List 2–6 high-payoff headers in `cmake/modulift/headers.cmake`.
4. Build locally:
   ```bash
   cmake -S . -B build -G Ninja -DCMAKE_CXX_STANDARD=20
   cmake --build build -v
   ```
5. Benchmark:
   ```bash
   bash scripts/bench_build.sh 7        # Linux/macOS
   pwsh scripts/bench_build.ps1 -Runs 7 # Windows/MSVC
   ```

## What you get

- **Header Units** today (no source rewrites): MSVC uses `/exportHeader` to produce `.ifc` and consumes via `/headerUnit` or `/ifcMap` (TOML). Clang/GCC precompile header units and consume via `-fmodule-file` (Clang) or `-fmodules-ts/-fmodule-header` (GCC).
- **Named Modules** via CMake 3.28+ when supported, using `CMAKE_CXX_SCAN_FOR_MODULES` and `FILE_SET CXX_MODULES` (Ninja/VS generators). If unsupported, ModuLift simply does nothing on that front and HU still provides value.
- **Explain mode**: post-process common concept/template diagnostics into short, actionable hints (no compiler patches).

## References (helpful docs)

- CMake C++ modules manual (`cmake-cxxmodules(7)`): header units not supported; scanning requirements; Ninja≥1.11/VS generators; no built-in `import std;` support.
- MSVC header units: `/exportHeader`, `/headerUnit`, `/ifcMap` TOML format.
- Clang C++20 modules & header units: `-fmodule-header`, consumption via `-fmodule-file=…`; `clang-scan-deps` importance.
- GCC C++20 modules & header units: `-fmodules-ts`, `-fmodule-header`, `-x c++-user-header`.
- Real-world ROI: Microsoft Office/Word reports **best-case +21.3% build throughput** migrating PCH→Header Units.

See the `REFERENCES.md` file for direct links.

## License
This bundle is provided under the same license as your repository (likely MIT). Modify as you see fit.
