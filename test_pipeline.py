from routes.upload import encrypt_and_store
from routes.download import decrypt_and_load

# Step 1: Encrypt
encrypt_and_store("test_files/test.txt")

# Step 2: Decrypt
decrypt_and_load()