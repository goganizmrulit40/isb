import math


# Частотный побитовый тест
def frequency_test(bits):
    num_ones = sum(bits)
    num_zeros = len(bits) - num_ones
    s_n = (abs(num_ones - num_zeros) / math.sqrt(len(bits)))

    p_value = math.erfc(s_n / math.sqrt(2))

    return p_value > 0.01


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

    numerator = abs(v_n - (2 * len(bits) * share_ones * (share_ones - 1)))
    denominator = 2 * math.sqrt(2 * len(bits)) * share_ones * (share_ones - 1)
    p_value = math.erfc(numerator / denominator)

    return p_value


def main():
    filenames = ['random_bits_cpp.txt', 'random_bits_java.txt']

    for filename in filenames:
        try:
            with open(filename, 'r') as file:
                line = file.readline().strip() # \n
                bits = [int(bit) for bit in line if bit in '01']

            result = frequency_test(bits)

            print(f"Результат частотного побитового теста для {filename}: {'Пройден' if result else 'Не пройден'}")

        except FileNotFoundError:
            print(f"Файл '{filename}' не найден.")
        except Exception as e:
            print(f"Произошла ошибка при обработке файла '{filename}': {e}")


if __name__ == "__main__":
    main()