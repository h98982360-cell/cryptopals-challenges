import argparse
from pathlib import Path

def xor_with_key(data: bytes, key: int) -> bytes:
    return bytes(byte ^ key for byte in data)

def english_score(data: bytes) -> float:
    text = data.decode("latin-1")
    common = "etaoinshrdlcumwfgypbvkjxqz ETAOINSHRDLCUMWFGYPBVKJXQZ"
    return sum(text.count(char) for char in common)

def is_mostly_printable(data: bytes) -> bool:
    return all(
        32 <= byte < 127 or byte in (9, 10, 13)
        for byte in data
    )

def best_single_byte_xor(ciphertext: bytes):
    best_score = -1
    best_key = None
    best_plaintext = None

    for key in range(256):
        decrypted = xor_with_key(ciphertext, key)

        if not is_mostly_printable(decrypted):
            continue

        score = english_score(decrypted)

        if score > best_score:
            best_score = score
            best_key = key
            best_plaintext = decrypted

    return best_score, best_key, best_plaintext

def solve_challenge_04(filename: str = "4.txt"):
    best_overall_score = -1
    best_line_number = None
    best_key = None
    best_plaintext = None

    path = Path(__file__).parent / filename

    with path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line:
                continue

            ciphertext = bytes.fromhex(line)
            score, key, plaintext = best_single_byte_xor(ciphertext)

            if score > best_overall_score:
                best_overall_score = score
                best_line_number = line_number
                best_key = key
                best_plaintext = plaintext

    if best_key is None or best_plaintext is None:
        raise ValueError(f"No mostly printable plaintext found in {path}")

    return best_line_number, best_key, best_plaintext

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Detect the line encrypted with single-byte XOR."
    )
    parser.add_argument(
        "filename",
        nargs="?",
        default="4.txt",
        help="path to the hex-encoded ciphertext file (default: 4.txt)",
    )
    args = parser.parse_args()
    line_number, key, plaintext = solve_challenge_04(args.filename)

    print(f"Line: {line_number}")
    print(f"Key: {key} ({chr(key)})")
    print(f"Plaintext: {plaintext.decode('latin-1')}")