"""Break repeating-key XOR encryption from a Base64 input file."""

import base64
from pathlib import Path

def hamming_distance(a: bytes, b: bytes) -> int:
    if len(a) != len(b):
        raise ValueError("Inputs must have the same length")

    return sum(bin(byte1 ^ byte2).count("1") for byte1, byte2 in zip(a, b))

def english_score(data: bytes) -> float:
    text = data.decode("latin-1")
    letter_frequencies = {
        "e": 12.7, "t": 9.1, "a": 8.2, "o": 7.5, "i": 7.0, "n": 6.7,
        "s": 6.3, "h": 6.1, "r": 6.0, "d": 4.3, "l": 4.0, "u": 2.8,
        "c": 2.8, "m": 2.4, "f": 2.2, "w": 2.4, "y": 2.0, "p": 1.9,
        "g": 2.0, "b": 1.5, "v": 1.0, "k": 0.8, "x": 0.2, "j": 0.15,
        "q": 0.1, "z": 0.07,
    }
    score = 0.0

    for char in text:
        if char.isalpha() and char.isascii():
            score += letter_frequencies.get(char.lower(), 0.0)
            if char.isupper():
                score -= 0.5
        elif char == " ":
            score += 13.0
        elif char in "\n\r\t":
            score += 1.0
        elif char in ".,'!?;:-\"()":
            score += 1.0
        elif char.isprintable():
            score -= 2.0
        else:
            score -= 20.0

    return score

def best_single_byte_xor(data: bytes):
    best_score = -1
    best_key = None
    best_plaintext = None

    for key in range(256):
        decrypted = bytes(byte ^ key for byte in data)

        score = english_score(decrypted)

        if score > best_score:
            best_score = score
            best_key = key
            best_plaintext = decrypted

    return best_score, best_key, best_plaintext

def guess_keysize(ciphertext: bytes, min_size=2, max_size=40):
    scores = []

    for keysize in range(min_size, max_size + 1):
        blocks = []

        for i in range(0, len(ciphertext) - keysize + 1, keysize):
            blocks.append(ciphertext[i:i + keysize])

        distances = []
        for i in range(len(blocks) - 1):
            distance = hamming_distance(blocks[i], blocks[i + 1])
            distances.append(distance / keysize)

        average_distance = sum(distances) / len(distances)
        scores.append((average_distance, keysize))

    scores.sort()
    return scores[:5]

def transpose_blocks(ciphertext: bytes, keysize: int):
    transposed = [[] for _ in range(keysize)]

    for index, byte in enumerate(ciphertext):
        transposed[index % keysize].append(byte)

    return [bytes(block) for block in transposed]

def break_repeating_key_xor(ciphertext: bytes):
    likely_keysizes = guess_keysize(ciphertext)

    best_result = None

    for _, keysize in likely_keysizes:
        transposed_blocks = transpose_blocks(ciphertext, keysize)

        key = bytearray()
        total_score = 0

        for block in transposed_blocks:
            score, key_byte, _ = best_single_byte_xor(block)
            key.append(key_byte)
            total_score += score

        decrypted = bytes(
            byte ^ key[index % len(key)]
            for index, byte in enumerate(ciphertext)
        )

        if best_result is None or total_score > best_result[0]:
            best_result = (total_score, bytes(key), decrypted)

    return best_result[1], best_result[2]

def main():
    path = Path(__file__).parent / "6.txt"

    with path.open("r", encoding="utf-8") as file:
        base64_data = "".join(line.strip() for line in file)

    ciphertext = base64.b64decode(base64_data)

    key, plaintext = break_repeating_key_xor(ciphertext)

    print("Key:", key.decode("latin-1"))
    print("\nPlaintext:\n")
    print(plaintext.decode("latin-1"))

if __name__ == "__main__":
    main()