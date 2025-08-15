param([int]$Runs = 7)
$ErrorActionPreference = "Stop"
function Bench($Name, $Enable) {
  Remove-Item -Recurse -Force "build_$Name" -ErrorAction SilentlyContinue
  cmake -S . -B "build_$Name" -G "Ninja" -DCMAKE_CXX_STANDARD=20 -DMODULIFT_ENABLE=$Enable
  $times = @()
  for ($i=0; $i -lt $Runs; $i++) {
    $sw = [Diagnostics.Stopwatch]::StartNew()
    cmake --build "build_$Name" -v | Out-Null
    $sw.Stop()
    $times += $sw.Elapsed.TotalSeconds
    cmake --build "build_$Name" --target clean | Out-Null
  }
  $sorted = $times | Sort-Object
  $n = $sorted.Count
  if ($n % 2 -eq 1) { $median = $sorted[([int]($n/2))] } else { $median = ($sorted[$n/2-1] + $sorted[$n/2]) / 2 }
  "median_sec=$median"
}
"[with   ] $(Bench 'with'    'ON')"
"[without] $(Bench 'without' 'OFF')"
