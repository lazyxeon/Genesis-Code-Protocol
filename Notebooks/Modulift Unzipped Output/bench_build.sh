#!/usr/bin/env bash
set -euo pipefail
RUNS="${1:-7}"
bench() {
  local name="$1" enable="$2"
  rm -rf "build_${name}" || true
  cmake -S . -B "build_${name}" -G Ninja -DCMAKE_CXX_STANDARD=20 -DMODULIFT_ENABLE=${enable}
  local times=()
  for i in $(seq 1 "${RUNS}"); do
    /usr/bin/time -f "%e" -o "build_${name}/.t" cmake --build "build_${name}" -v >/dev/null
    times+=("$(cat build_${name}/.t)")
    cmake --build "build_${name}" --target clean >/dev/null
  done
  printf "%s
" "${times[@]}" | awk '
    {a[NR]=$1} END{
      n=asort(a);
      median=(n%2?a[(n+1)/2]:(a[n/2]+a[n/2+1])/2);
      print "median_sec=" median
    }'
}
echo "[with   ] $(bench with   ON)"
echo "[without] $(bench without OFF)"
