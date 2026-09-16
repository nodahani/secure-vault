import crypto
import constants
from ui import (
    getting_input_user,
    get_user_lines,
    format_file_list,
    select_file,
    edit_lines_in_ui,
)
from file_manager import file_exist, save_encrypted_file, get_list_files


def create_file():
    user_input = getting_input_user("Enter file name, or type 'exit' to quit: ")

    if user_input != constants.EMPTY_INPUT:
        if user_input == constants.STATUS_BACK:
            return constants.STATUS_BACK
        elif user_input == constants.STATUS_EXIT:
            return constants.STATUS_EXIT
        else:
            file_status = file_exist(user_input)
            if file_status:
                return constants.DUPLICATE_NAME
            else:
                return save_encrypted_file(
                    user_input,
                    get_user_lines(
                        "You are writing to the file. Press Enter to finish and save, or type 'exit' to cancel: \n"
                    ),
                )
    else:
        return constants.EMPTY_INPUT


def display_file():
    """Display file titles and the content of the selected file."""

    result = ""
    pure_names = get_list_files()
    print(format_file_list(pure_names))

    selected = select_file(
        pure_names,
        "Which file do you want to see? Select by number, or type 'back' to return, or 'exit' to quit: ",
    )
    if selected == constants.STATUS_BACK:
        return constants.STATUS_BACK
    elif selected == constants.STATUS_EXIT:
        return constants.STATUS_EXIT
    elif selected == constants.EMPTY_INPUT:
        return constants.EMPTY_INPUT
    elif selected == constants.NOT_NUMBER:
        return constants.NOT_NUMBER
    elif selected == constants.INVALID_INPUT:
        return constants.INVALID_INPUT
    else:
        with open("./data/" + selected + ".txt", "r") as file:
            text = file.read()
            result += crypto.caesar_cipher(text, -constants.CIPHER_SHIFT)
        print(f"***\n{result}\n***")
        return constants.STATUS_OK


def edit_file():
    """Edit the file."""

    pure_names = get_list_files()
    print(format_file_list(pure_names))
    selected = select_file(
        pure_names,
        "Which file do you want to edit? Select by number, or type 'back' to return, or 'exit' to quit: ",
    )

    if selected == constants.STATUS_BACK:
        return constants.STATUS_BACK
    elif selected == constants.STATUS_EXIT:
        return constants.STATUS_EXIT
    elif selected == constants.EMPTY_INPUT:
        return constants.EMPTY_INPUT
    elif selected == constants.NOT_NUMBER:
        return constants.NOT_NUMBER
    elif selected == constants.INVALID_INPUT:
        return constants.INVALID_INPUT

    with open("./data/" + selected + ".txt", "r") as file:
        lines = crypto.caesar_cipher(file.read(), -constants.CIPHER_SHIFT).splitlines()
        result, status = edit_lines_in_ui(
            lines,
            'Type to edit, press Enter to continue, type "exit" to quit, and type "back" to go back:\n',
            "You have reached the end of the file. Do you want to continue writing? Type 'continue' or press Enter on a blank line to finish :\n",
            'Type, press Enter to Save, type "exit" to quit:\n',
        )
        if status == constants.STATUS_BACK:
            return constants.STATUS_BACK
        elif status == constants.STATUS_EXIT:
            return constants.STATUS_EXIT
        elif status == constants.STATUS_SAVE:
            text = "\n".join(result)
            with open("./data/" + selected + ".txt", "w") as file:
                file.write(crypto.caesar_cipher(text, constants.CIPHER_SHIFT))
                return constants.STATUS_SAVE


# def delete_file(file_name):
#     """Delete file.

#     Args:
#         file_name (str): The name of the file to delete.

#     Returns:
#         None
#     """

#     confirm = input(f"Delete {file_name}? (y/n): ")
#     if confirm.lower() != "y":
#         return False
#     else:
#         path = "./data/" + file_name + ".txt"
#         os.remove(path)
#         return True
