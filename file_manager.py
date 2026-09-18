import os
import crypto
import constants


def file_exist(stem):
    name_decrypt = crypto.caesar_cipher(stem, -constants.CIPHER_SHIFT)
    if name_decrypt + ".txt" in os.listdir("./data"):
        return True
    else:
        return False


def get_list_files():
    """Get list of files"""

    file_names = os.listdir("data")
    pure_names = []
    for file_name in file_names:
        name_decrypt = crypto.caesar_cipher(file_name, -constants.CIPHER_SHIFT)
        if file_name.endswith(".txt"):
            pure_names.append(name_decrypt[:-4])
    return pure_names


def save_encrypted_file(stem, input_result):
    """Writing encrypted text to a file"""

    name_encrypt = crypto.caesar_cipher(stem, constants.CIPHER_SHIFT)
    lines, status = input_result
    if status == constants.STATUS_SAVE:
        with open("./data/" + name_encrypt + ".txt", "w") as file:
            text = "\n".join(lines)
            file.write(crypto.caesar_cipher(text, constants.CIPHER_SHIFT))
            return status
    else:
        return status
