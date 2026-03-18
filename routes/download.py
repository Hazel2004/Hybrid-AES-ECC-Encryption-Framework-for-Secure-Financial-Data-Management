from encryption.aes import *
from encryption.ecc import *
import os

def decrypt_and_load():

    # Load encrypted file
    with open("storage/encrypted_files/file.bin", "rb") as f:
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    try:
        # Load ECC keys
        private_key = load_private_key()
        public_key = load_public_key()

        # Derive shared key
        derived_key = derive_shared_key(private_key, public_key)

        # Load encrypted AES key
        with open("storage/keys/encrypted_aes_key.bin", "rb") as f:
            encrypted_aes_key = f.read()

        # Recover AES key
        aes_key = decrypt_aes_key(encrypted_aes_key, derived_key)

        # Decrypt file
        data = decrypt_file(nonce, tag, ciphertext, aes_key)

        # Save output
        with open("storage/decrypted.txt", "wb") as f:
            f.write(data)

        # 🔥 NEW: return content as text
        return {
            "message": "File decrypted successfully!",
            "content": data.decode(errors="ignore")
        }

    except Exception as e:
        return {
            "error": f"Decryption failed: {str(e)}"
        }