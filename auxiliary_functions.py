from typing import List
from file_handling_functions import read_file
from os import system

def check_if_int(user_input) -> int:
    try:
        my_int = int(user_input)
        return my_int
    except ValueError:
        return -1

def check_if_float(user_input) -> float:
    try:
        my_float = float(user_input)
        return my_float
    except ValueError:
        return -1

def check_if_valid_choice(user_input, choices:List[int]) -> int:
    if user_input in choices:
        return user_input
    else:
        return -1

def get_input_from_file(clear_command: str, my_file: str, is_multi_choice: bool, specific_file_content: dict = None):

    if specific_file_content == None:
        specific_file_content = read_file(my_file)

    while True:
        print_file_content(my_file, specific_file_content)

        user_input = input("To go back, input `.\n\
For multiple products please input the items separated by a comma.\n\
Please provide new ID(s): ")
        if user_input == "`":
            return -1
        if is_multi_choice == False:
            user_input = check_if_int(user_input)
            if user_input in specific_file_content["indexes"]:
                return user_input
            else:
                system(clear_command)
                print("\nPlease input a valid number corresponding to one of the couriers.\n")
        elif is_multi_choice == True:
            list_of_inputs = [int(x) for x in user_input.split(",")]
            choices_which_exist, choices_which_dont_exist = [], []
            for choice in list_of_inputs:
                if choice in specific_file_content["indexes"]:
                    choices_which_exist.append(choice)
                else:
                    choices_which_dont_exist.append(choice)
            if len(choices_which_exist) == 0:
                system(clear_command)
                print("None of the items inputted exist.\n")
                continue
            elif len(choices_which_dont_exist) != 0:
                system(clear_command)
                print(f"Items {choices_which_exist} have been added.\n\
Items {choices_which_dont_exist} don't exist so have not been added.\n")
                return list_of_inputs
            else:
                system(clear_command)
                print(f"Items {choices_which_exist} have been added.")
                return list_of_inputs

def change_item_in_dictionary(clear_command:str, couriers_file: str, products_file: str, dictionary_to_change: dict,\
                                products_file_content: dict = None, couriers_file_content: dict = None):
    dict_keys = list(dictionary_to_change.keys())
    dict_values = list(dictionary_to_change.values())

    while True:
        print("Please select which attribute you wish to change:\n")
        for keys_index, value in enumerate(dict_keys):
            print(f"[{keys_index}] {value}")
        user_input = input("\nTo go back input `\n\
Please select a choice: ")
        if user_input == "`":
            break
        user_input = check_if_int(user_input)
        user_input = check_if_valid_choice(user_input, range(keys_index + 1))
        print()

        if user_input == -1:
            system(clear_command)
            print("The choice entered is not a number or not in the list.\n")
            continue

        key_at_index = dict_keys[user_input]
        type_of_value_at_index = type(dict_values[user_input])

        if key_at_index == "Courier":
            system(clear_command)
            while True:
                print(f"Courier currently being used is ID {str(dictionary_to_change['Courier'])}\n")
                courier_number = get_input_from_file(clear_command, couriers_file, False, couriers_file_content)
                if courier_number == -1:
                    system(clear_command)
                    break
                current_courier_number = dictionary_to_change["Courier"]
                if courier_number != current_courier_number:
                    dictionary_to_change["Courier"] = courier_number
                    system(clear_command)
                    print("Courier changed succesfully\n")
                    break
                else:
                    system(clear_command)
                    print("The new value provided is the same as the value currently present\n")

        elif key_at_index == "Status":
            system(clear_command)
            with open("list_of_possible_statuses.txt") as f:
                print(f"The current order status is {dictionary_to_change['Status']}\n")

                lines = [x.replace("\n", "") for x in f.readlines()]
                while True:
                    print("The available statuses are as per the below:\n")
                    for idx, status in enumerate(lines):
                        print(f"[{idx}] {status}")
                    print(f"[{idx+1}] Return to previous menu\n")
                    user_input = input("Please choose which status you would like to use: ")
                    user_input = check_if_int(user_input)
                    user_input = check_if_valid_choice(user_input, range(idx + 2))
                    print()
                    if user_input == -1:
                        system(clear_command)
                        print("The given value is not a number or not in the list. Try again.\n")
                        continue
                    elif user_input == idx + 1:
                        break
                    new_shipping_status = lines[user_input]
                    if new_shipping_status == dictionary_to_change["Status"]:
                        system(clear_command)
                        print("The new status provided is the same as the existing one\n")
                        print(f"The current order status is {dictionary_to_change['Status']}\n")
                    else:
                        dictionary_to_change["Status"] = new_shipping_status
                        system(clear_command)
                        print("Status changed succesfully")
                        break
        elif key_at_index == "List of products":
            # Candidate for refactoring and comunizing with code from Courier case
            system(clear_command)
            while True:
                print(f"IDs of products currently in the list {str(dictionary_to_change['List of products'])}\n")
                list_of_products = get_input_from_file(clear_command, products_file, True, products_file_content)
                if list_of_products == -1:
                    system(clear_command)
                    break
                current_list_of_products = dictionary_to_change["List of products"]
                are_identical = True
                for idx in range(len(current_list_of_products)):
                    if current_list_of_products[idx] != dictionary_to_change["List of products"][idx]:
                        are_identical = False
                if are_identical != False:
                    dictionary_to_change["List of products"] = list_of_products
                    system(clear_command)
                    print("List of products changed succesfully\n")
                    break
                else:
                    system(clear_command)
                    print("The new value provided is the same as the value currently present\n")
        elif type_of_value_at_index == str or type_of_value_at_index == int or type_of_value_at_index == float:
            system(clear_command)
            current_value = dict_values[user_input]
            while True:
                print(f"The currently present value is {current_value}\n")
                new_value = input("To go back input `.\n\
Please input the new desired value: ")
                int_new_value = check_if_int(new_value)
                float_new_value = check_if_float(new_value)
                if int_new_value != -1:
                    new_value = int_new_value
                elif float_new_value != -1:
                    new_value = float_new_value

                if new_value == '`':
                    system(clear_command)
                    break
                elif current_value != new_value:
                    dictionary_to_change[list(dict_keys)[user_input]] = new_value
                    system(clear_command)
                    print("Value changed sucessfully.\n")
                    break
                else:
                    system(clear_command)
                    print("The value inputted is the same as the one currently present.\n")

    return dictionary_to_change

def print_file_content(my_file: str, specific_file_content:dict):
    print(f"List of available {my_file.split('.')[0].lower()}:\n")
    for idx in range(len(specific_file_content["indexes"])):
        print("ID: " + str(specific_file_content["indexes"][idx]) + f" | {my_file.split('.')[0]}: " + str(specific_file_content["content"][idx]))
    print()