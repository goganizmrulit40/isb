from collections import Counter

frequency_index = {
    ' ': 0.128675,
    'О': 0.096456,
    'И': 0.075312,
    'Е': 0.072292,
    'А': 0.064841,
    'Н': 0.061820,
    'Т': 0.061619,
    'С': 0.051953,
    'Р': 0.040677,
    'В': 0.039267,
    'М': 0.029803,
    'Л': 0.029400,
    'Д': 0.026983,
    'Я': 0.026379,
    'К': 0.025977,
    'П': 0.024768,
    'З': 0.015908,
    'Ы': 0.015707,
    'Ь': 0.015103,
    'У': 0.013290,
    'Ч': 0.011679,
    'Ж': 0.010673,
    'Г': 0.009867,
    'Х': 0.008659,
    'Ф': 0.007249,
    'Й': 0.006847,
    'Ю': 0.006847,
    'Б': 0.006645,
    'Ц': 0.005034,
    'Ш': 0.004229,
    'Щ': 0.003625,
    'Э': 0.002416,
    'Ъ': 0.000000
}

replacement_dict = {
    "Z": "А",
    "G": "Б",
    "у": "В",
    "3": "Г",
    "Х": "Е",
    "F": "З",
    "Y": "Л",
    "U": "М",
    "г": "Н",
    "%": "О",
    "7": "П",
    "=": "С",
    "1": "У",
    "R": "Ф",
    "i": "Щ",
    "N": "Ч",
    "s": "Ц",
    "J": "Ш",
    "9": "Ъ",
    "ю": "Ю",
    "@": "Ы",
    "<": "Ь"
}

def Code_to_a_single_alphabet(text):
    for old_char, new_char in replacement_dict.items():
        text = text.replace(old_char, new_char)

    return text

replacement_dict_2 = {
    "А": " ",
    "Т": "с",
    "Б": "о",
    "В": "и",
    "Г": "е",
    "З": "а",
    "Щ": "з",
    "М": "п",
    "Ф": "д",
    "Д": "н",
    "Я": "к",
    "Ъ": "ц",
    "П": "л",
    "У": "я",
    "Е": "т",
    "Л": "р",
    "О": "б",
    "Ё": "ч",
    "С": "ы",
    "Н": "в",
    "Ч": "м",
    "Ю": "ж",
    "И": "у",
    "К": "щ",
    "Ш": "х",
    "Ц": "ь",
    "Р": "ю",
    "Й": "г",
    "Ь": "э",
    "Ж": "й",
    "Ы": "ф"

}

def replace_text(text):
    for old_char, new_char in replacement_dict_2.items():
        text = text.replace(old_char, new_char)

    return text

replacement_dict_3 = {
    "Z": " ",
    "Т": "с",
    "G": "о",
    "у": "и",
    "3": "е",
    "F": "а",
    "i": "з",
    "U": "п",
    "R": "д",
    "Д": "н",
    "Я": "к",
    "9": "ц",
    "7": "л",
    "1": "я",
    "Х": "т",
    "Y": "р",
    "%": "б",
    "Ё": "ч",
    "=": "ы",
    "г": "в",
    "N": "м",
    "ю": "ж",
    "И": "у",
    "К": "щ",
    "J": "х",
    "s": "ь",
    "Р": "ю",
    "Й": "г",
    "<": "э",
    "Ж": "й",
    "@": "ф"
}

def main():
    with open('cod23.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    print(text)

    text = Code_to_a_single_alphabet(text)
    print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    print(text)

    print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    frequency = Counter(text)

    total_chars = sum(frequency.values())
    frequency_index_cipher = {char: count / total_chars for char, count in frequency.items()}

    sorted_frequency_cipher_index = dict(sorted(frequency_index_cipher.items(), key=lambda item: item[1], reverse=True))

    print("Индекс частоты появления букв:")
    for char, freq in sorted_frequency_cipher_index.items():
        print(f"Символ: '{char}', Частота: {freq:.6f}")

    print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    text = replace_text(text)

    print(text)
    print("\n")

    with open('res.txt', 'w', encoding='utf-8') as file:
        file.write(text)

    with open('replacement_dict.txt', 'w', encoding='utf-8') as f:
        for key, value in replacement_dict_3.items():
            f.write(f"{key}: {value}\n")

if __name__ == "__main__":
    main()
''