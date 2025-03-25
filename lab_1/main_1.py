from collections import Counter
from constants import *

def replace_text(text, const):
    for old_char, new_char in const.items():
        text = text.replace(old_char, new_char)

    return text

def main():
    try:
        with open(FILE_ENTER, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{FILE_ENTER}' не найден.")
        return
    except IOError as e: #ошибки ввода-вывода
        print(f"Ошибка при чтении файла '{FILE_ENTER}': {e}")
        return

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

    frequency_index_cipher = {char: count / total_chars for char, count in frequency.items()}

    sorted_frequency_cipher_index = dict(sorted(frequency_index_cipher.items(), key=lambda item: item[1], reverse=True))

    print("Индекс частоты появления букв:")
    for char, freq in sorted_frequency_cipher_index.items():
        print(f"Символ: '{char}', Частота: {freq:.6f}")

    print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    text = replace_text(text, REPLACEMENT_DICT_TWO)

    print(text)
    print("\n")

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

if __name__ == "__main__":
    main()
