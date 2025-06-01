import os

import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class SymmetricEncryption:
    # конструктор
    def __init__(self, key_length):
        if key_length not in range(40, 129, 8):
            raise ValueError("Длина ключа должна быть от 40 до 128 бит с шагом 8 бит.")

        self.key = secrets.token_bytes(key_length // 8)


    # зашифровка
    def encrypt(self, inital_text):
        init_vector = os.urandom(8)
        cipher = Cipher(algorithms.CAST5(self.key), modes.CBC(init_vector))
        encryptor = cipher.encryptor()

        pad_length = 8 - (len(inital_text) % 8)
        padded_plaintext = inital_text + bytes([pad_length] * pad_length)

        ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
        return init_vector + ciphertext


    # дешифровка
    def decrypt(self, init_vector_and_ciphertext):
        init_vector = init_vector_and_ciphertext[:8]
        ciphertext = init_vector_and_ciphertext[8:]

        cipher = Cipher(algorithms.CAST5(self.key), modes.CBC(init_vector))
        decryptor = cipher.decryptor()

        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

        pad_length = padded_plaintext[-1]
        return padded_plaintext[:-pad_length]

