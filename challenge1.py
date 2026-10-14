import base64

hex_input = (
    "49276d206b696c6c696e6720796f757220627261696e206c696b652061"
    "20706f69736f6e6f7573206d757368726f6f6d"
)

raw_bytes = bytes.fromhex(hex_input)
base64_output = base64.b64encode(raw_bytes).decode("ascii")

print(base64_output)