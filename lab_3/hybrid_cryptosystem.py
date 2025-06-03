from symmetric_encryption import SymmetricEncryption
from asymmetric_encryption import AsymmetricEncryption
from file_operations import OperationsFiles


class HybridCryptosystem:
    # генерация ключей гибридной системы
    @staticmethod
    def generate_keys(sym_key_path: str, public_key_path: str, private_key_path: str):
        key_length = int(input("Введите длину ключа. Длина ключа должна быть от 40 до 128 бит с шагом 8 бит.\n"))
        sym_key = SymmetricEncryption.generator(key_length)

        private_key, public_key = AsymmetricEncryption.generate_keys(private_key_path, public_key_path)

        encrypted_sym_key = AsymmetricEncryption.encrypt(sym_key, public_key)

        if encrypted_sym_key is not None:
            OperationsFiles.write_bytes(sym_key_path, encrypted_sym_key)
        else:
            print("Ошибка: зашифрованный симметричный ключ равен None.")


    # шифрование данных гибридной системой
    @staticmethod
    def encrypt_data(initial_file_path: str, private_key_path: str, sym_key_path: str, encrypted_file_path: str):
        private_key = OperationsFiles.read_private_key(private_key_path)
        encrypted_sym_key = OperationsFiles.read_bytes(sym_key_path)

        sym_key = AsymmetricEncryption.decrypt(encrypted_sym_key, private_key)

        cipher_text = SymmetricEncryption.encrypt(initial_file_path, sym_key)

        OperationsFiles.write_bytes(encrypted_file_path, cipher_text)


    # дешифрование данных гибридной системой
    @staticmethod
    def decrypt_data(encrypted_file_path: str, private_key_path: str, sym_key_path: str, decrypted_file_path: str):
        private_key = OperationsFiles.read_private_key(private_key_path)
        encrypted_sym_key = OperationsFiles.read_bytes(sym_key_path)

        sym_key = AsymmetricEncryption.decrypt(encrypted_sym_key, private_key)

        decrypted_text = SymmetricEncryption.decrypt(encrypted_file_path, sym_key)
        OperationsFiles.write_bytes(decrypted_file_path, decrypted_text)

