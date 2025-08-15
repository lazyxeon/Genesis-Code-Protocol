#pragma once
#include <string>
#include <vector>
// Pretend this is a heavy fan-out header in your codebase.
// It is a good candidate for header-unit precompilation.
inline std::string greet(const std::string& name){ return "hi " + name; }
