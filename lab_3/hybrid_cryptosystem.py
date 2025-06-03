from symmetric_encryption import SymmetricEncryption
from asymmetric_encryption import AsymmetricEncryption
from file_operations import OperationsFiles


class HybridCryptosystem:
    """Class for implementing a hybrid cryptosystem using both symmetric and asymmetric encryption."""

    @staticmethod
    def generate_keys(sym_key_path: str, public_key_path: str, private_key_path: str):
        """
        Generates keys for the hybrid cryptosystem.
        This method generates a symmetric key of required length and asymmetric key pair (public and private).
        The symmetric key is then encrypted using the public key and saved to a file.
        :param sym_key_path: Path to save the encrypted symmetric key.
        :param public_key_path: Path to save the generated public key.
        :param private_key_path: Path to save the generated private key.
        """
        key_length = int(input("Введите длину ключа. Длина ключа должна быть от 40 до 128 бит с шагом 8 бит.\n"))
        sym_key = SymmetricEncryption.generator(key_length)

        private_key, public_key = AsymmetricEncryption.generate_keys(private_key_path, public_key_path)

        encrypted_sym_key = AsymmetricEncryption.encrypt(sym_key, public_key)

        if encrypted_sym_key is not None:
            OperationsFiles.write_bytes(sym_key_path, encrypted_sym_key)
        else:
            print("Ошибка: зашифрованный симметричный ключ равен None.")


    @staticmethod
    def encrypt_data(initial_file_path: str, private_key_path: str, sym_key_path: str, encrypted_file_path: str):
        """
        Encrypts data using the hybrid cryptosystem.
        This method reads the private key and the encrypted symmetric key from files,
        decrypts the symmetric key using the private key,
        and then uses it to encrypt the data from the initial file.
        The resulting ciphertext is saved to a specified file.
        :param initial_file_path: Path to the initial file containing data to be encrypted.
        :param private_key_path: Path to the file containing the private key.
        :param sym_key_path: Path to the file containing the encrypted symmetric key.
        :param encrypted_file_path: Path to save the resulting encrypted data.
        """
        private_key = OperationsFiles.read_private_key(private_key_path)
        encrypted_sym_key = OperationsFiles.read_bytes(sym_key_path)

        sym_key = AsymmetricEncryption.decrypt(encrypted_sym_key, private_key)

        cipher_text = SymmetricEncryption.encrypt(initial_file_path, sym_key)

        OperationsFiles.write_bytes(encrypted_file_path, cipher_text)


    @staticmethod
    def decrypt_data(encrypted_file_path: str, private_key_path: str, sym_key_path: str, decrypted_file_path: str):
        """
        Decrypts data using the hybrid cryptosystem.
        This method reads the private key and the encrypted symmetric key from files,
        decrypts the symmetric key using the private key,
        and then uses it to decrypt the encrypted text from the specified encrypted file.
        The resulting text is saved to a specified file.
        :param encrypted_file_path: Path to the file containing data to be decrypted.
        :param private_key_path: Path to the file containing the private key.
        :param sym_key_path: Path to the file containing the encrypted symmetric key.
        :param decrypted_file_path: Path to save the resulting decrypted data.
        """
        private_key = OperationsFiles.read_private_key(private_key_path)
        encrypted_sym_key = OperationsFiles.read_bytes(sym_key_path)

        sym_key = AsymmetricEncryption.decrypt(encrypted_sym_key, private_key)

        decrypted_text = SymmetricEncryption.decrypt(encrypted_file_path, sym_key)
        OperationsFiles.write_bytes(decrypted_file_path, decrypted_text)

