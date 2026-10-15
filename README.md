# Cryptopals Challenges

Solutions and notes for the Cryptopals cryptography challenges, implemented
with Python's standard library.

## Set 1

| Challenge | Topic | Folder |
| --- | --- | --- |
| 1 | Convert hex to Base64 | `set1/challenge01_hex_to_base64/` |
| 2 | Fixed XOR | `set1/challenge02_fixed_xor/` |
| 3 | Single-byte XOR cipher | `set1/challenge03_single_byte_xor/` |
| 4 | Detect single-character XOR | `set1/challenge04_detect_single_character_xor/` |
| 5 | Implement repeating-key XOR | `set1/challenge05_repeating_key_xor/` |
| 6 | Break repeating-key XOR | `set1/challenge06_break_repeating_key_xor/` |

Each challenge folder contains its `solution.py` and a challenge-specific
README. Challenges that require input data keep it alongside the solution.

## Requirements

- Python 3.8 or newer
- No third-party packages

Run a solution from its challenge folder, for example:

```bash
python solution.py
```

Challenge 4 and Challenge 6 read their bundled input files from the same
folder as their solution.
