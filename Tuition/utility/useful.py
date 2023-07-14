from cryptography.fernet import Fernet
from django.conf import settings

secret_key = settings.SECRET_KEY.encode('utf-8')

def encrypt_string(input_string):
    # Create a Fernet cipher object with the secret key
    cipher = Fernet(secret_key)

    # Encode the input string to bytes
    input_bytes = input_string.encode()

    # Encrypt the input bytes
    encrypted_bytes = cipher.encrypt(input_bytes)

    # Convert the encrypted bytes to a string representation
    encrypted_string = encrypted_bytes.decode()
    print(encrypted_string)
    return encrypted_string

def decrypt_string(encrypted_string):
    # Create a Fernet cipher object with the secret key
    cipher = Fernet(secret_key)

    # Convert the encrypted string to bytes
    encrypted_bytes = encrypted_string.encode()

    # Decrypt the encrypted bytes
    decrypted_bytes = cipher.decrypt(encrypted_bytes)

    # Convert the decrypted bytes to a string
    decrypted_string = decrypted_bytes.decode()
    print("real val==========",decrypted_string)
    return decrypted_string


def usefulPrint():
    print(secret_key)