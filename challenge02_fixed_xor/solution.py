def fixed_xor(first_hex, second_hex):
    first_bytes = bytes.fromhex(first_hex)
    second_bytes = bytes.fromhex(second_hex)

    if len(first_bytes) != len(second_bytes):
        raise ValueError("Both inputs must have the same length")

    result = bytes(
        first_byte ^ second_byte
        for first_byte, second_byte in zip(first_bytes, second_bytes)
    )

    return result.hex()


first = "1c0111001f010100061a024b53535009181c"
second = "686974207468652062756c6c277320657965"

answer = fixed_xor(first, second)
print(answer)