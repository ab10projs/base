"""Print the first 10 CSV rows for each regular file in input/ (Polars).

Run: C:/pythonprojects/venv/Scripts/python.exe print_input_top_rows.py
"""

from __future__ import annotations

# my-df-rule used
# used skill file my-skill
# the subagent my-subagent file was used

import sys
from pathlib import Path

import polars as pl

INPUT_DIR = Path(__file__).resolve().parent / "input"
ROW_LIMIT = 10


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    if not INPUT_DIR.is_dir():
        print(f"No input folder: {INPUT_DIR}", file=sys.stderr)
        sys.exit(1)

    paths = sorted(p for p in INPUT_DIR.iterdir() if p.is_file())
    if not paths:
        print(f"No files in {INPUT_DIR}", file=sys.stderr)
        return

    for path in paths:
        print(f"=== {path.name} (first {ROW_LIMIT} rows) ===")
        try:
            df = pl.read_csv(
                path,
                n_rows=ROW_LIMIT,
                encoding="utf8",
                try_parse_dates=True,
            )
            print(df)
        except Exception as e:
            print(f"(error: {e})", file=sys.stderr)
        print()


if __name__ == "__main__":
    main()
