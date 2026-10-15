
import base64
import urllib.request
from Crypto.Cipher import AES

# Download the challenge ciphertext
url = "https://cryptopals.com/static/challenge-data/7.txt"

with urllib.request.urlopen(url) as response:
    encoded_data = response.read()

# Decode Base64 into bytes
ciphertext = base64.b64decode(encoded_data)

# AES-128 key (exactly 16 bytes)
key = b"YELLOW SUBMARINE"

# Decrypt using AES in ECB mode
cipher = AES.new(key, AES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext)

# Display the decrypted message
print(plaintext.decode("utf-8", errors="replace"))
