from os import system
from auxiliary_functions import *

def orders_menu(clear_command, which_menu:str, operation_mode:str):
    
    my_file = 'Orders.txt'
    key_word = 'order'
    list_of_possible_choices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    file_content = check_if_file_exists_and_load_content(my_file)

    while True:
        print(f'{key_word.replace(key_word[0],key_word[0].upper())} menu:\n\
[0] Return to main menu\n\
[1] Print {key_word} list\n\
[2] Add new {key_word}\n\
[3] Amend existing {key_word}\n\
[4] Delete {key_word}\n\
[5] Search {key_word}s\n')

        user_input = check_if_input_is_a_menu_option(list_of_possible_choices)

        if user_input == -1:
            system(clear_command)
            print('Inappropriate input. Please input a pozitive single digit number, as per the menu\n')
        elif user_input == 0:
            system(clear_command)
            return file_content
        elif user_input == 1:
            if operation_mode == 'safe':
                file_content = check_if_file_exists_and_load_content(my_file)
            if file_content:
                system(clear_command)
                print(f'List of {key_word}s currently in the list:\n')
                for x in file_content:
                    print(x)
                print('')
            elif len(file_content) == 0:
                system(clear_command)
                print(f'The {key_word} list is empty\n')
        elif user_input == 2:
            customer_name = input("Please provide the customer name: ")
            customer_address = input("Please provide the customer address: ")
            customer_phone = input("Please provide the customer phone number: ")
            with open('Couriers.txt') as f:
                list_of_couriers = [x.replace('\n','') for x in f.readlines()]
            while True:
                for idx, courier in enumerate(list_of_couriers):
                    print(idx, courier)
                try:
                    courier = int(input("Please provide courier number to use: "))
                    if courier not in range(idx+1):
                        raise ValueError
                    break
                except ValueError:
                    system(clear_command)
                    print('Please input a valid number corresponding to one of the couriers.')
            status = 'preparing'
            product_to_add = {
                'customer_name': customer_name,
                'customer_address': customer_address,
                'customer_phone': customer_phone,
                'courier': courier,
                'status': status
            }
            print('')
            element_exists_already = False
            for element in file_content:
                if product_to_add  == list(element.values())[0]:
                    element_exists_already = True
            if element_exists_already == False:
                if operation_mode == 'safe':
                    append_to_file(my_file, file_content, product_to_add)
                system(clear_command)
                print(f'{key_word.replace(key_word[0],key_word[0].upper())} added succesfully.\n')
                file_content.append(product_to_add)
                return file_content
            else:
                system(clear_command)
                print(f'{key_word.replace(key_word[0],key_word[0].upper())} already exists.\n')
        elif user_input == 3:
            product_to_replace = input(f"Please enter the name of the {key_word} you wish to change: ").lower()
            print('')
            new_product = input(f"Please enter the name of the new {key_word}: ").lower()
            print('')
            if file_content and new_product not in file_content:
                try:
                    file_content[file_content.index(product_to_replace)] = new_product
                except ValueError:
                    system(clear_command)
                    print('The item you have inputted is not in the list.\n')
                if operation_mode == 'safe':
                    write_to_file(my_file, file_content)
                system(clear_command)
                print(f'{key_word.replace(key_word[0],key_word[0].upper())} {product_to_replace} has been replaced with {key_word} {new_product}.\n')
            elif len(file_content) == 0:
                system(clear_command)
                print(f'The {key_word} list is empty\n')
            elif new_product in file_content:
                system(clear_command)
                print(f'The value given for the new {key_word} already exists in the database.\n')
        elif user_input == 4:
            product_to_delete = input(f"Please enter the name of the {key_word} to delete: ").lower()
            print('')
            if file_content:
                try:
                    file_content.remove(product_to_delete)
                except ValueError:
                    system(clear_command)
                    print('The item you have inputted is not in the list.\n')
                if operation_mode == 'safe':
                    write_to_file(my_file, file_content)
                system(clear_command)
                print(f'{key_word.replace(key_word[0],key_word[0].upper())} {product_to_delete} has been deleted.\n')
            elif len(file_content) == 0:
                system(clear_command)
                print(f'The {key_word} list is empty\n')
        elif user_input == 5:
            product_to_search = input(f"Please enter the name of the {key_word} to search for: ").lower()
            print('')
            if file_content:
                system(clear_command)
                print(f'The following results have been found of keywork {product_to_search}:\n')
                for product in file_content:
                    if product_to_search in product:
                        print(product)
                print("")
            elif len(file_content) == 0:
                system(clear_command)
                print(f'The {key_word} list is empty\n')
        elif user_input == 6:
            pass
        elif user_input == 7:
            pass
        elif user_input == 8:
            pass