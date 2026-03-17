from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF


# Generate ECC key pair
def generate_keys():
    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()
    return private_key, public_key


# Save keys to files
import os

def save_keys(private_key, public_key):

    os.makedirs("keys", exist_ok=True)  # 🔥 ensures folder exists

    with open("keys/private_key.pem", "wb") as f:
        f.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    with open("keys/public_key.pem", "wb") as f:
        f.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

# Load keys from files
def load_private_key():
    with open("keys/private_key.pem", "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None)


def load_public_key():
    with open("keys/public_key.pem", "rb") as f:
        return serialization.load_pem_public_key(f.read())


# Generate shared key using ECDH
def derive_shared_key(private_key, public_key):
    shared_key = private_key.exchange(ec.ECDH(), public_key)

    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data'
    ).derive(shared_key)

    return derived_key


# Encrypt AES key using XOR (simple approach)
def encrypt_aes_key(aes_key, derived_key):
    return bytes(a ^ b for a, b in zip(aes_key, derived_key))


# Decrypt AES key
def decrypt_aes_key(encrypted_key, derived_key):
    return bytes(a ^ b for a, b in zip(encrypted_key, derived_key))