import math
from scipy.special import gammainc
from constants import *


# Частотный побитовый тест
def frequency_test(bits):
    num_ones = sum(bits)
    num_zeros = len(bits) - num_ones
    s_n = (abs(num_ones - num_zeros) / math.sqrt(len(bits)))

    p_value = math.erfc(s_n / math.sqrt(2))

    return p_value


# Тест на одинаковые подряд идущие биты
def row_walking_frequency_test(bits):
    num_ones = sum(bits)
    share_ones = num_ones / len(bits)

    if (abs(share_ones - 0.5) >= (2 / math.sqrt(len(bits)))):
        return 0

    v_n = 0
    for i in range(1, len(bits)):
        if bits[i] == bits[i - 1]:
            v_n += 0
        else:
            v_n += 1

    numerator = abs(v_n - (2 * len(bits) * share_ones * (1 - share_ones)))
    denominator = 2 * math.sqrt(2 * len(bits)) * share_ones * (1 - share_ones)
    p_value = math.erfc(numerator / denominator)

    return p_value


# Ищем максимальную длину последовательности подряд идущих единиц в блоке
def max_consecutive_ones(block):
    max_length = 0
    current_length = 0

    for bit in block:
        if bit == 1:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0

    return max_length


# Анализируем последовательность битов и возвращаем статистику по блокам
def analyze_sequence(bits):
    block_size = 8
    num_blocks = len(bits) // block_size

    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0

    for i in range(num_blocks):
        block = bits[i * block_size:(i + 1) * block_size]
        max_length = max_consecutive_ones(block)

        if max_length <= 1:
            count_1 += 1
        elif max_length == 2:
            count_2 += 1
        elif max_length == 3:
            count_3 += 1
        elif max_length >= 4:
            count_4 += 1

    print(f"Количество блоков с максимальной длиной ≤ 1: {count_1}")
    print(f"Количество блоков с максимальной длиной = 2: {count_2}")
    print(f"Количество блоков с максимальной длиной = 3: {count_3}")
    print(f"Количество блоков с максимальной длиной ≥ 4: {count_4}")

    return count_1, count_2, count_3, count_4


# Вычисление хи-квадрата
def chi_square_test(observed_counts):
    p = [0.2148, 0.3672, 0.2305, 0.1875]

    chi2_stat = sum(((observed_counts[i] - 16 * p[i]) ** 2) / (16 * p[i]) for i in range(4))

    p_value = gammainc(1.5, chi2_stat / 2)

    return chi2_stat, p_value


def read_bits_from_file(filename):
    try:
        with open(filename, 'r') as file:
            line = file.readline().strip() # \n
            bits = [int(bit) for bit in line if bit in '01']
            return bits
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return None
    except Exception as e:
        print(f"Произошла ошибка при обработке файла '{filename}': {e}")
        return None


def write_results_to_file(filename, p_value_1, p_value_2, p_value_3, output_filename):
    try:
        with open(output_filename, "a") as file:
            file.write(f"{filename}: {p_value_1}\n")
            file.write(f"{filename}: {p_value_2}\n")
            file.write(f"{filename}: {p_value_3}\n\n")
        print("Результаты успешно записаны в файл.")
    except IOError as e:
        print(f"Ошибка при записи в файл: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def main():
    filenames = [FILE_ENTER_1, FILE_ENTER_2]

    for filename in filenames:
        bits = read_bits_from_file(filename)

        if bits is not None:
            if len(bits) == 128:
                p_value_1 = frequency_test(bits)
                result = p_value_1 > 0.01
                print(f"Результат частотного побитового теста для {filename}: {f"Пройден: {p_value_1}" if result else 'Не пройден'}")

                p_value_2 = row_walking_frequency_test(bits)
                result = p_value_2 > 0.01
                print(f"Результат теста на одинаковые подряд идущие биты для {filename}: {f"Пройден: {p_value_2}" if result else 'Не пройден'}")

                observed_counts = analyze_sequence(bits)
                print(f"Наблюдаемые значения: {observed_counts}")
                chi2_stat, p_value_3 = chi_square_test(observed_counts)

                print(f"Статистика хи-квадрат: {chi2_stat}")
                result = p_value_3 > 0.01
                print(f"Результат теста на самую длинную последовательность единиц в блоке для {filename}: {f"Пройден: {p_value_3}" if result else 'Не пройден'}")
                print("\n")

                write_results_to_file(filename, p_value_1, p_value_2, p_value_3, FILE_EXIT)


if __name__ == "__main__":
    main()