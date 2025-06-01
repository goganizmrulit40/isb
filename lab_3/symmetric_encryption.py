import secrets


class SymmetricEncryption:
    def __init__(self, key_length):
        if key_length not in range(40, 129, 8):
            raise ValueError("Длина ключа должна быть от 40 до 128 бит с шагом 8 бит.")

        self.key = secrets.token_bytes(key_length // 8)
