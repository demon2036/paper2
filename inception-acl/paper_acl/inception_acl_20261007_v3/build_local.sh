#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
mkdir -p build-local
exec tectonic --keep-logs --keep-intermediates --synctex --outdir build-local "$@" main.tex
