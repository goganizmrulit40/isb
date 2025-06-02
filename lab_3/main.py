from file_operations import OperationsFiles
from utils import generate_keys, encrypt_data, decrypt_data


def main():
    settings = OperationsFiles.read_json('settings.json')
    if not settings:
        return

    initial_file = settings["initial_file"]
    encrypted_file = settings["encrypted_file"]
    decrypted_file = settings["decrypted_file"]
    symmetric_key = settings["symmetric_key"]
    public_key = settings["public_key"]
    private_key = settings["private_key"]

    print("Проверка правильного считывания пути к файлам из файла настроек:")
    print(f"sym_key_path: {symmetric_key}, public_key_path: {public_key}, private_key_path: {private_key}")
    print(f"initial_file_path: {initial_file}, encrypted_file_path: {encrypted_file}, decrypted_file_path: {decrypted_file}\n")

    print("Выберите желаемое действие: \n1: генерация ключей гибридной системы\n2: шифрование данных гибридной системой")
    print("3: дешифрование данных гибридной системой\n0 - выход из программы (завершение её работы)")
    key = int(input())
    while key != 0:
        if key == 1:
            generate_keys(symmetric_key, public_key, private_key)
            key = int(input("Введите следующее желаемое действие: "))
            continue
        elif key == 2:
            encrypt_data(initial_file, private_key, symmetric_key, encrypted_file)
            key = int(input("Введите следующее желаемое действие: "))
            continue
        elif key == 3:
            decrypt_data(encrypted_file, private_key, symmetric_key, decrypted_file)
            key = int(input("Введите следующее желаемое действие: "))
            continue
        else:
            print("Вы ввели число не из возможного диапазона [0; 3]")
            key = int(input("Введите следующее желаемое действие: "))
    print("Работа программы завершена")


if __name__ == "__main__":
    main()
