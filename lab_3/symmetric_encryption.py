import os

import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class SymmetricEncryption:
    # конструктор
    def __init__(self, key_length):
        if key_length not in range(40, 129):
            raise ValueError("Длина ключа должна быть от 40 до 128 бит с шагом 8 бит.")

        self.key = secrets.token_bytes(key_length // 8)


    # зашифровка
    def encrypt(self, inital_text, key):
        init_vector = os.urandom(8)
        cipher = Cipher(algorithms.CAST5(key), modes.CBC(init_vector))
        encryptor = cipher.encryptor()

        pad_length = 8 - (len(inital_text) % 8)
        padded_plain_text = inital_text + bytes([pad_length] * pad_length)

        cipher_text = encryptor.update(padded_plain_text) + encryptor.finalize()
        return init_vector + cipher_text


    # дешифровка
    def decrypt(self, init_vector_and_cipher_text, key):
        init_vector = init_vector_and_cipher_text[:8]
        cipher_text = init_vector_and_cipher_text[8:]

        cipher = Cipher(algorithms.CAST5(key), modes.CBC(init_vector))
        decryptor = cipher.decryptor()

        padded_plain_text = decryptor.update(cipher_text) + decryptor.finalize()

        pad_length = padded_plain_text[-1]
        return padded_plain_text[:-pad_length]

