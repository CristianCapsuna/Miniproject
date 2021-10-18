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
            if which_menu in ["products", "couriers"]:
                item_to_add = input(f"Please provide {key_word} to add: ")
                print()
                item_to_check = item_to_add.lower()
                list_of_items = [x.lower() for x in file_content["content"]]
            elif which_menu == "orders":
                print()
                customer_name = input("Please provide the customer name: ")
                customer_address = input("Please provide the customer address: ")
                customer_phone = input("Please provide the customer phone number: ")
                list_of_couriers = read_file("Couriers.txt")
                while True:
                    print()
                    print("List of available couriers:\n")
                    for idx in range(len(list_of_couriers["indexes"])):
                        print("ID: " + str(list_of_couriers["indexes"][idx]) + " | Courier: " + str(list_of_couriers["content"][idx]))
                    try:
                        print()
                        courier_number = input("Please provide courier number to use: ")
                        courier_number = check_if_int(courier_number)
                        if courier_number not in list_of_couriers["indexes"]:
                            raise ValueError
                        break
                    except ValueError:
                        system(clear_command)
                        print("Customer name given: ", customer_name)
                        print("Customer address given: ", customer_address)
                        print("Customer phone number given: ", customer_phone)
                        print()
                        print('Please input a valid number corresponding to one of the couriers.')
                status = 'preparing'
                item_to_add = {
                    'customer_name': customer_name,
                    'customer_address': customer_address,
                    'customer_phone': customer_phone,
                    'courier': courier_number,
                    'status': status
                }
                print('')
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
            product_to_replace_index = input(f"Please use function 5 to find the index of the product you wish to change.\n\
Please enter the index of the {key_word} you wish to change: ")
            print('')
            product_to_replace_index = check_if_int(product_to_replace_index)
            if product_to_replace_index not in file_content["indexes"]:
                system(clear_command)
                print(f'The number given for the {key_word} to replace does not exist or is not a number.\n')
                continue
            new_product = input(f"Please enter the name of the new {key_word}: ")
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