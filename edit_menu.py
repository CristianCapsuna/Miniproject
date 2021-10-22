from os import system
from auxiliary_functions import *
from file_handling_functions import *

def edit_menu(clear_command, which_menu:str, operation_mode:str,\
    file_content: dict = None, next_index: int = None,\
    products_file_content: dict = None, couriers_file_content: dict = None):
    
    products_file = "Products.txt"
    couriers_file = "Couriers.txt"
    orders_file = "Orders.txt"

    if which_menu == 'products':
        my_file = products_file
        key_word = 'product'
    elif which_menu == 'couriers':
        my_file = couriers_file
        key_word = 'courier'
    elif which_menu == 'orders':
        my_file = orders_file
        key_word = 'order'
        if products_file_content == None:
            products_file_content = read_file(products_file)
        if couriers_file_content == None:
            couriers_file_content = read_file(couriers_file)

    if file_content == None:
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
                item_to_add = input(f"To go back input `.\n\
Please provide {key_word} to add: ")
                if item_to_add == "`":
                    system(clear_command)
                    continue
                print()
                item_to_check = item_to_add.lower()
                list_of_items = [x.lower() for x in file_content["content"]]
            elif which_menu == "orders":
                print("To go back input `.\n")
                customer_name = input("Please provide the customer name: ")
                if customer_name == "`":
                    system(clear_command)
                    continue
                print()
                customer_address = input("Please provide the customer address: ")
                if customer_address == "`":
                    system(clear_command)
                    continue
                print()
                while True:
                    customer_phone = input("Please provide the customer phone number: ")
                    if customer_phone.isnumeric() == True:
                        customer_phone = int(customer_phone)
                        break
                    else:
                        system(clear_command)
                        print("Please input only numbers.\n")
                if customer_phone == "`":
                    system(clear_command)
                    continue
                print()
                courier_number = get_input_from_file(clear_command, couriers_file, False, couriers_file_content)
                if courier_number == -1:
                    system(clear_command)
                    continue
                status = 'Preparing'
                list_of_products = get_input_from_file(clear_command, products_file, True, products_file_content)
                if list_of_products == -1:
                    system(clear_command)
                    continue
                item_to_add = {
                    "Customer name": customer_name,
                    "Customer address": customer_address,
                    "Customer phone": customer_phone,
                    "Courier": courier_number,
                    "Status": status,
                    "List of products": list_of_products
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
                print(f'{item_to_add} added succesfully.\n')
            else:
                system(clear_command)
                print(f'{item_to_add} already exists.\n')
        elif user_input == 3:
            system(clear_command)
            print_file_content(my_file, file_content)
            item_to_replace_index = input(f"To go back input `.\n\
Please enter the index of the {key_word} you wish to change: ")
            if item_to_replace_index == "`":
                system(clear_command)
                continue
            print()
            item_to_replace_index = check_if_int(item_to_replace_index)
            if item_to_replace_index not in file_content["indexes"]:
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
                        file_content["content"][file_content["indexes"].index(item_to_replace_index)] = new_product
                        file_content["indexes"][file_content["indexes"].index(item_to_replace_index)] = next_index
                        next_index += 1
                    except ValueError:
                        system(clear_command)
                        print('The item you have inputted is not in the list.\n')
                    if operation_mode == 'safe':
                        write_to_file(my_file, file_content, next_index)
                    system(clear_command)
                    print(f'{key_word.replace(key_word[0],key_word[0].upper())} of index {item_to_replace_index} has been replaced with {key_word} {new_product}.\n')
                elif len(file_content["content"]) == 0:
                    system(clear_command)
                    print(f'The {key_word} list is empty\n')
                elif new_product.lower() in lowered_content:
                    system(clear_command)
                    print(f'The name given for the new {key_word} already exists.\n')
            elif which_menu == "orders":
                item_position_in_list = file_content["indexes"].index(item_to_replace_index)
                dictionary_to_change = change_item_in_dictionary(clear_command, couriers_file, products_file, file_content["content"][item_position_in_list], products_file_content, couriers_file_content)
                file_content["content"][item_position_in_list] = dictionary_to_change
                if operation_mode == 'safe':
                    write_to_file(my_file, file_content, next_index)
            system(clear_command)
        elif user_input == 4:
            system(clear_command)
            print_file_content(my_file, file_content)
            item_to_delete_index = input(f"To go back input `.\n\
Please enter the index of the {key_word} you wish to change: ")
            if item_to_delete_index == "`":
                system(clear_command)
                continue
            print()
            item_to_delete_index = check_if_int(item_to_delete_index)
            if item_to_delete_index not in file_content["indexes"]:
                system(clear_command)
                print(f'The number given for the {key_word} to replace does not exist or is not a number.\n')
                continue
            if file_content["indexes"]:
                file_content["content"].remove(file_content["content"][file_content["indexes"].index(item_to_delete_index)])
                file_content["indexes"].remove(item_to_delete_index)
                if operation_mode == 'safe':
                    write_to_file(my_file, file_content, next_index)
                system(clear_command)
                print(f'{key_word.replace(key_word[0],key_word[0].upper())} of index {item_to_delete_index} has been deleted.\n')
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