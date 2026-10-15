# Cryptopals Set 1 — Challenge 6: Break Repeating-Key XOR

This challenge provides a Base64-encoded file encrypted using repeating-key XOR
with an unknown key. The goal is to recover both the key and plaintext.

## Approach

1. Decode the Base64 input into bytes.
2. Calculate the Hamming distance between byte blocks.
3. Test key sizes from 2 to 40.
4. Normalize each Hamming distance by dividing it by the key size.
5. Select the most likely key sizes based on the lowest normalized distance.
6. Split the ciphertext into blocks of the selected key size.
7. Transpose the blocks so each group contains bytes encrypted with the same key byte.
8. Solve each transposed group using single-byte XOR frequency analysis.
9. Combine the recovered bytes into the full repeating key.
10. Decrypt the full ciphertext.

## Files

```text
solution.py           # Python solution
6.txt                 # Base64-encoded challenge data
README.md             # This documentation
```

## How to Run

```bash
python solution.py
```

## Expected Key

```text
Terminator X: Bring the noise
```

## What I Learned

- How to calculate Hamming distance between byte strings
- How normalized Hamming distance helps estimate repeating-key length
- How block transposition turns repeating-key XOR into multiple single-byte XOR problems
- How to combine frequency analysis with key-size detection

## Reference

- [Cryptopals Set 1, Challenge 6](https://cryptopals.com/sets/1/challenges/6)