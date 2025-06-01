import os

import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class SymmetricEncryption:
    @staticmethod
    def __init__(self, key_length):
        if key_length not in range(40, 129, 8):
            raise ValueError("Длина ключа должна быть от 40 до 128 бит с шагом 8 бит.")

        self.key = secrets.token_bytes(key_length // 8)


    @staticmethod
    def encrypt(self, inital_text):
        init_vector = os.urandom(8)
        cipher = Cipher(algorithms.CAST5(self.key), modes.CBC(init_vector))
        encryptor = cipher.encryptor()

        pad_length = 8 - (len(inital_text) % 8)
        padded_plaintext = inital_text + bytes([pad_length] * pad_length)

        ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
        return init_vector + ciphertext



