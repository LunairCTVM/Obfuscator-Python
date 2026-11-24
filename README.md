# Python Source Obfuscator

A small Python project that renames variables, functions, classes, and arguments in a Python source file using Python's AST.

> Note: The selected file is overwritten. Make a backup before running the obfuscator.

---

## Project Files

- `Obfuscator.py`: Reads a Python file, obfuscates eligible names, and writes the result back to that same file.
- `Teste/`: Example Python files.

---

## Requirements

- Python 3.9 or newer
- No third-party packages required

---

## Usage

1. Run the obfuscator:
```bash
python Obfuscator.py
```

2. When prompted, enter the path to the Python file you want to obfuscate.

3. The obfuscated code replaces the contents of the selected file.

---

## Limitations

- This is a basic learning project, not a security or code-protection guarantee.
- Dynamic name lookups, reflection, and other runtime-dependent behavior may not work after obfuscation.
- The source file is modified in place; keep a copy of the original.
