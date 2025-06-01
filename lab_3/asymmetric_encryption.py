from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
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