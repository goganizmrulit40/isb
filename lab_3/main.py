from symmetric_encryption import SymmetricEncryption
from file_operations import read_json, read_file, write_file

def main():
    settings = read_json('settings.json')
    if not settings:
        return

    initial_file = settings.get("initial_file")
    encrypted_file = settings.get("encrypted_file")
    decrypted_file = settings.get("decrypted_file")

    initial_text = read_file(initial_file)
    if initial_text is None:
        return

    key_length = int(input("Введите длину ключа. Длина ключа должна быть от 40 до 128 бит с шагом 8 бит.\n"))
    encryption = SymmetricEncryption(key_length)

    encrypted_data = encryption.encrypt(initial_text)
    print("Зашифрованные данные:\n", encrypted_data)

    write_file(encrypted_file, encrypted_data)

    decrypted_data = encryption.decrypt(encrypted_data)
    print("Расшифрованные данные:\n", decrypted_data.decode('utf-8'))

    write_file(decrypted_file, decrypted_data)

    if initial_text == decrypted_data:
        print("Шифрование и расшифровка прошли успешно")
    else:
        print("Ошибка: расшифрованные данные не совпадают с исходными")

if __name__ == "__main__":
    main()
