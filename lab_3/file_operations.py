import json
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


class OperationsFiles:
    # читаем из файла json
    @staticmethod
    def read_json(file_path: str) -> dict:
        try:
            with open(file_path, 'r', encoding='utf-8') as json_file:
                print(f"Файл {file_path} успешно прочитан.")
                return json.load(json_file)
        except FileNotFoundError:
            print(f"Файл {file_path} не найден.")
        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON в файле {file_path}.")
        except Exception as e:
            print(f"Произошла ошибка при чтении файла {file_path}: {e}")


    # пишем в файл json
    @staticmethod
    def write_json(file_path: str, data: dict):
        try:
            with open(file_path, 'w') as fp:
                print(f"В файл {file_path} успешно записана информация.")
                json.dump(data, fp)
        except IOError:
            print(f"Ошибка записи в файл {file_path}")
        except Exception as e:
            print(f"Произошла ошибка при записи в файл {file_path}: {e}")


    # читаем из файла
    @staticmethod
    def read_file(file_path: str) -> bytes:
        try:
            with open(file_path, 'rb', encoding='utf-8') as file:
                print(f"Файл {file_path} успешно прочитан.")
                return file.read()
        except FileNotFoundError:
            print(f"Файл {file_path} не найден.")
        except IOError:
            print(f"Ошибка чтения файла {file_path}")
        except Exception as e:
            print(f"Произошла ошибка при чтении файла {file_path}: {e}")


    # пишем в файл
    @staticmethod
    def write_file(file_path: str, data: bytes):
        try:
            with open(file_path, 'wb', encoding='utf-8') as file:
                print(f"В файл {file_path} успешно записана информация.")
                file.write(data)
        except IOError:
            print(f"Ошибка записи в файл {file_path}")
        except Exception as e:
            print(f"Произошла ошибка при записи в файл {file_path}: {e}")


    # читаем байты из файла
    @staticmethod
    def read_bytes(file_path: str) -> bytes:
        try:
            with open(file_path, 'rb') as file:
                print(f"Файл {file_path} успешно прочитан.")
                return file.read()
        except FileNotFoundError:
            print(f"Файл {file_path} не найден.")
        except IOError:
            print(f"Ошибка чтения файла {file_path}")
        except Exception as e:
            print(f"Произошла ошибка при чтении файла {file_path}: {e}")


    # пишем байты в файл
    @staticmethod
    def write_bytes(file_path: str, data: bytes):
        try:
            with open(file_path, 'wb') as file:
                print(f"В файл {file_path} успешно записана информация.")
                file.write(data)
        except IOError:
            print(f"Ошибка записи в файл {file_path}")
        except Exception as e:
            print(f"Произошла ошибка при записи в файл {file_path}: {e}")


    # читаем приватный ключ из файла
    @staticmethod
    def read_private_key(file_path: str) -> rsa.RSAPrivateKey:
        try:
            with open(file_path, 'rb') as key_file:
                private_key = serialization.load_pem_private_key(
                    key_file.read(),
                    password=None
                )
                print(f"Приватный ключ успешно прочитан из {file_path}.")
                return private_key
        except FileNotFoundError:
            print(f"Файл {file_path} не найден.")
        except ValueError:
            print(f"Ошибка декодирования приватного ключа в файле {file_path}.")
        except Exception as e:
            print(f"Произошла ошибка при чтении приватного ключа из файла {file_path}: {e}")


    # пишем приватный ключ в файл
    @staticmethod
    def write_private_key(file_path: str, private_key: rsa.RSAPrivateKey):
        try:
            with open(file_path, 'wb') as key_file:
                key_file.write(
                    private_key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                        encryption_algorithm=serialization.NoEncryption()  # Здесь можно указать шифрование
                    )
                )
                print(f"Приватный ключ успешно записан в {file_path}.")
        except IOError:
            print(f"Ошибка записи в файл {file_path}.")
        except Exception as e:
            print(f"Произошла ошибка при записи приватного ключа в файл {file_path}: {e}")


    # читаем публичный ключ из файла
    @staticmethod
    def read_public_key(file_path: str) -> rsa.RSAPublicKey:
        try:
            with open(file_path, 'rb') as key_file:
                public_key = serialization.load_pem_public_key(key_file.read())
                print(f"Публичный ключ успешно прочитан из {file_path}.")
                return public_key
        except FileNotFoundError:
            print(f"Файл {file_path} не найден.")
        except ValueError:
            print(f"Ошибка декодирования публичного ключа в файле {file_path}.")
        except Exception as e:
            print(f"Произошла ошибка при чтении публичного ключа из файла {file_path}: {e}")


    # пишем публичный ключ в файл
    @staticmethod
    def write_public_key(file_path: str, public_key: rsa.RSAPublicKey):
        try:
            with open(file_path, 'wb') as key_file:
                key_file.write(
                    public_key.public_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PublicFormat.SubjectPublicKeyInfo
                    )
                )
                print(f"Публичный ключ успешно записан в {file_path}.")
        except IOError:
            print(f"Ошибка записи в файл {file_path}.")
        except Exception as e:
            print(f"Произошла ошибка при записи публичного ключа в файл {file_path}: {e}")



