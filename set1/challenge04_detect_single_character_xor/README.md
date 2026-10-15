# Cryptopals Set 1 — Challenge 4: Detect Single-Character XOR

The bundled sample contains hex-encoded strings, one of which has been
encrypted using single-byte XOR. The goal is to identify that string and
decrypt it.

## Approach

1. Read every line from `4.txt`.
2. Convert each hexadecimal line into bytes.
3. For every line, try all 256 possible single-byte XOR keys.
4. Score every decrypted candidate using English character frequency.
5. Keep the highest-scoring plaintext from each line.
6. Compare all line scores and return the overall best result.

This reuses the single-byte XOR cracking technique from Challenge 3, but applies
it to every ciphertext in the file.

## Files

```text
solution.py           # Python solution
4.txt                 # Challenge input data
README.md             # This documentation
```

## How to Run

```bash
python solution.py
```

## Expected Output

```text
Line: 4
Key: 53 (5)
Plaintext: Now that the party is jumping
```

## What I Learned

- How to detect single-byte XOR encryption among multiple ciphertexts
- How to reuse a frequency-analysis-based decryption function
- How to process files line by line in Python
- How to compare scores across multiple candidates to identify the most likely plaintext

## Reference

- [Cryptopals Set 1, Challenge 4](https://cryptopals.com/sets/1/challenges/4)
