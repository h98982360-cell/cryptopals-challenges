# Cryptopals Challenges

## Set 1, Challenge 1: Convert hex to Base64

The solution in `challenge1.py` uses `bytes.fromhex()` to convert the
hexadecimal representation into raw bytes. It then uses
`base64.b64encode()` to convert those bytes into the required Base64
representation.
