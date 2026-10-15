def repeating_key_xor(plaintext: bytes, key: bytes) -> bytes:
    return bytes(
        plaintext_byte ^ key[index % len(key)]
        for index, plaintext_byte in enumerate(plaintext)
    )

def main():
    plaintext = (
        "Burning 'em, if you ain't quick and nimble\n"
        "I go crazy when I hear a cymbal"
    ).encode()

    key = b"ICE"

    ciphertext = repeating_key_xor(plaintext, key)

    print(ciphertext.hex())

if __name__ == "__main__":
    main()