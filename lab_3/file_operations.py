import json

# читаем из файла json
def read_json(file_path: str):
    try:
        with open(file_path) as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле {file_path}.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла {file_path}: {e}")

# пишем в файл json
def write_json(file_path: str, data: dict):
    try:
        with open(file_path, 'w') as fp:
            json.dump(data, fp)
    except IOError:
        print(f"Ошибка записи в файл {file_path}")
    except Exception as e:
        print(f"Произошла ошибка при записи в файл {file_path}: {e}")

# читаем из файла
def read_file(file_path: str) -> bytes:
    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except IOError:
        print(f"Ошибка чтения файла {file_path}")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла {file_path}: {e}")

# пишем в файл
def write_file(file_path: str, data: bytes):
    try:
        with open(file_path, 'wb') as file:
            file.write(data)
    except IOError:
        print(f"Ошибка записи в файл {file_path}")
    except Exception as e:
        print(f"Произошла ошибка при записи в файл {file_path}: {e}")


