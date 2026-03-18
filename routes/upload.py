from encryption.aes import *
from encryption.ecc import *
import os

def encrypt_and_store(file_path):

    os.makedirs("storage/encrypted_files", exist_ok=True)
    os.makedirs("storage/keys", exist_ok=True)

    # Read file
    with open(file_path, "rb") as f:
        data = f.read()

    # 🔐 Step 1: Generate AES key
    aes_key = generate_aes_key()

    # 🔐 Step 2: AES Encrypt file
    enc = encrypt_file(data, aes_key)

    # Save encrypted file
    with open("storage/encrypted_files/file.bin", "wb") as f:
        f.write(enc["nonce"] + enc["tag"] + enc["ciphertext"])

    # 🔐 Step 3: ECC Key Generation
    private_key, public_key = generate_keys()
    save_keys(private_key, public_key)

    # 🔐 Step 4: Derive shared key
    derived_key = derive_shared_key(private_key, public_key)

    # 🔐 Step 5: Encrypt AES key using ECC (XOR method)
    encrypted_aes_key = encrypt_aes_key(aes_key, derived_key)

    # Save encrypted AES key
    with open("storage/keys/encrypted_aes_key.bin", "wb") as f:
        f.write(encrypted_aes_key)

    # ✅ Return AES key (for testing/demo only)
    return aes_key.hex()