# Challenge 8: Detect AES in ECB Mode

## Objective

Find which hexadecimal ciphertext was encrypted using AES in ECB mode.

## Method

1. Read each ciphertext line from `8.txt`.
2. Convert each line from hexadecimal into raw bytes.
3. Split the bytes into 16-byte blocks.
4. Count repeated blocks.
5. Select the ciphertext with the most repeated blocks.

## Why it works

AES has a 16-byte block size. ECB mode encrypts identical plaintext blocks into identical ciphertext blocks, so repeated ciphertext blocks can reveal ECB mode.

## Result

The program prints the candidate line number, repeated-block count, and ciphertext.