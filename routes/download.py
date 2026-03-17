from encryption.aes import *
import os

def decrypt_and_load():

    # Load encrypted file
    with open("storage/encrypted_files/file.bin", "rb") as f:
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    # 🔥 ASK USER FOR KEY
    key_input = input("🔑 Enter AES key (hex): ")

    try:
        aes_key = bytes.fromhex(key_input)

        # Decrypt
        data = decrypt_file(nonce, tag, ciphertext, aes_key)

        # Save output
        with open("storage/decrypted.txt", "wb") as f:
            f.write(data)

        print("✅ File decrypted successfully!")

    except Exception as e:
        print("❌ Decryption failed:", str(e))