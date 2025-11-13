#!/usr/bin/env bash
set -euo pipefail
sudo apt install python3 -y
clear
cd "$(dirname "$0")"
PY=python3
if ! command -v "$PY" >/dev/null 2>&1; then
  if command -v python >/dev/null 2>&1 && python -c 'import sys; sys.exit(0) if sys.version_info[0]>=3 else sys.exit(1)'; then
    PY=python
  else
    echo "Python 3 is required. Install package 'python3' and retry." >&2
    exit 1
  fi
fi
[ -f note.py ] || { echo "note.py not found in $(pwd)" >&2; exit 2; }
exec "$PY" note.py "$@"

 #made by AI but note.py is not 