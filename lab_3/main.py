from file_operations import OperationsFiles
from utils import generate_keys, encrypt_data, decrypt_data


def main():
    settings = OperationsFiles.read_json('settings.json')
    if not settings:
        return

    initial_file = settings["initial_file"]
    encrypted_file = settings["encrypted_file"]
    decrypted_file = settings["decrypted_file"]
    symmetric_key = settings["symmetric_key"]
    public_key = settings["public_key"]
    private_key = settings["private_key"]

    print(f"sym_key_path: {symmetric_key}, public_key_path: {public_key}, private_key_path: {private_key}")
    generate_keys(symmetric_key, public_key, private_key)

    print(f"initial_file_path: {initial_file}")
    encrypt_data(initial_file, private_key, symmetric_key, encrypted_file)

    print(f"encrypted_file_path: {encrypted_file}, decrypted_file_path: {decrypted_file}")
    decrypt_data(encrypted_file, private_key, symmetric_key, decrypted_file)


if __name__ == "__main__":
    main()
