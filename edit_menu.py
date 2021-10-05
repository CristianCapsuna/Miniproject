from os import system
from auxiliary_functions import *

def edit_menu(clear_command, which_menu:str, operation_mode:str):
    if which_menu == 'products':
        file = 'Products.txt'
        key_word = 'product'
    elif which_menu == 'curiers':
        file = 'Curiers.txt'
        key_word = 'courier'
    
    file_content = check_if_file_exists_and_load_content(file)
    
    while True:
        print(f'{key_word.replace(key_word[0],key_word[0].upper())} menu:\n\
[0] Return to main menu\n\
[1] Print {key_word} list\n\
[2] Add new {key_word}\n\
[3] Amend existing {key_word}\n\
[4] Delete {key_word}\n\
[5] Search {key_word}s\n')
        
        user_input = check_if_input_is_a_menu_option([0, 1, 2, 3, 4, 5])

        if user_input == -1:
            system(clear_command)
            print('Inappropriate input. Please input a pozitive single digit number, as per the menu\n')
        elif user_input == 0:
            system(clear_command)
            return file_content
        elif user_input == 1:
            if operation_mode == 'safe':
                file_content = check_if_file_exists_and_load_content(file)
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
            product_to_add = input(f"Please provide {key_word} to add: ").lower()
            print('')
            if product_to_add not in file_content:
                if operation_mode == 'safe':
                    write_to_file(file, file_content, 'append', product_to_add)
                file_content.append(product_to_add)
                system(clear_command)
                print(f'{key_word.replace(key_word[0],key_word[0].upper())} added succesfully.\n')
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
                    write_to_file(file, file_content)
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
                    write_to_file(file, file_content)
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
