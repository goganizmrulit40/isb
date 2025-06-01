from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from file_operations import read_json, write_file


class AsymmetricEncryption:
    # читаем настройки из settings.json
    @staticmethod
    def load_settings(settings_path='settings.json'):
        settings = read_json(settings_path)
        return settings

    # генерируем пару ключей RSA и сохраняем их в файлы
    @staticmethod
    def generate_keys(private_key_path, public_key_path):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        public_key = private_key.public_key()

        print(type(private_key))
        print(private_key)
        print(type(public_key))
        print(public_key)

        write_file(
            private_key_path,
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL
            )
        )

        write_file(
            public_key_path,
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

        return private_key, public_key

    # шифруем симметричный ключ с использованием открытого ключа
    @staticmethod
    def encrypt(sym_key, public_key):
        encrypted_sym_key = public_key.encrypt(
            sym_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
            )
        )
        return encrypted_sym_key

    # расшифровываем симметричный ключ с использованием закрытого ключа
    @staticmethod
    def decrypt(encrypted_sym_key, private_key):
        decrypted_sym_key = private_key.decrypt(
            encrypted_sym_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
            )
        )
        return decrypted_sym_key
















