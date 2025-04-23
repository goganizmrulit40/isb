import math


#Проверка частоты побитового теста
def frequency_test(bits):
    num_ones = sum(bits)
    num_zeros = len(bits) - num_ones
    s_n = (abs(num_ones - num_zeros) / math.sqrt(len(bits)))

    p_value = math.erfc(s_n / math.sqrt(2))

    return p_value > 0.01


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