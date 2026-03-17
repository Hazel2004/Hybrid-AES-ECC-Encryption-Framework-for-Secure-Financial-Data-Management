from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Generate AES-256 key
def generate_aes_key():
    return get_random_bytes(32)


# Encrypt file data
def encrypt_file(data, key):
    cipher = AES.new(key, AES.MODE_EAX)

    ciphertext, tag = cipher.encrypt_and_digest(data)

    return {
        "nonce": cipher.nonce,
        "tag": tag,
        "ciphertext": ciphertext
    }


# Decrypt file data
def decrypt_file(nonce, tag, ciphertext, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    data = cipher.decrypt_and_verify(ciphertext, tag)

    return data