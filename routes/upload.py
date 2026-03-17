from encryption.aes import *
from encryption.ecc import *
import os

def encrypt_and_store(file_path):

    os.makedirs("storage/encrypted_files", exist_ok=True)
    os.makedirs("storage/keys", exist_ok=True)

    # Read file
    with open(file_path, "rb") as f:
        data = f.read()

    # AES encryption
    aes_key = generate_aes_key()

    # 🔥 PRINT KEY FOR USER
    print("\n🔑 AES Key (SAVE THIS):", aes_key.hex(), "\n")

    enc = encrypt_file(data, aes_key)

    # Save encrypted file
    with open("storage/encrypted_files/file.bin", "wb") as f:
        f.write(enc["nonce"] + enc["tag"] + enc["ciphertext"])

    print("✅ File encrypted successfully!")