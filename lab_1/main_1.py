from collections import Counter
from constants import *


def replace_text(text, const):
    for old_char, new_char in const.items():
        text = text.replace(old_char, new_char)

    return text


def read_from_file():
    with open(FILE_ENTER, 'r', encoding='utf-8') as file:
        return file.read()


def processing_frequency(text):
    frequency = Counter(text)

    total_chars = sum(frequency.values())
    if total_chars == 0:
        print("Ошибка: текст пуст, невозможно вычислить частоту.")
        return

    frequency_index_cipher = {char: count / total_chars for char, count in frequency.items()}
    sorted_frequency_cipher_index = dict(sorted(frequency_index_cipher.items(), key=lambda item: item[1], reverse=True))

    print("Индекс частоты появления букв:")
    for char, freq in sorted_frequency_cipher_index.items():
        print(f"Символ: '{char}', Частота: {freq:.6f}")


def write_to_files(text):
    with open(FILE_EXIT, 'w', encoding='utf-8') as file:
        file.write(text)


def main():
    try:
        text = read_from_file()

        print(text)

        text = replace_text(text, REPLACEMENT_DICT)
        print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        print(text)

        print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

        processing_frequency(text)

        print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        text = replace_text(text, REPLACEMENT_DICT_TWO)

        print(text)
        print("\n")

        write_to_files(text)

    except FileNotFoundError:
        print(f"Ошибка: Файл не найден.")
        return
    except IOError as e:
        print(f"Ошибка при работе с файлом: {e}")
        return

if __name__ == "__main__":
    main()
