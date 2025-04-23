import math


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


def main():
    filenames = ['random_bits_cpp.txt', 'random_bits_java.txt']

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


if __name__ == "__main__":
    main()