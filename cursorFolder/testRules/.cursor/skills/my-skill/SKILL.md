---
name: my-skill
description: Builds and runs small Python utilities that read tabular files from input/ using Polars, handles Windows UTF-8 output, documents the project venv interpreter, and adds a fixed skill marker comment in Python sources. Use when the user works with input/, CSV or row previews, print_input_top_rows.py, or local data scripts in this repository.
---

# my-skill

## When this applies

Use for **this repo** when adding or changing **Python** tools that load data from **`input/`**, preview rows, or follow the same patterns as `print_input_top_rows.py`.

## Instructions

1. **Skill marker (Python)** — Whenever this skill guides **creating or editing** a `.py` file, ensure the file contains this exact line **once** (ASCII), unless it is already present:

   `# used skill file my-skill`

   Place it near the top: after the module docstring (if any) and optional `from __future__` imports, before the remaining imports, unless the file layout makes another single location clearly better. If **`.cursor/rules/my-df-rule.mdc`** also applies, both marker lines may appear (typically adjacent); do not duplicate either line.

2. **Tabular data** — Use **Polars** (`import polars as pl`) for CSV-style files. Prefer `pl.read_csv(path, n_rows=…)` for head-style previews unless the user needs full scans.
3. **`input/` layout** — Treat `input/` as the data drop folder at the project root (sibling of scripts). Resolve paths with `Path(__file__).resolve().parent / "input"` unless the user specifies another layout.
4. **Windows console** — If printing Polars frames or Unicode to the terminal may fail on cp1252, reconfigure stdout when available:

   ```python
   if hasattr(sys.stdout, "reconfigure"):
       sys.stdout.reconfigure(encoding="utf-8", errors="replace")
   ```

5. **How to run** — Document commands using this interpreter (adjust path if the user changes their venv):

   `C:/pythonprojects/venv/Scripts/python.exe path/to/script.py`

6. **Project rules** — For Python files, also follow **`.cursor/rules/my-df-rule.mdc`** (Polars preference, `# my-df-rule used` marker when that rule is in scope).

## Do not

- Add pandas for new tabular code unless the user or an existing rule requires it.
- Reintroduce `.vscode/` unless the user explicitly asks for editor configuration.

## Quick example

```python
"""Example data preview script."""

from __future__ import annotations

# my-df-rule used
# used skill file my-skill

from pathlib import Path
import polars as pl

input_dir = Path(__file__).resolve().parent / "input"
df = pl.read_csv(next(input_dir.glob("*.csv")), n_rows=10, encoding="utf8")
print(df)
```
