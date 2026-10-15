HEX_CIPHERTEXT = (
    "1b37373331363f78151b7f2b783431333d"
    "78397828372d363c78373e783a393b3736"
)

def xor_with_key(data: bytes, key: int) -> bytes:
    return bytes(byte ^ key for byte in data)

def english_score(text: str) -> float:
    common = "etaoinshrdlcumwfgypbvkjxqz ETAOINSHRDLCUMWFGYPBVKJXQZ"
    return sum(text.count(char) for char in common)

def solve_single_byte_xor(hex_ciphertext: str):
    ciphertext = bytes.fromhex(hex_ciphertext)

    best_score = -1
    best_key = None
    best_plaintext = None

    for key in range(256):
        decrypted = xor_with_key(ciphertext, key)

        if any(b < 32 and b not in (9, 10, 13) for b in decrypted):
            continue

        text = decrypted.decode("latin-1")
        score = english_score(text)

        if score > best_score:
            best_score = score
            best_key = key
            best_plaintext = text

    return best_key, best_plaintext, best_score

key, plaintext, score = solve_single_byte_xor(HEX_CIPHERTEXT)

print(f"Key: {key} ({chr(key)})")
print(f"Score: {score}")
print(f"Plaintext: {plaintext}")