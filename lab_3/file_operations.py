import json
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


class OperationsFiles:
    """Class for performing file operations."""

    @staticmethod
    def read_json(file_path: str) -> dict:
        """
        Reads a json file and returns its contents as a dictionary.
        :param file_path: Path to the json file.
        :return: Json data as a dictionary.
        """
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


    @staticmethod
    def write_json(file_path: str, data: dict):
        """
        Writes a dictionary to a json file.
        :param file_path: Path to the json file where data will be written.
        :param data: The dictionary we write to the file.
        """
        try:
            with open(file_path, 'w') as fp:
                print(f"В файл {file_path} успешно записана информация.")
                json.dump(data, fp)
        except IOError:
            print(f"Ошибка записи в файл {file_path}")
        except Exception as e:
            print(f"Произошла ошибка при записи в файл {file_path}: {e}")


    @staticmethod
    def read_bytes(file_path: str) -> bytes:
        """
        Reads the contents of a file in binary mode.
        :param file_path: Path to the file.
        :return: Contents of the file as bytes.
        """
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


    @staticmethod
    def write_bytes(file_path: str, data: bytes):
        """
        Writes bytes to a file.
        :param file_path: Path to the file where data will be written.
        :param data: Data to write in bytes.
        """
        try:
            with open(file_path, 'wb') as file:
                print(f"В файл {file_path} успешно записана информация.")
                file.write(data)
        except IOError:
            print(f"Ошибка записи в файл {file_path}")
        except Exception as e:
            print(f"Произошла ошибка при записи в файл {file_path}: {e}")


    @staticmethod
    def read_private_key(file_path: str) -> rsa.RSAPrivateKey:
        """
        Reads a private key from a file.
        :param file_path: Path to the file containing the private key.
        :return: The private key as an RSAPrivateKey object.
        """
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


    @staticmethod
    def write_private_key(file_path: str, private_key: rsa.RSAPrivateKey):
        """
        Writes a private key to a file.
        :param file_path: Path to the file where the private key will be written.
        :param private_key: The private key to write as an RSAPrivateKey object.
        """
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


    @staticmethod
    def read_public_key(file_path: str) -> rsa.RSAPublicKey:
        """
        Reads a public key from a file.
        :param file_path: Path to the file containing the public key.
        :return: The public key as an RSAPublicKey object.
        """
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


    @staticmethod
    def write_public_key(file_path: str, public_key: rsa.RSAPublicKey):
        """
        Writes a public key to a file.
        :param file_path: Path to the file where the public key will be written.
        :param public_key: The public key to write as an RSAPublicKey object.
        """
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



