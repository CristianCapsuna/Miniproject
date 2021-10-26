from os import system
from os_checker import set_clear_command
from auxiliary_functions import check_if_int
from auxiliary_functions import check_if_float
from auxiliary_functions import check_if_valid_choice
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
                  f"[1] Switch to {self.switch_to_mode} operation\n"
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
                if self.operation_mode == "safe":
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
                system( CLEAR_COMMAND )
                self.products_next_index = self.build_dictionary_and_add(
                    [ "name", "price" ],
                    [ str, float ],
                    self.products_indexes,
                    self.products_content,
                    self.products_next_index
                )

                if self.operation_mode == "safe":
                    self.persist_orders_from_memory()
            
            elif user_input == 3:
                self.products_indexes, self.products_content, self.products_next_index =\
                self.change_content_and_up_index(
                    self.products_indexes,
                    self.products_content,
                    self.products_next_index,
                    "product"
                    )

                if self.operation_mode == "safe":
                    self.persist_products_from_memory()
            
            elif user_input == 4:
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
                if self.operation_mode == "safe":
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
                system( CLEAR_COMMAND )
                self.couriers_next_index = self.build_dictionary_and_add(
                    [ "name", "phone" ],
                    [ str, str ],
                    self.couriers_indexes,
                    self.couriers_content,
                    self.couriers_next_index
                )

                if self.operation_mode == "safe":
                    self.persist_orders_from_memory()
            
            elif user_input == 3:
                self.couriers_indexes, self.couriers_content, self.couriers_next_index =\
                    self.change_content_and_up_index(self.couriers_indexes,
                                                     self.couriers_content,
                                                     self.couriers_next_index,
                                                     "product"
                                                     )

                if self.operation_mode == "safe":
                    self.persist_couriers_from_memory()

            elif user_input == 4:
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
                if self.operation_mode == "safe":
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
                    [ str, str, str, int, str, list ],
                    self.orders_indexes,
                    self.orders_content,
                    self.orders_next_index
                )

                if self.operation_mode == "safe":
                    self.persist_orders_from_memory()
            
            elif user_input == 3:
                self.orders_content = self.change_content(self.orders_indexes, self.orders_content)

                if self.operation_mode == "safe":
                    self.persist_orders_from_memory()

            elif user_input == 4:
                self.orders_next_index = self.change_or_delete_element_in_lists(
                                                       config.ORDERS_FILE,
                                                       self.orders_indexes,
                                                       self.orders_content,
                                                       self.orders_next_index,
                                                       user_input
                                                      )
                if self.operation_mode == "safe":
                    self.persist_orders_from_memory()
            
            elif user_input == 5:
                self.search_order()

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
        self.switch_to_mode = "safe"

    def persist_products_from_memory( self ):
        
        persist_list_of_dictionaries(
                                config.PRODUCTS_FILE,
                                self.products_content
                                )
        write_new_indexes(
                            config.PRODUCTS_FILE,
                            self.products_next_index
                            )

    def persist_couriers_from_memory( self ):

        persist_list_of_dictionaries(
                                config.COURIERS_FILE,
                                self.couriers_content
                                )
        write_new_indexes(
                            config.COURIERS_FILE,
                            self.couriers_next_index
                            )

    def persist_orders_from_memory( self ):

        persist_list_of_dictionaries(
                                        config.ORDERS_FILE,
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
            self.switch_to_mode = "fast"

        else:
            self.operation_mode = "fast"
            self.switch_to_mode = "safe"
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
            return next_index

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
        new_dict = {"id": next_index}
        print(f"To go back input {BACK_CHAR}\n")
        for idx, data_type in enumerate(list_of_data_types):

            if list_of_keys[ idx ] == "courier":
                system( CLEAR_COMMAND )
                courier_number = self.choose_from_couriers()

                if courier_number == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    return next_index
                
                new_dict[ "courier" ] = courier_number

            elif list_of_keys[ idx ] == "list of products":
                system( CLEAR_COMMAND )
            
                list_of_products = self.choose_from_products()

                if list_of_products == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    return next_index
                
                new_dict[ list_of_keys[ idx ] ] = list_of_products

            elif list_of_keys[ idx ] == "status":
                new_dict[ "status" ] = "Preparing"

            elif "phone" in list_of_keys[ idx ]:
                system( CLEAR_COMMAND )
                phone_number = self.get_phone_number( list_of_keys[ idx ] )
                
                if phone_number == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    return next_index

                new_dict[ list_of_keys[idx] ] = phone_number

            elif data_type == str:
                system( CLEAR_COMMAND )

                expected_string = self.get_string_from_user( list_of_keys[idx] )

                if expected_string == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    return next_index

                new_dict[ list_of_keys[idx] ] = expected_string

            elif data_type == int or data_type == float:
                system( CLEAR_COMMAND )

                expected_number = self.get_number_of_same_type( data_type, list_of_keys[idx] )

                if expected_string == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    return next_index

                print()
                new_dict[ list_of_keys[idx] ] = expected_number
            
        if new_dict not in content:
            indexes.append(next_index)
            next_index += 1
            content.append(new_dict)
            system( CLEAR_COMMAND )
            print(f"{new_dict} added succesfully.\n")
            return next_index
        else:
            system( CLEAR_COMMAND )
            print(f"{new_dict} already exists.\n")
    
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

        system( CLEAR_COMMAND )
        while True:
            
            print("Please select which attribute you wish to change:\n")

            for keys_index in range(1, len( dict_keys )):
                print(f"[{keys_index}] {dict_keys[ keys_index ]}")

            user_input = input(f"\nTo go back input {BACK_CHAR}\n"
                                "Please select a choice: ")

            if user_input == BACK_CHAR:
                system( CLEAR_COMMAND )
                return dictionary_to_change

            user_input = check_if_int(user_input)
            user_input = check_if_valid_choice(user_input, range( 1, keys_index + 1 ))
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
            
            elif "phone" in key_at_index:
                dictionary_to_change = self.replace_phone_number_in_dict(dictionary_to_change, user_input)

            elif type_of_value_at_index == str:
                dictionary_to_change = self.replace_string_in_dictionary(dictionary_to_change, user_input)

            elif type_of_value_at_index == int or type_of_value_at_index == float:
                dictionary_to_change = self.replace_int_or_float_in_dict(dictionary_to_change, user_input)

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
        while True:

            print(f"The current order status is {dictionary_to_change['status']}\n")

            new_shipping_status = self.print_available_statuses_and_get_input()

            if new_shipping_status == BACK_CHAR:
                system( CLEAR_COMMAND )
                return dictionary_to_change

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

    def get_phone_number( self, key_word ):

        while True:

            phone_number = self.get_string_from_user( key_word )

            if phone_number == BACK_CHAR:
                system( CLEAR_COMMAND )
                return BACK_CHAR

            if phone_number.isnumeric() == True:
                return phone_number
            else:
                system( CLEAR_COMMAND )
                print("Please input only numbers.\n")
    
    def replace_string_in_dictionary( self, dictionary_to_change: dict, change_index: int) -> dict:
        system( CLEAR_COMMAND )

        key_at_index = list( dictionary_to_change.keys() )[ change_index ]
        value_at_index = list( dictionary_to_change.values() )[ change_index ]

        print(f"Current value is {value_at_index}\n")

        new_string = self.get_string_from_user( key_at_index )

        if new_string == BACK_CHAR:
            system( CLEAR_COMMAND )
            return dictionary_to_change
        print()

        if new_string != value_at_index:
            dictionary_to_change[ key_at_index ] = new_string
            system( CLEAR_COMMAND )
            print("Value changed sucessfully.\n")
            return dictionary_to_change
        else:
            system( CLEAR_COMMAND )
            print("The value inputted is the same as the one currently present.\n")

    def replace_int_or_float_in_dict( self, dictionary_to_change: dict, change_index: int ) -> dict:

        system( CLEAR_COMMAND )

        key_at_index = list( dictionary_to_change.keys() )[ change_index ]
        value_at_index = list( dictionary_to_change.values() )[ change_index ]
        type_of_value_at_index = type(value_at_index)
        
        print(f"Current value is {str(value_at_index)}\n")

        expected_number = self.get_number_of_same_type( type_of_value_at_index, key_at_index )

        if expected_number == BACK_CHAR:
            system( CLEAR_COMMAND )
            return dictionary_to_change

        if value_at_index != expected_number:
            dictionary_to_change[ key_at_index ] = expected_number
            system( CLEAR_COMMAND )
            print("Value changed sucessfully.\n")
            return dictionary_to_change
        else:
            system( CLEAR_COMMAND )
            print("The value inputted is the same as the one currently present.\n")
    
    def replace_phone_number_in_dict( self, dictionary_to_change: dict, change_index: int) -> dict:
        system( CLEAR_COMMAND )

        key_at_index = list( dictionary_to_change.keys() )[ change_index ]
        value_at_index = list( dictionary_to_change.values() )[ change_index ]

        print(f"Current value is {value_at_index}\n")

        new_phone_number = self.get_phone_number( value_at_index )

        if new_phone_number == BACK_CHAR:
            system( CLEAR_COMMAND )
            return dictionary_to_change
        print()

        if new_phone_number != value_at_index:
            dictionary_to_change[ key_at_index ] = new_phone_number
            system( CLEAR_COMMAND )
            print("Value changed sucessfully.\n")
            return dictionary_to_change
        else:
            system( CLEAR_COMMAND )
            print("The value inputted is the same as the one currently present.\n")

    def change_content_and_up_index( self,
                                     indexes: List,
                                     content: List,
                                     next_index: int,
                                     key_word: str
                                    ):
        system( CLEAR_COMMAND )
        
        self.print_all_items( indexes, content, key_word )
        item_to_replace_index = input(f"To go back input {BACK_CHAR}\n"
                                        f"Please enter the index you wish to change: ")
        
        if item_to_replace_index == BACK_CHAR:
            system( CLEAR_COMMAND )
            return indexes, content, next_index

        item_to_replace_index = check_if_int(item_to_replace_index)
        if item_to_replace_index in indexes:
            item_position_in_list = indexes.index(item_to_replace_index)
            old_dict = content[item_position_in_list].copy()
            new_dict = self.change_dictionary( content[item_position_in_list] )
            if new_dict != old_dict:
                new_dict["id"] = next_index
                next_index += 1
                indexes[item_position_in_list] = new_dict["id"]
                content[item_position_in_list] = new_dict
            return indexes, content, next_index
        else:
            system( CLEAR_COMMAND )
            print(f'\nThe number given for the {key_word} to replace does not exist or is not a number.\n')
            return indexes, content, next_index

    def change_content( self,
                        indexes,
                        content
                      ):
        system( CLEAR_COMMAND )
        self.print_all_items( indexes, content, "orders" )
        item_to_replace_index = input(f"To go back input {BACK_CHAR}\n"
                                        f"Please enter the index of the order you wish to change: ")
        
        if item_to_replace_index == BACK_CHAR:
            system( CLEAR_COMMAND )
            return content

        item_to_replace_index = check_if_int(item_to_replace_index)
        if item_to_replace_index in indexes:
            item_position_in_list = indexes.index(item_to_replace_index)
            dictionary_to_change = self.change_dictionary( content[item_position_in_list] )
            content[item_position_in_list] = dictionary_to_change
            return content
        else:
            system(clear_command)
            print(f'\nThe number given for the {key_word} to replace does not exist or is not a number.\n')
            return content

    def search_order( self ):
        system( CLEAR_COMMAND )

        while True:
            print("Please chose what you want to search by:\n\n"
                "[1] Courier\n"
                "[2] Status\n")

            user_input = input(f"To go back input {BACK_CHAR}\n"
                                "Choice: ")
            
            if user_input == BACK_CHAR:
                system( CLEAR_COMMAND )
                return
            
            user_input = check_if_int( user_input )
            user_input = check_if_valid_choice( user_input, [1,2])

            if user_input == -1:
                system( CLEAR_COMMAND )
                print("Invalid choice. Please provide a number as per the menu.\n")
            elif user_input == 1:
                system( CLEAR_COMMAND )
                user_input = self.choose_from_couriers()

                if user_input == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    return

                self.filter_order( user_input, "courier" )
            elif user_input == 2:
                system( CLEAR_COMMAND )
                user_input = self.print_available_statuses_and_get_input()

                if user_input == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    return

                self.filter_order( user_input, "status" )
    
    def filter_order( self, user_input, key: str):

        list_of_results = []
        for item in self.orders_content:
            if item[ key ] == user_input:
                list_of_results.append(item)
        
        if len(list_of_results) > 0:
            system( CLEAR_COMMAND )
            print("The below search results have been found:\n")

            for item in list_of_results:
                print(item)
            print()
        else:
            system( CLEAR_COMMAND )
            print("No matches found")
            return

    def print_available_statuses_and_get_input( self ):
        while True:
            with open("list_of_possible_statuses.txt") as f:

                lines = [x.replace("\n", "") for x in f.readlines()]

                print("The available statuses are as per the below:\n")

                for idx, status in enumerate(lines):
                    print(f"[{idx}] {status}")
                print()

                user_input = input(f"To go back input {BACK_CHAR}\n"
                                    "Please choose which status you would like to use: ")

                if user_input == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    return BACK_CHAR

                user_input = check_if_int(user_input)
                user_input = check_if_valid_choice(user_input, range(idx + 1))

                if user_input == -1:
                    system( CLEAR_COMMAND )
                    print("The given value is not a number or not in the list.\n")
                    continue
                else:
                    return lines[ user_input ]

start = App()