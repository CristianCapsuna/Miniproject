from os import system
from os_checker import set_clear_command
from auxiliary_functions import check_if_int
from auxiliary_functions import check_if_float
from auxiliary_functions import check_if_valid_choice
from file_handling_functions import persist_list_of_strings
from file_handling_functions import persist_list_of_dictionaries
from file_handling_functions import get_current_index
from file_handling_functions import read_file
from file_handling_functions import write_new_indexes
import config
from typing import List

CLEAR_COMMAND = set_clear_command()
system( CLEAR_COMMAND )
BACK_CHAR = "`"

INAPPROPRIATE_MENU_CHOICE_STATEMENT = 'Inappropriate input. Please input a positive single digit number, as per the menu\n'

class App:
    
    def __init__( self ):
        self.initialize_all_variables()
        
        while True:
            print(
                  f"Main menu:\n\n"
                  f"[1] Switch to {self.operation_mode} operation\n"
                   "[2] Product menu\n"
                   "[3] Couriers menu\n"
                   "[4] Orders menu\n"
                 )
            
            user_input = input(
                               f"To quit input {BACK_CHAR}\n"
                                "Please select a choice: "
                              )
            if user_input == BACK_CHAR:

                if self.operation_mode == "fast":
                    self.persist_products_from_memory()
                    self.persist_couriers_from_memory()
                    self.persist_orders_from_memory()
                exit()

            user_input = self.validate_user_input(
                                                  user_input,
                                                  [1, 2, 3, 4]
                                                  )

            if user_input == -1:
                self.guide_user( INAPPROPRIATE_MENU_CHOICE_STATEMENT )

            elif user_input == 1:
                self.change_operation_mode()

            elif user_input == 2:
                system( CLEAR_COMMAND )
                self.products_menu()
            elif user_input == 3:
                system( CLEAR_COMMAND )
                self.couriers_menu()
            elif user_input == 4:
                system( CLEAR_COMMAND )
                self.orders_menu()
    
    def products_menu(self):

        if len( self.products_content ) == 0:
            self.products_indexes, self.products_content = read_file( config.PRODUCTS_FILE )
            self.products_next_index = get_current_index( "product" )
        
        while True:
            self.print_generic_menu( "product" )

            user_input = input(
                               f"To go back input {BACK_CHAR}\n"
                                "Please select a choice: "
                              )
            
            if user_input == BACK_CHAR:
                system( CLEAR_COMMAND )
                if self.operation_mode == "fast":
                    self.persist_products_from_memory()            
                break

            user_input = self.validate_user_input(
                                                  user_input,
                                                  [1, 2, 3, 4, 5]
                                                 )

            if user_input == -1:
                self.guide_user(INAPPROPRIATE_MENU_CHOICE_STATEMENT)
            
            elif user_input == 1:
                system( CLEAR_COMMAND )
                self.print_all_items(
                                self.products_indexes,
                                self.products_content,
                                "products"
                                )
            
            elif user_input == 2:
                self.products_next_index = self.add_user_input_if_new(
                                           config.PRODUCTS_FILE,
                                           self.products_indexes,
                                           self.products_content,
                                           self.products_next_index
                                          )
                
                if self.operation_mode == "safe":
                        self.persist_products_from_memory()
            
            elif user_input == 3 or user_input == 4:
                self.products_next_index = self.change_or_delete_element_in_lists(
                                                       config.PRODUCTS_FILE,
                                                       self.products_indexes,
                                                       self.products_content,
                                                       self.products_next_index,
                                                       user_input
                                                      )
            
                if self.operation_mode == "safe":
                        self.persist_products_from_memory()

            elif user_input == 5:
                self.search_for_string_in_list(self.products_indexes, self.products_content)
    
    def couriers_menu(self):

        if len( self.couriers_content ) == 0:
            self.couriers_indexes, self.couriers_content = read_file( config.COURIERS_FILE )
            self.couriers_next_index = get_current_index( "courier" )
        
        while True:
            self.print_generic_menu( "courier" )

            user_input = input(
                               f"To go back input {BACK_CHAR}\n"
                                "Please select a choice: "
                              )
            
            if user_input == BACK_CHAR:
                system( CLEAR_COMMAND )
                if self.operation_mode == "fast":
                    self.persist_couriers_from_memory()            
                break

            user_input = self.validate_user_input(
                                                  user_input,
                                                  [1, 2, 3, 4, 5]
                                                 )

            if user_input == -1:
                self.guide_user(INAPPROPRIATE_MENU_CHOICE_STATEMENT)
            
            elif user_input == 1:
                system( CLEAR_COMMAND )
                self.print_all_items(
                                self.couriers_indexes,
                                self.couriers_content,
                                "couriers"
                                )
            
            elif user_input == 2:
                self.couriers_next_index = self.add_user_input_if_new(
                                           config.COURIERS_FILE,
                                           self.couriers_indexes,
                                           self.couriers_content,
                                           self.couriers_next_index
                                          )
                
                if self.operation_mode == "safe":
                        self.persist_couriers_from_memory()
            
            elif user_input == 3 or user_input == 4:
                self.couriers_next_index = self.change_or_delete_element_in_lists(
                                                       config.COURIERS_FILE,
                                                       self.couriers_indexes,
                                                       self.couriers_content,
                                                       self.couriers_next_index,
                                                       user_input
                                                      )
                
                if self.operation_mode == "safe":
                        self.persist_couriers_from_memory()
            
            elif user_input == 5:
                self.search_for_string_in_list(self.couriers_indexes, self.couriers_content)
    
    def orders_menu(self):
        
        if len( self.orders_content ) == 0:
            self.orders_indexes, self.orders_content = read_file( config.ORDERS_FILE )
            self.orders_next_index = get_current_index( "order" )
        
        while True:
            self.print_generic_menu( "order" )

            user_input = input(
                               f"To go back input {BACK_CHAR}\n"
                                "Please select a choice: "
                              )
            
            if user_input == BACK_CHAR:
                system( CLEAR_COMMAND )
                if self.operation_mode == "fast":
                    self.persist_orders_from_memory()
                break

            user_input = self.validate_user_input(
                                                  user_input,
                                                  [1, 2, 3, 4, 5]
                                                 )
            
            if user_input == -1:
                self.guide_user(INAPPROPRIATE_MENU_CHOICE_STATEMENT)
            
            elif user_input == 1:
                system( CLEAR_COMMAND )
                self.print_all_items(
                                self.orders_indexes,
                                self.orders_content,
                                "orders"
                                )
            
            elif user_input == 2:
                system( CLEAR_COMMAND )
                self.orders_next_index = self.build_dictionary_and_add(
                    [ "customer name", "customer address", "customer phone", "courier", "status", "list of products" ],
                    [ str, str, int, int, str, list ],
                    self.orders_indexes,
                    self.orders_content,
                    self.orders_next_index
                )

                if self.operation_mode == "safe":
                    self.persist_orders_from_memory()
            
            elif user_input == 3:
                system( CLEAR_COMMAND )
                self.print_all_items( self.orders_indexes, self.orders_content, "orders" )
                item_to_replace_index = input(f"To go back input {BACK_CHAR}\n"
                                              f"Please enter the index of the order you wish to change: ")
                
                if item_to_replace_index == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    continue

                item_to_replace_index = check_if_int(item_to_replace_index)
                if item_to_replace_index in self.orders_indexes:
                    item_position_in_list = self.orders_indexes.index(item_to_replace_index)
                    dictionary_to_change = self.change_dictionary( self.orders_content[item_position_in_list] )
                    self.orders_content[item_position_in_list] = dictionary_to_change
                else:
                    system(clear_command)
                    print(f'\nThe number given for the {key_word} to replace does not exist or is not a number.\n')
                    continue

            elif user_input == 4:
                self.orders_next_index = self.change_or_delete_element_in_lists(
                                                       config.ORDERS_FILE,
                                                       self.orders_indexes,
                                                       self.orders_content,
                                                       self.orders_next_index,
                                                       user_input
                                                      )

    def initialize_all_variables( self ):
        self.products_content = []
        self.products_indexes = []
        self.products_next_index = None
        self.couriers_content = []
        self.couriers_indexes = []
        self.couriers_next_index = None
        self.orders_content = []
        self.orders_indexes = []
        self.orders_next_index = None
        self.operation_mode = "fast"

    def persist_products_from_memory( self ):
        
        if len( self.products_content ) > 0:
            persist_list_of_strings(
                                    config.PRODUCTS_FILE,
                                    self.products_indexes,
                                    self.products_content
                                    )
            write_new_indexes(
                              config.PRODUCTS_FILE,
                              self.products_next_index
                              )

    def persist_couriers_from_memory( self ):

        if len( self.couriers_content ) > 0:
            persist_list_of_strings(
                                    config.COURIERS_FILE,
                                    self.couriers_indexes,
                                    self.couriers_content
                                    )
            write_new_indexes(
                              config.COURIERS_FILE,
                              self.couriers_next_index
                              )

    def persist_orders_from_memory( self ):

        if len( self.orders_content ) > 0:
            persist_list_of_dictionaries(
                                         config.ORDERS_FILE,
                                         self.orders_indexes,
                                         self.orders_content
                                         )
            write_new_indexes(
                              config.ORDERS_FILE,
                              self.orders_next_index
                              )

    def guide_user( self, message: str ):
        system( CLEAR_COMMAND )
        print( message )
    
    def change_operation_mode( self ):

        if self.operation_mode == "fast":
            self.operation_mode = "safe"

        else:
            self.operation_mode = "fast"
        system(CLEAR_COMMAND)

    
    def print_generic_menu( self, key_word: str):
        print(
              f"{key_word.replace(key_word[0],key_word[0].upper())} menu:\n\n"
              f"[1] Print {key_word} list\n"
              f"[2] Add new {key_word}\n"
              f"[3] Amend existing {key_word}\n"
              f"[4] Delete {key_word}\n"
              f"[5] Search {key_word}s\n"
               )

    def print_all_items( self, indexes: List, content: List, key_word: str):

        if len( content ) > 0:
            print( f'List of {key_word} currently in the list:\n' )

            for idx in range( len( indexes ) ):
                print(
                      "ID: " + str( indexes[idx] ) +
                     f" | {key_word.replace( key_word[0], key_word[0].upper() )}: " + str( content[idx] )
                     )
            print()

        else:
            system( CLEAR_COMMAND )
            print( f'The {key_word} list is empty\n' )
    
    def get_string_from_user( self, key_word: str ):
        input_string = input(
                            f"To quit input {BACK_CHAR}\n"
                            f"Please provide the {key_word}: "
                            )
        print()

        return input_string
    
    def validate_user_input( self, user_input: str, list_of_choices: List ):
        user_input = check_if_int (user_input )
        user_input = check_if_valid_choice(
                                           user_input,
                                           list_of_choices
                                          )
        return user_input

    def add_user_input_if_new(self,
                              my_file: str,
                              indexes: List,
                              content: List,
                              next_index: int,
                              pos_of_replace_id: int = 0):
        
        system( CLEAR_COMMAND )
        item_to_add = self.get_string_from_user( "product" )

        if item_to_add == BACK_CHAR:
            system(CLEAR_COMMAND)
            return

        item_to_add_lowered = item_to_add.lower()
        lowered_content = [x.lower() for x in content]

        if item_to_add_lowered not in lowered_content:
            if pos_of_replace_id == 0:
                indexes.append( next_index )
                next_index += 1
                content.append( item_to_add )
            else:
                indexes[ pos_of_replace_id ] = next_index
                next_index += 1
                content[ pos_of_replace_id ] = item_to_add
            system( CLEAR_COMMAND )
            if self.operation_mode == "safe":
                persist_list_of_strings(
                                        my_file,
                                        indexes,
                                        content
                                       )
            print( f"{item_to_add} added succesfully.\n" )

        else:
            system( CLEAR_COMMAND )
            print( f"{item_to_add} already exists.\n" )
        
        return next_index
    
    def print_content_and_get_id_to_change( self, indexes: List, content: List ):
        system(CLEAR_COMMAND)
        self.print_all_items(
                            indexes,
                            content,
                            "products"
                            )
        id_to_replace = input( 
            f"To quit input {BACK_CHAR}\n"
             "Please enter the index of the product you wish to change: "
            )
        print()

        if id_to_replace == BACK_CHAR:
            return BACK_CHAR

        id_to_replace = check_if_int( id_to_replace )
        return id_to_replace
    
    def search_for_string_in_list(self, indexes, content):
        if len(content) == 0:
            system(CLEAR_COMMAND)
            print(f"The product list is empty\n")
            return

        system( CLEAR_COMMAND )
        product_to_search = self.get_string_from_user( "product" )

        system( CLEAR_COMMAND )
        print(f'The following results have been found of keywork {product_to_search}:\n')
        for product in content:
            if product_to_search.lower() in product.lower():
                index_of_product = content.index(product)
                print("ID: " + str( indexes[ index_of_product ] ) + " | Item: " + product)
        print()
    
    def change_or_delete_element_in_lists(
                                          self,
                                          my_file: str,
                                          indexes: List,
                                          content: List,
                                          next_index: int,
                                          user_input: int
                                          ):
        
        if len(content) == 0:
            system(CLEAR_COMMAND)
            print(f"The product list is empty\n")
            return

        id_to_change = self.print_content_and_get_id_to_change( indexes, content )
        
        if id_to_change == BACK_CHAR:
            system( CLEAR_COMMAND )
            return

        if id_to_change in indexes:
            pos_of_id_to_change = indexes.index( id_to_change )

            if user_input == 3:
                next_index = self.add_user_input_if_new(
                                            my_file,
                                            indexes,
                                            content,
                                            next_index,
                                            pos_of_id_to_change
                                            )
            else:
                deleted_content = content.pop(pos_of_id_to_change)
                deleted_id = indexes.pop(pos_of_id_to_change)
                system( CLEAR_COMMAND )
                print(f"ID {deleted_id} | {deleted_content} has been deleted.\n")
        else:
            self.guide_user( "The ID given for the product to replace does not exist or is not a number.\n" )
        
        return next_index
    
    def build_dictionary_and_add(
                                 self,
                                 list_of_keys: List,
                                 list_of_data_types: List,
                                 indexes: List,
                                 content: List,
                                 next_index: int
                                 ):
        # new_dict = {"id": next_index}
        new_dict = {}
        print(f"To go back input {BACK_CHAR}\n")
        for idx, data_type in enumerate(list_of_data_types):

            if list_of_keys[ idx ] == "courier":
                courier_number = self.choose_from_couriers()

                if courier_number == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    return
                
                new_dict[ "courier" ] = courier_number

            elif list_of_keys[ idx ] == "list of products":
                list_of_products = self.choose_from_products()

                if list_of_products == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    return
                
                new_dict[ "list of products" ] = list_of_products

            elif list_of_keys[ idx ] == "status":
                new_dict[ "status" ] = "Preparing"

            elif data_type == str:
                system( CLEAR_COMMAND )

                expected_string = self.get_string_from_user( list_of_keys[idx] )

                if expected_string == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    return
                print()
                new_dict[ list_of_keys[idx] ] = expected_string

            elif data_type == int or data_type == float:

                expected_number = get_number_of_same_type( data_type, list_of_keys[idx] )

                if expected_string == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    return

                print()
                new_dict[ list_of_keys[idx] ] = expected_number
            
        if new_dict not in content:
            indexes.append(next_index)
            next_index += 1
            content.append(new_dict)
            system( CLEAR_COMMAND )
            print(f"{new_dict} added succesfully.\n")
        else:
            system( CLEAR_COMMAND )
            print(f"{new_dict} already exists.\n")
            
            return next_index
    
    def choose_from_couriers( self ):
        if len( self.couriers_content ) == 0:
            self.couriers_indexes, self.couriers_content = read_file( config.COURIERS_FILE )

        while True:
            self.print_all_items( self.couriers_indexes, self.couriers_content, "couriers" )

            user_input = input(f"To go back, input {BACK_CHAR}\n"
                                "Please chose an ID: ")

            if user_input == BACK_CHAR:
                return BACK_CHAR

            user_input = check_if_int(user_input)
            if user_input in self.couriers_indexes:
                return user_input
            else:
                system( CLEAR_COMMAND )
                print("\nPlease input a valid number corresponding to one of the couriers.\n")
    
    def choose_from_products( self ):
        if len( self.products_content ) == 0:
            self.products_indexes, self.products_content = read_file( config.PRODUCTS_FILE )

        while True:
            self.print_all_items( self.products_indexes, self.products_content, "products" )

            user_input = input(f"To go back, input {BACK_CHAR}\n"
                                "Please chose IDs separated with a comma: ")

            if user_input == BACK_CHAR:
                return BACK_CHAR
            
            try:
                list_of_inputs = [int(x) for x in user_input.split(",")]
            except ValueError:
                system( CLEAR_COMMAND )
                print("Incorrect input. Only numbers separated by commas are allowed.\n")
                continue

            choices_which_exist, choices_which_dont_exist = [], []

            for choice in list_of_inputs:

                if choice in self.products_indexes:
                    choices_which_exist.append(choice)
                else:
                    choices_which_dont_exist.append(choice)

            if len(choices_which_exist) == 0:
                system( CLEAR_COMMAND )
                print("None of the items inputted exist.\n")
                continue
            elif len(choices_which_dont_exist) != 0:
                system( CLEAR_COMMAND )
                print(f"Items {choices_which_exist} have been added.\n"
                      f"Items {choices_which_dont_exist} don't exist so have not been added.\n")
                return list_of_inputs
            else:
                system( CLEAR_COMMAND )
                print(f"Items {choices_which_exist} have been added.")
                return list_of_inputs
    
    def change_dictionary( self, dictionary_to_change: dict ):
        dict_keys = list(dictionary_to_change.keys())
        dict_values = list(dictionary_to_change.values())

        while True:
            print("Please select which attribute you wish to change:\n")

            for keys_index, value in enumerate(dict_keys):
                print(f"[{keys_index}] {value}")
            user_input = input(f"\nTo go back input {BACK_CHAR}\n"
                                "Please select a choice: ")

            if user_input == BACK_CHAR:
                system( CLEAR_COMMAND )
                return dictionary_to_change

            user_input = check_if_int(user_input)
            user_input = check_if_valid_choice(user_input, range(keys_index + 1))
            print()

            if user_input == -1:
                system( CLEAR_COMMAND )
                print("The choice entered is not a number or not in the list.\n")
                continue

            key_at_index = dict_keys[user_input]
            value_at_index = dict_values[user_input]
            type_of_value_at_index = type(value_at_index)
            print( type_of_value_at_index )

            if key_at_index == "courier":
                dictionary_to_change = self.change_courier( dictionary_to_change )

            elif key_at_index == "list of products":
                dictionary_to_change = self.change_list_of_products( dictionary_to_change )

            elif key_at_index == "status":
                dictionary_to_change = self.change_status( dictionary_to_change )

            elif type_of_value_at_index == str:
                system( CLEAR_COMMAND )

                print(f"Current value is {str(dictionary_to_change[key_at_index])}\n")

                new_string = self.get_string_from_user( value_at_index )

                if new_string == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    return dictionary_to_change
                print()

                if new_string != value_at_index:
                    dictionary_to_change[ key_at_index ] = new_string
                    system( CLEAR_COMMAND )
                    print("Value changed sucessfully.\n")
                else:
                    system( CLEAR_COMMAND )
                    print("The value inputted is the same as the one currently present.\n")

            elif type_of_value_at_index == int or type_of_value_at_index == float:
                system( CLEAR_COMMAND )

                print(f"Current value is {str(dictionary_to_change[key_at_index])}\n")

                expected_number = self.get_number_of_same_type( type_of_value_at_index, key_at_index )

                if expected_number == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    return dictionary_to_change

                if value_at_index != expected_number:
                    dictionary_to_change[ key_at_index ] = expected_number
                    system( CLEAR_COMMAND )
                    print("Value changed sucessfully.\n")
                else:
                    system( CLEAR_COMMAND )
                    print("The value inputted is the same as the one currently present.\n")

        return dictionary_to_change

    def change_courier( self, dictionary_to_change: dict ):
        system( CLEAR_COMMAND )
        while True:
            print(f"Courier currently being used is ID {str(dictionary_to_change['courier'])}\n")
            courier_number = self.choose_from_couriers()

            if courier_number == BACK_CHAR:
                system( CLEAR_COMMAND )
                return dictionary_to_change

            current_courier_number = dictionary_to_change["courier"]
            if courier_number != current_courier_number:
                dictionary_to_change["courier"] = courier_number
                system( CLEAR_COMMAND )
                print("Courier changed succesfully\n")
                return dictionary_to_change
            else:
                system( CLEAR_COMMAND )
                print("The new value provided is the same as the value currently present\n")
        
    def change_list_of_products ( self, dictionary_to_change):
        system( CLEAR_COMMAND )
        while True:
            print(f"IDs of products currently in the list {str(dictionary_to_change['list of products'])}\n")
            list_of_products = self.choose_from_products()

            if list_of_products == BACK_CHAR:
                system( CLEAR_COMMAND )
                return dictionary_to_change

            current_list_of_products = dictionary_to_change[ "list of products" ]
            are_identical = True
            for idx in range( len( current_list_of_products ) ):

                if current_list_of_products[idx] != dictionary_to_change["list of products"][idx]:
                    are_identical = False
                    break

            if are_identical != False:
                dictionary_to_change["list of products"] = list_of_products
                system( CLEAR_COMMAND )
                print("List of products changed succesfully\n")
                return dictionary_to_change
            else:
                system( CLEAR_COMMAND )
                print("The new value provided is the same as the value currently present\n")
    
    def change_status( self, dictionary_to_change ):
        system( CLEAR_COMMAND )
        with open("list_of_possible_statuses.txt") as f:
            print(f"The current order status is {dictionary_to_change['status']}\n")

            lines = [x.replace("\n", "") for x in f.readlines()]
            while True:
                print("The available statuses are as per the below:\n")


                for idx, status in enumerate(lines):
                    print(f"[{idx}] {status}")
                print()

                user_input = input(f"To go back input {BACK_CHAR}\n"
                                    "Please choose which status you would like to use: ")

                if user_input == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    return dictionary_to_change

                user_input = check_if_int(user_input)
                user_input = check_if_valid_choice(user_input, range(idx + 2))
                print()

                if user_input == -1:
                    system( CLEAR_COMMAND )
                    print("The given value is not a number or not in the list.\n")
                    continue

                new_shipping_status = lines[user_input]

                if new_shipping_status == dictionary_to_change["status"]:
                    system( CLEAR_COMMAND )
                    print("The new status provided is the same as the existing one\n")
                    print(f"The current order status is {dictionary_to_change['status']}\n")
                else:
                    dictionary_to_change["status"] = new_shipping_status
                    system( CLEAR_COMMAND )
                    print("Status changed succesfully\n")
                    return dictionary_to_change
    
    def get_number_of_same_type( self, data_type: type, key_word: str ):
        if data_type == int:
            my_func = int
        else:
            my_func = float

        while True:
            expected_number = self.get_string_from_user( key_word )

            if expected_number == BACK_CHAR:
                system( CLEAR_COMMAND )
                return BACK_CHAR

            try:
                expected_number = my_func(expected_number)
                return expected_number
            except ValueError:
                system( CLEAR_COMMAND )
                print("Please input only numbers.\n")

start = App()