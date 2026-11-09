#!/usr/bin/env bash
set -euo pipefail

if [[ $# != 3 ]]; then
  echo 'Usage: bash scripts/run_maintainability.sh SOURCE DECIDIM OUTPUT' >&2
  exit 2
fi

task_source=$(realpath "$1")
task_core=$(realpath "$2")
mkdir -p "$3"
task_output=$(realpath "$3")
task_scripts=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
task_image='registry.gitlab.com/lappis-unb/decidimbr/dev/participa@sha256:f0ddf9c5faed72d5b49e15a56c2858c2545779576a8eb635b2f6bbd68743c953'

if [[ -e "$task_output/execution.json" || -e "$task_output/summary.json" ]]; then
  echo 'Use a new output directory to preserve existing evidence.' >&2
  exit 2
fi

docker run --rm --pull never --network none --user "$(id -u):$(id -g)" \
  --entrypoint /bin/sh \
  -v "$task_source:/source:ro" -v "$task_core:/core:ro" \
  -v "$task_scripts:/tools:ro" -v "$task_output:/output" -w /tmp \
  "$task_image" -c '
    ruby /tools/collect_maintainability.rb /source /core /output || exit $?
    rubocop --ignore-disable-comments --cache false --config /tools/maintainability.rubocop.yml \
      --only Metrics/CyclomaticComplexity --format json --out /output/M2.2-rubocop.json \
      /source/app/commands /source/app/controllers /source/app/permissions /source/app/services
    result=$?
    test "$result" -le 1
  '
python3 "$task_scripts/verify_maintainability.py" "$task_output" > "$task_output/verification.json"
