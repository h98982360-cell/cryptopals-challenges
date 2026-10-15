# Cryptopals Set 1 — Challenge 5: Implement Repeating-Key XOR

This challenge requires implementing encryption using repeating-key XOR.

In repeating-key XOR, each plaintext byte is XORed with the corresponding byte
of a key. When the end of the key is reached, the key restarts from its first
byte.

## Formula

```text
ciphertext[i] = plaintext[i] XOR key[i % len(key)]
```

For example, using the key `ICE`:

```text
Plaintext: B U R N I N G
Key:       I C E I C E I
```

## Files

```text
solution.py           # Python implementation
README.md             # Project documentation
```

## How to Run

```bash
python solution.py
```

## Expected Output

```text
0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
```

## What I Learned

- How repeating-key XOR differs from single-byte XOR
- How to use the modulo operator to cycle through a key
- How to encrypt bytes and encode the result as hexadecimal
- Why repeating-key XOR is related to the Vigenère cipher

## Reference

- [Cryptopals Set 1, Challenge 5](https://cryptopals.com/sets/1/challenges/5)