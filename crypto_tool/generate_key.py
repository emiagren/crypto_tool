"""
Generate secret key
"""

from cryptography.fernet import Fernet

def generate_secret_key(filename="secret.key"):
    """Generates a secret key and saves it to a file."""
    secret_key = Fernet.generate_key()  # Generating encryption key
    with open(filename, 'wb') as key_file:
        key_file.write(secret_key)  # Save the key to file
    print(f"Secret key saved to {filename}")
    print(f"Krypterad text: {secret_key}")

if __name__ == "__main__":
    generate_secret_key()