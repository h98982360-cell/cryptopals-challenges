from pathlib import Path


BLOCK_SIZE = 16


def count_repeated_blocks(ciphertext):
    blocks = [
        ciphertext[index:index + BLOCK_SIZE]
        for index in range(0, len(ciphertext), BLOCK_SIZE)
    ]

    return len(blocks) - len(set(blocks))


def main():
    input_path = Path(__file__).with_name("8.txt")

    if not input_path.exists():
        raise FileNotFoundError(f"File not found: {input_path}")

    lines = input_path.read_text().splitlines()

    best_line_number = None
    best_ciphertext = None
    highest_repeat_count = 0

    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue

        ciphertext = bytes.fromhex(line.strip())
        repeat_count = count_repeated_blocks(ciphertext)

        if repeat_count > highest_repeat_count:
            highest_repeat_count = repeat_count
            best_line_number = line_number
            best_ciphertext = line.strip()

    print(f"ECB candidate line: {best_line_number}")
    print(f"Repeated blocks: {highest_repeat_count}")
    print(f"Ciphertext: {best_ciphertext}")


if __name__ == "__main__":
    main()