import json

# читаем из файла json
def read_json(file_path: str):
    with open(file_path) as json_file:
        return json.load(json_file)


# пишем в файл json
def write_json(file_path: str, data: dict):
    with open(file_path, 'w') as fp:
        json.dump(data, fp)


# читаем из файла
def read_file(file_path: str) -> bytes:
    with open(file_path, 'rb') as file:
        return file.read()


# пишем в файл
def write_file(file_path: str, data: bytes):
    with open(file_path, 'wb') as file:
        file.write(data)

