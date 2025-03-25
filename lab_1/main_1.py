from collections import Counter
from constants import *

def replace_text(text, const):
    for old_char, new_char in const.items():
        text = text.replace(old_char, new_char)

    return text

def frequency_count (frequency, total_chars):
    frequency_index_cipher = {char: count / total_chars for char, count in frequency.items()}
    sorted_frequency_cipher_index = dict(sorted(frequency_index_cipher.items(), key=lambda item: item[1], reverse=True))

    return sorted_frequency_cipher_index

def read_from_file():
    try:
        with open(FILE_ENTER, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{FILE_ENTER}' не найден.")
        return
    except IOError as e: #ошибки ввода-вывода
        print(f"Ошибка при чтении файла '{FILE_ENTER}': {e}")
        return

def write_to_files(text):
    try:
        with open(FILE_EXIT, 'w', encoding='utf-8') as file:
            file.write(text)
    except IOError as e:
        print(f"Ошибка при записи в файл '{FILE_EXIT}': {e}")
        return

    try:
        with open(FILE_DICT, 'w', encoding='utf-8') as f:
            for key, value in REPLACEMENT_DICT_RES.items():
                f.write(f"{key}: {value}\n")
    except IOError as e:
        print(f"Ошибка при записи в файл '{FILE_DICT}': {e}")
        return

def main():
    text = read_from_file()

    print(text)

    text = replace_text(text, REPLACEMENT_DICT)
    print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    print(text)

    print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    frequency = Counter(text)

    total_chars = sum(frequency.values())
    if total_chars == 0:
        print("Ошибка: текст пуст, невозможно вычислить частоту.")
        return

    sorted_frequency_cipher_index = frequency_count(frequency, total_chars)

    print("Индекс частоты появления букв:")
    for char, freq in sorted_frequency_cipher_index.items():
        print(f"Символ: '{char}', Частота: {freq:.6f}")

    print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    text = replace_text(text, REPLACEMENT_DICT_TWO)

    print(text)
    print("\n")

    write_to_files(text)

if __name__ == "__main__":
    main()
