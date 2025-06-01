from symmetric_encryption import SymmetricEncryption
from asymmetric_encryption import AsymmetricEncryption
from file_operations import read_json, read_file, write_file, write_json


# генерация ключей гибридной системы
def generate_keys(sym_key_path, public_key_path, private_key_path):
    key_length = int(input("Введите длину ключа. Длина ключа должна быть от 40 до 128 бит с шагом 8 бит.\n"))
    sym_key = SymmetricEncryption(key_length)

    private_key, public_key = AsymmetricEncryption.generate_keys(private_key_path, public_key_path)

    encrypted_sym_key = AsymmetricEncryption.encrypt(sym_key, public_key)

    write_json(sym_key_path, encrypted_sym_key)


# шифрование данных гибридной системой
def encrypt_data(initial_file_path, private_key_path, sym_key_path, decrypted_file_path):
    settings = read_json('settings.json')
    if not settings:
        return

    private_key = read_file(private_key_path)
    encrypted_sym_key = read_file(sym_key_path)

    sym_key = AsymmetricEncryption.decrypt(encrypted_sym_key, private_key)

    cipher_text = SymmetricEncryption.encrypt(initial_file_path)

    write_file(decrypted_file_path, cipher_text)



