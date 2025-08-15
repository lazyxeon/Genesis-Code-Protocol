#pragma once
#include <numeric>
#include <vector>
inline int sum(const std::vector<int>& v){ return std::accumulate(v.begin(), v.end(), 0); }
