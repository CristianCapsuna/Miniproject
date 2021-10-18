from os import system
from auxiliary_functions import *
from file_handling_functions import *

def edit_menu(clear_command, which_menu:str, operation_mode:str):
    
    if which_menu == 'products':
        my_file = 'Products.txt'
        key_word = 'product'
    elif which_menu == 'couriers':
        my_file = 'Couriers.txt'
        key_word = 'courier'
    elif which_menu == 'orders':
        my_file = 'Orders.txt'
        key_word = 'order'
    
    file_content = read_file(my_file)
    next_index = get_specific_index(my_file)

    while True:

        print(f'{key_word.replace(key_word[0],key_word[0].upper())} menu:\n\n\
[0] Return to main menu\n\
[1] Print {key_word} list\n\
[2] Add new {key_word}\n\
[3] Amend existing {key_word}\n\
[4] Delete {key_word}\n\
[5] Search {key_word}s\n')

        user_input = input("Please select a choice: ")
        user_input = check_if_int(user_input)
        user_input = check_if_valid_choice(user_input, [0, 1, 2, 3, 4, 5])
        print()

        if user_input == -1:
            system(clear_command)
            print('Inappropriate input. Please input a pozitive single digit number, as per the menu\n')
        elif user_input == 0:
            system(clear_command)
            break
        elif user_input == 1:
            if file_content["content"]:
                system(clear_command)
                print(f'List of {key_word}s currently in the list:\n')
                for idx in range(len(file_content["indexes"])):
                    print("ID: " + str(file_content["indexes"][idx]) + f" | {key_word.replace(key_word[0],key_word[0].upper())}: " + str(file_content["content"][idx]))
                print('')
            elif len(file_content["content"]) == 0:
                system(clear_command)
                print(f'The {key_word} list is empty\n')
        elif user_input == 2:
            system(clear_command)
            if which_menu in ["products", "couriers"]:
                item_to_add = input(f"Please provide {key_word} to add: ")
                print()
                item_to_check = item_to_add.lower()
                list_of_items = [x.lower() for x in file_content["content"]]
            elif which_menu == "orders":
                customer_name = input("Please provide the customer name: ")
                print()
                customer_address = input("Please provide the customer address: ")
                print()
                customer_phone = input("Please provide the customer phone number: ")
                print()
                courier_number = get_courier_input(clear_command, customer_name, customer_address, customer_phone)
                status = 'preparing'
                item_to_add = {
                    "customer_name": customer_name,
                    "customer_address": customer_address,
                    "customer_phone": customer_phone,
                    "courier": courier_number,
                    "status": status
                }
                item_to_check = item_to_add
                list_of_items = file_content["content"]
            if item_to_check not in list_of_items:
                file_content['indexes'].append(next_index)
                next_index += 1
                file_content['content'].append(item_to_add)
                system(clear_command)
                if operation_mode == 'safe':
                    write_to_file(my_file, file_content, next_index)
                print(f'{key_word.replace(key_word[0],key_word[0].upper())} added succesfully.\n')
            else:
                system(clear_command)
                print(f'{key_word.replace(key_word[0],key_word[0].upper())} already exists.\n')
        elif user_input == 3:
            product_to_replace_index = input(f"Please enter the index of the {key_word} you wish to change: ")
            print()
            product_to_replace_index = check_if_int(product_to_replace_index)
            if product_to_replace_index not in file_content["indexes"]:
                system(clear_command)
                print(f'The number given for the {key_word} to replace does not exist or is not a number.\n')
                continue
            if which_menu in ["products", "couriers"]:
                new_product = input(f"Please enter the name of the new {key_word}: ")
                print()
                lowered_content = [x.lower() for x in file_content["content"]]
                if file_content["indexes"] and\
                new_product.lower() not in lowered_content:
                    try:
                        file_content["content"][file_content["indexes"].index(product_to_replace_index)] = new_product
                        file_content["indexes"][file_content["indexes"].index(product_to_replace_index)] = next_index
                        next_index += 1
                    except ValueError:
                        system(clear_command)
                        print('The item you have inputted is not in the list.\n')
                    if operation_mode == 'safe':
                        write_to_file(my_file, file_content, next_index)
                    system(clear_command)
                    print(f'{key_word.replace(key_word[0],key_word[0].upper())} of index {product_to_replace_index} has been replaced with {key_word} {new_product}.\n')
                elif len(file_content["content"]) == 0:
                    system(clear_command)
                    print(f'The {key_word} list is empty\n')
                elif new_product.lower() in lowered_content:
                    system(clear_command)
                    print(f'The name given for the new {key_word} already exists.\n')
            elif which_menu == "orders":
                while True:
                    print("Please select which attribute of the order you wish to change:\n\n\
[0] customer_name\n\
[1] customer_address\n\
[2] customer_phone\n\
[3] courier\n\
[4] status\n\
[5] list_of_items\n")
                    user_input = input("Please select a choice: ")
                    user_input = check_if_int(user_input)
                    user_input = check_if_valid_choice(user_input, [0, 1, 2, 3, 4, 5])
                    print()
                    if user_input == 0:
                        file_content = get_new_value("customer name", file_content, product_to_replace_index, clear_command)
                        system(clear_command)
                        print("Name changed succesfully")
                    elif user_input == 1:
                        file_content = get_new_value("customer address", file_content, product_to_replace_index, clear_command)
                        system(clear_command)
                        print("Address changed succesfully")
                    elif user_input == 2:
                        file_content = get_new_value("customer phone", file_content, product_to_replace_index, clear_command)
                        system(clear_command)
                        print("Phone changed succesfully")
                    elif user_input == 3:
                        while True:
                            courier_number = get_courier_input(clear_command)
                            current_courier_number = file_content["content"][file_content["indexes"].index(product_to_replace_index)]["courier"]
                            if courier_number != current_courier_number:
                                file_content["content"][file_content["indexes"].index(product_to_replace_index)]["courier"] = courier_number
                                break
                            else:
                                system(clear_command)
                                print("\nThe new value provided is the same as the value currently present. Please input another\n")
                        system(clear_command)
                        print("Courier changed succesfully")
                    elif user_input == 4:
                        with open("list_of_possible_statuses.txt") as f:
                            lines = [x.replace("\n", "") for x in f.readlines()]
                            while True:
                                print("The available statuses are as per the below:\n")
                                for idx, status in enumerate(lines):
                                    print(f"[{idx}] {status}")
                                user_input = input("\nPlease choose which status you would like to use: ")
                                user_input = check_if_int(user_input)
                                user_input = check_if_valid_choice(user_input, range(idx + 1))
                                print()
                                shipping_status = lines[user_input]
                                if user_input != -1 and shipping_status not in file_content["content"][file_content["indexes"].index(product_to_replace_index)]["status"]:
                                    file_content["content"][file_content["indexes"].index(product_to_replace_index)]["status"] = shipping_status
                                    break
                                elif user_input == -1:
                                    system(clear_command)
                                    print("The given value is not a number or not in the list. Try again.\n")
                                elif shipping_status in file_content["content"][file_content["indexes"].index(product_to_replace_index)]["status"]:
                                    system(clear_command)
                                    print("The new status provided is the same as the existing one. Nothing changed\n")
                                    break
                        system(clear_command)
                        print("Status changed succesfully")
                    elif user_input == 5:
                        pass
                        #code to come here
                    while True:
                        user_input = input("Do you wish to change anything else in this order?\n\n\
[0] No\n\
[1] Yes\n\n\
Choice: ")
                        user_input = check_if_int(user_input)
                        user_input = check_if_valid_choice(user_input, [0,1])
                        print()
                        if user_input != -1:
                            break
                    if user_input == 0:
                        break
                if operation_mode == 'safe':
                    write_to_file(my_file, file_content, next_index)
            system(clear_command)
        elif user_input == 4:
            product_to_delete_index = input(f"Please use function 5 to find the index of the product you wish to change.\n\
Please enter the index of the {key_word} you wish to change: ")
            print('')
            product_to_delete_index = check_if_int(product_to_delete_index)
            if product_to_delete_index not in file_content["indexes"]:
                system(clear_command)
                print(f'The number given for the {key_word} to replace does not exist or is not a number.\n')
                continue
            if file_content["indexes"]:
                file_content["content"].remove(file_content["content"][file_content["indexes"].index(product_to_delete_index)])
                file_content["indexes"].remove(product_to_delete_index)
                if operation_mode == 'safe':
                    write_to_file(my_file, file_content, next_index)
                system(clear_command)
                print(f'{key_word.replace(key_word[0],key_word[0].upper())} of index {product_to_delete_index} has been deleted.\n')
            elif len(file_content) == 0:
                system(clear_command)
                print(f'The {key_word} list is empty\n')
        elif user_input == 5:
            product_to_search = input(f"Please enter the name of the {key_word} to search for: ")
            print('')
            if file_content["content"]:
                system(clear_command)
                print(f'The following results have been found of keywork {product_to_search}:\n')
                for product in file_content["content"]:
                    if product_to_search.lower() in product.lower():
                        print("ID: " + str(file_content["indexes"][file_content["content"].index(product)]) + " | Item: " + product)
                print("")
            elif len(file_content["content"]) == 0:
                system(clear_command)
                print(f'The {key_word} list is empty\n')

    return file_content, next_index