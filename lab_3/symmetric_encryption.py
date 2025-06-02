import os

import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from file_operations import OperationsFiles


class SymmetricEncryption:
    # генератор ключа
    @staticmethod
    def generator(key_length):
        if key_length not in range(40, 129):
            raise ValueError("Длина ключа должна быть от 40 до 128 бит с шагом 8 бит.")

        return secrets.token_bytes(key_length // 8)


    # зашифровка
    @staticmethod
    def encrypt(initial_text, key):
        init_vector = os.urandom(8)
        cipher = Cipher(algorithms.CAST5(key), modes.CBC(init_vector))
        encryptor = cipher.encryptor()

        transformation_text = OperationsFiles.read_bytes(initial_text)
        pad_length = 8 - (len(transformation_text) % 8)
        padded_plain_text = transformation_text + bytes([pad_length] * pad_length)

        cipher_text = encryptor.update(padded_plain_text) + encryptor.finalize()
        return init_vector + cipher_text


    # дешифровка
    @staticmethod
    def decrypt(init_vector_and_cipher_text, key):
        init_vector_and_cipher = OperationsFiles.read_bytes(init_vector_and_cipher_text)
        init_vector = init_vector_and_cipher[:8]
        cipher_text = init_vector_and_cipher[8:]

        cipher = Cipher(algorithms.CAST5(key), modes.CBC(init_vector))
        decryptor = cipher.decryptor()

        padded_plain_text = decryptor.update(cipher_text) + decryptor.finalize()

        pad_length = padded_plain_text[-1]
        return padded_plain_text[:-pad_length]

