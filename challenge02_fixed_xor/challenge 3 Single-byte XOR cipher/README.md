# Cryptopals Set 1 — Challenge 3: Single-byte XOR Cipher

This project solves Cryptopals Set 1, Challenge 3.

The challenge provides a hex-encoded string that has been XOR-encrypted using a
single unknown byte. The goal is to discover the key and recover the original
English message.

## Challenge

Given ciphertext:

```text
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
```

The plaintext was encrypted using:

```text
ciphertext = plaintext XOR key
```

where `key` is one unknown byte.

## How It Works

The solution uses brute force and frequency analysis:

1. Convert the hexadecimal ciphertext into bytes.
2. Try every possible single-byte key, from `0` to `255`.
3. XOR each key with every ciphertext byte.
4. Score each decrypted result based on how similar it is to English text.
5. Select the key that produces the highest English-like score.

English text contains common characters such as `e`, `t`, `a`, `o`, `i`, `n`,
and spaces. The correct decryption should contain many of these characters,
while incorrect keys usually produce unreadable output.

## Files

```text
challenge_03.py       # Python solution
README.md             # Project documentation
.gitignore            # Files that should not be uploaded to GitHub
```

## Requirements

- Python 3.8 or newer
- No external libraries are required

## How to Run

Open a terminal in the project folder and run:

```bash
python challenge_03.py
```

## Expected Output

```text
Key: 88 (X)
Plaintext: Cooking MC's like a pound of bacon
```

## What I Learned

- How XOR encryption works at the byte level
- How to convert hexadecimal data into bytes in Python
- How to brute-force a small keyspace
- How English character-frequency analysis can identify likely plaintext
- Why single-byte XOR encryption is not secure for protecting real data

## Reference

- [Cryptopals Set 1, Challenge 3](https://cryptopals.com/sets/1/challenges/3)