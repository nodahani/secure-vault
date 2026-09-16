from app import create_file, display_file, edit_file
import constants

# UI
while True:
    print("1. Create New File")
    print("2. View Files")
    print("3. Edit File")
    # print("4. Delete File")
    print("5. Exit")

    choise = input("What do you want to do...? ")

    # Create file
    if choise == "1":
        status = create_file()
        if status == constants.STATUS_SAVE:
            print("** file saved successfully. **")
        elif status == constants.DUPLICATE_NAME:
            print("** This name already exists. **")
        elif status == constants.STATUS_BACK:
            print("** You have returned to the previous menu. **")
        elif status == constants.STATUS_EXIT:
            print("** You are out. **")
            break
        elif status == constants.EMPTY_INPUT:
            print("** You cannot leave the input blank! **")
        else:
            print(f"** Unexpected status: {status} **")

    # Display files
    elif choise == "2":
        status = display_file()
        if status == constants.STATUS_OK:
            pass
        elif status == constants.STATUS_BACK:
            print("** You have returned to the previous menu. **")
        elif status == constants.STATUS_EXIT:
            print("** You are out. **")
            break
        elif status == constants.EMPTY_INPUT:
            print("** You cannot leave the input blank! **")
        elif status == constants.NOT_NUMBER:
            print("** Please enter a valid number. **")
        elif status == constants.INVALID_INPUT:
            print("** Your choice is not in the list **")

    # Edit file
    elif choise == "3":
        status = edit_file()
        if status == constants.STATUS_SAVE:
            print("** The file was successfully edited. **")
        elif status == constants.STATUS_BACK:
            print("** You have returned to the previous menu. **")
        elif status == constants.STATUS_EXIT:
            print("** You are out. **")
            break
        elif status == constants.EMPTY_INPUT:
            print("** You cannot leave the input blank! **")
        elif status == constants.NOT_NUMBER:
            print("** Please enter a valid number. **")
        elif status == constants.INVALID_INPUT:
            print("** Your choice is not in the list **")

    # # Delete note
    # elif choise == "4":
    #     pure_names = get_list_files()
    #     for i, file_name in enumerate(pure_names, start=1):
    #         print(f"''{i}. {file_name}''")
    #     file_name = select_file(pure_names)
    #     if file_name:
    #         if delete_file(file_name):
    #             print("Note DELETED!")
    #         else:
    #             print("Cancelled")

    #     else:
    #         print(">> Please choose from the options. <<")

    # Exit
    elif choise == "5":
        print("Goodbay!")
        break

    else:
        print(">> Please choose from the options. <<")
