from symmetric_encryption import SymmetricEncryption
from asymmetric_encryption import AsymmetricEncryption
from file_operations import read_json, read_file, write_file


def generate_keys(sym_key_path, public_key_path, private_key_path):
    key_length = int(input("Введите длину ключа. Длина ключа должна быть от 40 до 128 бит с шагом 8 бит.\n"))
    sym_key = SymmetricEncryption(key_length)

    private_key, public_key = AsymmetricEncryption.generate_keys(private_key_path, public_key_path)

    encrypted_sym_key = AsymmetricEncryption.encrypt(sym_key, public_key)

    settings = read_json('settings.json')
    if not settings:
        return

    symmetric_key_file = settings.get("symmetric_key")

    write_file(symmetric_key_file, encrypted_sym_key)
