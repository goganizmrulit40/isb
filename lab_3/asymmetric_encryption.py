from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from file_operations import OperationsFiles


class AsymmetricEncryption:
    """Class for asymmetric encryption using the RSA algorithm."""

    @staticmethod
    def load_settings(settings_path='settings.json'):
        """
        Loads settings from a json file.
        :param settings_path: Path to the settings JSON file.
        :return: Settings as a dictionary.
        """
        settings = OperationsFiles.read_json(settings_path)
        return settings


    @staticmethod
    def generate_keys(private_key_path, public_key_path):
        """
        Generates an RSA key pair and saves them to specified files.
        :param private_key_path: File path to save the private key.
        :param public_key_path: File path to save the public key.
        :return: The generated private and public keys.
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        public_key = private_key.public_key()

        print(type(private_key))
        print(private_key)
        print(type(public_key))
        print(public_key)

        OperationsFiles.write_bytes(
            private_key_path,
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

        OperationsFiles.write_bytes(
            public_key_path,
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

        return private_key, public_key


    @staticmethod
    def encrypt(sym_key, public_key):
        """
        The symmetrical key is encrypted using an open key.
        :param sym_key: The symmetric key used for encrypt.
        :param public_key: The public key used for encryption.
        :return: Encrypted symmetric key.
        """
        encrypted_sym_key = public_key.encrypt(
            sym_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_sym_key


    @staticmethod
    def decrypt(encrypted_sym_key, private_key):
        """
        Decrypts an encrypted symmetric key using the private key.
        :param encrypted_sym_key: The encrypted symmetric key used for decrypt.
        :param private_key: The private key used for decryption.
        :return: Decrypted symmetric key.
        """
        decrypted_sym_key = private_key.decrypt(
            encrypted_sym_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_sym_key

