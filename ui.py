import constants
from file_manager import get_list_files


def get_user_lines(message):
    """Accepting and returning multi-line input"""

    text = []
    status = constants.STATUS_SAVE
    while True:
        user_input = input(message)
        if user_input == constants.STATUS_EXIT:
            return [], constants.STATUS_EXIT
        elif user_input == "":
            break
        else:
            text.append(user_input)

    return text, status


def getting_input_user(message):
    """Prompt the user and return their input.

    Returns a status constant if user types 'back' or 'exit'."""
    user_input = input(message)
    if user_input == constants.STATUS_BACK:
        return constants.STATUS_BACK
    elif user_input == constants.STATUS_EXIT:
        return constants.STATUS_EXIT
    else:
        return user_input


def format_file_list(files):
    """Return a numbered list of files as a single string."""
    return "\n".join(f"{i}. {f}" for i, f in enumerate(files, start=1))


def select_file(pure_names, message):
    """It takes a list of raw filenames and a number from the user, and returns the raw name of the corresponding file."""

    user_input = getting_input_user(message)

    if user_input == constants.STATUS_BACK:
        return constants.STATUS_BACK
    elif user_input == constants.STATUS_EXIT:
        return constants.STATUS_EXIT
    elif user_input == constants.EMPTY_INPUT:
        return constants.EMPTY_INPUT
    else:
        try:
            index = int(user_input)
        except ValueError:
            return constants.NOT_NUMBER

        if index < 1 or index > len(pure_names):
            return constants.INVALID_INPUT

    return pure_names[index - 1]


def edit_lines_in_ui(lines, message, message_want_continue, message_continue):
    """Edit import file lines"""
    edit_lines = []
    for line in lines:
        print(line)
        user_input = input(message)
        if user_input == constants.STATUS_BACK:
            return [], constants.STATUS_BACK
        elif user_input == constants.STATUS_EXIT:
            return [], constants.STATUS_EXIT
        elif user_input != "":
            edit_lines.append(user_input)
        else:
            edit_lines.append(line)

    user_input = input(message_want_continue)
    if user_input == constants.CONTINUE:
        list_lines, status = get_user_lines(message_continue)
        if status == constants.STATUS_BACK:
            return [], constants.STATUS_BACK
        elif status == constants.STATUS_EXIT:
            return [], constants.STATUS_EXIT
        elif status != "":
            edit_lines.extend(list_lines)
        else:
            return edit_lines, constants.STATUS_SAVE
    return edit_lines, constants.STATUS_SAVE
