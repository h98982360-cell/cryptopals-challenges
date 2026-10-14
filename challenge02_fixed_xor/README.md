# Challenge 2: Fixed XOR

The goal is to XOR two equal-length hexadecimal strings.

First, I converted both hexadecimal strings into raw bytes using
`bytes.fromhex()`. I then XORed each pair of corresponding bytes and
converted the result back to hexadecimal.

## Output

746865206b696420646f6e277420706c6179