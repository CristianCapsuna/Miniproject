from os import system
from os_checker import set_clear_command
from auxiliary_functions import check_if_int
from auxiliary_functions import check_if_float
from auxiliary_functions import check_if_valid_choice
import config
from typing import List
from database_management import get_all_content
from database_management import execute_query
from database_management import get_index_of_last_entry
import pymysql
from decimal import Decimal

CLEAR_COMMAND = set_clear_command()
system( CLEAR_COMMAND )
BACK_CHAR = "`"

INAPPROPRIATE_MENU_CHOICE_STATEMENT = 'Inappropriate input. Please input a positive single digit number, as per the menu\n'

class App:
    
    def __init__( self ):
        
        while True:
            print(
                  "Main menu:\n\n"
                   "[1] Product menu\n"
                   "[2] Couriers menu\n"
                   "[3] Orders menu\n"
                 )
            
            user_input = input(
                               f"To quit input {BACK_CHAR}\n"
                                "Please select a choice: "
                              )
            if user_input == BACK_CHAR:
                system( CLEAR_COMMAND )
                exit()

            if user_input == "1":
                system( CLEAR_COMMAND )
                self.products_menu()
            elif user_input == "2":
                system( CLEAR_COMMAND )
                self.couriers_menu()
            elif user_input == "3":
                system( CLEAR_COMMAND )
                self.orders_menu()
            else:
                self.guide_user( INAPPROPRIATE_MENU_CHOICE_STATEMENT )

    
    def products_menu(self):

        while True:
            self.print_generic_menu( "product" )

            user_input = input(
                            f"To go back input {BACK_CHAR}\n"
                                "Please select a choice: "
                            )
            
            if user_input == BACK_CHAR:
                system( CLEAR_COMMAND )    
                break

            if user_input == "1":
                system( CLEAR_COMMAND )
                self.print_content( "products" )
            
            elif user_input == "2":
                system( CLEAR_COMMAND )
                new_dict = self.build_dictionary(
                                                [ "name", "price" ],
                                                [ str, float ],
                                                "products",
                                                )
                if new_dict == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    continue
                self.persist_products_or_couriers( new_dict, "products")

            elif user_input == "3":
                self.change_content( "products" )

            elif user_input == "4":
                self.delete_item( "products" )

            else:
                self.guide_user(INAPPROPRIATE_MENU_CHOICE_STATEMENT)
    
    def couriers_menu(self):

        while True:
            self.print_generic_menu( "courier" )

            user_input = input(
                               f"To go back input {BACK_CHAR}\n"
                                "Please select a choice: "
                              )
            
            if user_input == BACK_CHAR:
                system( CLEAR_COMMAND )            
                break

            if user_input == "1":
                system( CLEAR_COMMAND )
                self.print_content( "couriers" )
            
            elif user_input == "2":
                system( CLEAR_COMMAND )
                new_dict = self.build_dictionary(
                                                [ "name", "phone" ],
                                                [ str, str ],
                                                "couriers"
                                                )
                if new_dict == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    continue
                self.persist_products_or_couriers( new_dict, "couriers")

            elif user_input == "3":
                self.change_content( "couriers" )

            elif user_input == "4":
                self.delete_item( "couriers" )
                
            else:
                self.guide_user(INAPPROPRIATE_MENU_CHOICE_STATEMENT)
    
    def orders_menu(self):
        
        while True:
            self.print_generic_menu( "order" )

            user_input = input(
                               f"To go back input {BACK_CHAR}\n"
                                "Please select a choice: "
                              )
            
            if user_input == BACK_CHAR:
                system( CLEAR_COMMAND )
                break
            
            if user_input == "1":
                system( CLEAR_COMMAND )
                self.print_content( "orders" )
            
            elif user_input == "2":
                system( CLEAR_COMMAND )
                new_dict = self.build_dictionary(
                    [ "customer_name", "customer_address", "customer_phone", "courier", "status", "list_of_products" ],
                    [ str, str, str, int, str, list ],
                    "orders"
                )
                if new_dict == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    continue
                self.persist_orders( new_dict )

            elif user_input == "3":
                self.change_content( "orders" )

            elif user_input == "4":
                self.delete_item( "orders" )
            
            elif user_input == "5":
                self.search_order()

            else:
                self.guide_user(INAPPROPRIATE_MENU_CHOICE_STATEMENT)


    def persist_products_or_couriers( self, my_dict: dict, table_name: str ):
        
        keys = list( my_dict.keys() )
        values = list( my_dict.values() )

        column_names_string, values_string =\
            self.create_column_names_and_values_strings_for_use_in_query( keys, values )
        
        execute_query(f"INSERT INTO {table_name} ({column_names_string})"
                       f"VALUES ({values_string})")
        
        system( CLEAR_COMMAND )
        print(f"{table_name[:-1].replace(table_name[0],table_name[0].upper())} added succesfully.\n")

    def persist_orders( self, my_dict: dict ):
        
        list_of_keys = list( my_dict.keys() )
        list_of_values = list( my_dict.values() )

        keys = list_of_keys[:-1]
        values = list_of_values[:-1]

        product_values = list_of_values[-1]

        column_names_string, values_string =\
            self.create_column_names_and_values_strings_for_use_in_query( keys, values )
        
        execute_query(f"INSERT INTO orders ({column_names_string})"
                       f"VALUES ({values_string})")
        
        id_of_order = get_index_of_last_entry( "orders" )

        values_string = self.create_values_string_for_orders_map_insertion(
             id_of_order,
             product_values
             )
        execute_query(f"INSERT INTO orders_map (order_id, product_id) "
                                "VALUES " + values_string)
        
        print(f"Order added succesfully.\n")

    def guide_user( self, message: str ):
        system( CLEAR_COMMAND )
        print( message )
    
    def print_generic_menu( self, key_word: str):
        print(
              f"{key_word.replace(key_word[0],key_word[0].upper())} menu:\n\n"
              f"[1] Print {key_word} list\n"
              f"[2] Add new {key_word}\n"
              f"[3] Amend existing {key_word}\n"
              f"[4] Delete {key_word}\n"
               )

    def print_content( self, table_name: str , content: dict = None):

        if content == None:
            content = get_all_content(table_name)

        if table_name == "orders":
                content = self.create_list_of_products(content)        

        if len( content ) > 0:
            keys = list( content[0].keys() )            
            self.print_line_with_nice_spacing(keys)
            print("-" * 20 * len(keys))
            for my_dict in content:
                values = list( my_dict.values() )
                self.print_line_with_nice_spacing(values)
            print()

        else:
            system( CLEAR_COMMAND )
            print( f'The {table_name} list is empty\n' )
    
        return content

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

    def print_content_and_get_single_id_to_change( self, table_name: str ):
        content = None
        while True:
            content = self.print_content( table_name , content)
            id_to_change = input( 
                f"To quit input {BACK_CHAR}\n"
                "Please enter the index you wish to change: "
                )

            if id_to_change == BACK_CHAR:
                system( CLEAR_COMMAND )
                return BACK_CHAR, BACK_CHAR

            id_to_change = check_if_int(id_to_change)

            if len(content) > 0:
                keys = list( content[0].keys() )
                indexes = []
                for item in content:
                    indexes.append(item[keys[0]])
                print()

                if id_to_change in indexes:
                    return id_to_change, content
                else:
                    system( CLEAR_COMMAND )
                    print("The value given is either not a number or not in the list.\n")
                    continue
            else:
                pass

    def print_content_and_get_multiple_ids_to_add( self, table_name: str ):
        content = None
        while True:
            content = self.print_content( table_name , content)
            ids_to_change = input( 
                f"To quit input {BACK_CHAR}\n"
                "Please enter the index you wish to change: "
                )

            if ids_to_change == BACK_CHAR:
                system( CLEAR_COMMAND )
                return BACK_CHAR, BACK_CHAR

            if len(content) > 0:
                try:
                    list_of_inputs = [int(x) for x in ids_to_change.split(",")]
                    return list_of_inputs, content
                except ValueError:
                    system( CLEAR_COMMAND )
                    print("Incorrect input. Only one number or multiple numbers separated by commas are allowed.\n")
                    continue
            else:
                pass

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
    
    def delete_item( self, table_name: str ):
        system( CLEAR_COMMAND )
        id_to_change, content = self.print_content_and_get_single_id_to_change( table_name )
        
        if len(content) == 0:
            system(CLEAR_COMMAND)
            print(f"The product list is empty\n")
            return

        if id_to_change == BACK_CHAR:
            system( CLEAR_COMMAND )
            return
        
        keys = list( content[0].keys() )

        if table_name == "orders":
            execute_query(f"DELETE FROM orders_map WHERE order_id = {id_to_change}")
        execute_query(f"DELETE FROM {table_name} WHERE {keys[0]} = {id_to_change}")

        system( CLEAR_COMMAND )
        print(f"ID {id_to_change} has been deleted.\n")
    
    def build_dictionary(
                         self,
                         list_of_keys: List,
                         list_of_data_types: List,
                         table_name: str
                         ):

        new_dict = {}
        print(f"To go back input {BACK_CHAR}\n")
        for idx, data_type in enumerate(list_of_data_types):

            if list_of_keys[ idx ] == "courier":
                system( CLEAR_COMMAND )
                courier_number = self.choose_from_couriers()

                if courier_number == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    return BACK_CHAR
                
                new_dict[ "courier" ] = courier_number

            elif list_of_keys[ idx ] == "list_of_products":
                system( CLEAR_COMMAND )
            
                list_of_products = self.choose_from_products()

                if list_of_products == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    return BACK_CHAR
                
                new_dict[ list_of_keys[ idx ] ] = list_of_products

            elif list_of_keys[ idx ] == "status":
                new_dict[ "status" ] = "Preparing"

            elif "phone" in list_of_keys[ idx ]:
                system( CLEAR_COMMAND )
                phone_number = self.get_phone_number( list_of_keys[ idx ] )
                
                if phone_number == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    return BACK_CHAR

                new_dict[ list_of_keys[idx] ] = phone_number

            elif data_type == str:
                system( CLEAR_COMMAND )

                expected_string = self.get_string_from_user( list_of_keys[idx] )

                if expected_string == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    return BACK_CHAR

                new_dict[ list_of_keys[idx] ] = expected_string

            elif data_type == int or data_type == float:
                system( CLEAR_COMMAND )

                expected_number = self.get_number_of_same_type( data_type, list_of_keys[idx] )

                if expected_string == BACK_CHAR:
                    system( CLEAR_COMMAND )
                    return BACK_CHAR

                print()
                new_dict[ list_of_keys[idx] ] = expected_number
            
        return new_dict
    
    def choose_from_couriers( self ):

        while True:
            user_input, content = self.print_content_and_get_single_id_to_change( "couriers")

            if user_input == BACK_CHAR:
                return BACK_CHAR

            user_input = check_if_int(user_input)
            indexes = [x["courier_id"] for x in content]
            if user_input in [x["courier_id"] for x in content]:
                return user_input
            else:
                system( CLEAR_COMMAND )
                print("\nPlease input a valid number corresponding to one of the couriers.\n")
    
    def choose_from_products( self ):

        while True:
            list_of_inputs, content = self.print_content_and_get_multiple_ids_to_add( "products" )

            if list_of_inputs == BACK_CHAR:
                return BACK_CHAR

            choices_which_exist, choices_which_dont_exist = [], []

            for choice in list_of_inputs:

                if choice in [x["product_id"] for x in content]:
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
                return choices_which_exist
            else:
                system( CLEAR_COMMAND )
                print(f"Items {choices_which_exist} have been added.\n")
                return choices_which_exist
    
    def change_dictionary( self, item_to_change_index: int, table_name: str):

        system( CLEAR_COMMAND )
        while True:
            new_content = get_all_content( table_name )
            dict_keys = list(new_content[0].keys())
            for item in new_content:
                if item[dict_keys[0]] == item_to_change_index:
                    dictionary_to_change = item
            dict_values = list(dictionary_to_change.values())
            
            print("Please select which attribute you wish to change:\n")

            for keys_index in range(1, len( dict_keys )):
                print(f"[{keys_index}] {dict_keys[ keys_index ]}")

            user_input = input(f"\nTo go back input {BACK_CHAR}\n"
                                "Please select a choice: ")

            if user_input == BACK_CHAR:
                system( CLEAR_COMMAND )
                return BACK_CHAR

            user_input = self.validate_user_input( user_input, range( 1, keys_index + 1 ))
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
                self.change_courier( dictionary_to_change, item_to_change_index )

            elif key_at_index == "list_of_products":
                self.change_list_of_products( dictionary_to_change, item_to_change_index )

            elif key_at_index == "status":
                self.change_status( dictionary_to_change, item_to_change_index )
            
            elif "phone" in key_at_index:
                self.replace_phone_number_in_dict( dictionary_to_change,
                                                   item_to_change_index,
                                                   key_at_index,
                                                   table_name )

            elif type_of_value_at_index == str:
                self.replace_string_in_dictionary( dictionary_to_change,
                                                   item_to_change_index,
                                                   key_at_index,
                                                   table_name )

            elif type_of_value_at_index == int or type_of_value_at_index == Decimal:
                self.replace_int_or_float_in_dict(dictionary_to_change,
                                                  item_to_change_index,
                                                  key_at_index,
                                                  table_name )

        return 1

    def change_courier( self, dictionary_to_change: dict, item_to_change_index: int ):
        system( CLEAR_COMMAND )
        while True:
            print(f"Courier currently being used is ID {str(dictionary_to_change['courier'])}\n")
            courier_number = self.choose_from_couriers()

            if courier_number == BACK_CHAR:
                system( CLEAR_COMMAND )
                return

            current_courier_number = dictionary_to_change["courier"]
            if courier_number != current_courier_number:
                execute_query("UPDATE orders " 
                              f"SET courier = {courier_number} "
                              f"WHERE order_id = {item_to_change_index};")
                system( CLEAR_COMMAND )
                print("Courier changed succesfully\n")
                return
            else:
                system( CLEAR_COMMAND )
                print("The new value provided is the same as the value currently present\n")
        
    def change_list_of_products ( self, dictionary_to_change: dict, order_id: int ):
        system( CLEAR_COMMAND )
        while True:
            print(f"IDs of products currently in the list {str(dictionary_to_change['list_of_products'])}\n")
            list_of_products = self.choose_from_products()

            if list_of_products == BACK_CHAR:
                system( CLEAR_COMMAND )
                return dictionary_to_change

            current_list_of_products = dictionary_to_change[ "list_of_products" ]
            are_identical = True
            for idx in range( len( current_list_of_products ) ):

                if current_list_of_products[idx] != dictionary_to_change["list_of_products"][idx]:
                    are_identical = False
                    break

            if are_identical != False:
                
                execute_query(f"DELETE FROM orders_map WHERE order_id = {order_id}")
                values_string = self.create_values_string_for_orders_map_insertion(
                    order_id,
                    list_of_products
                    )
                
                execute_query(f"INSERT INTO orders_map (order_id, product_id) "
                                "VALUES " + values_string)
                system( CLEAR_COMMAND )
                print("list_of_products changed succesfully\n")
                return dictionary_to_change
            else:
                system( CLEAR_COMMAND )
                print("The new value provided is the same as the value currently present\n")
    
    def change_status( self, dictionary_to_change: dict, item_to_change_index ):
        system( CLEAR_COMMAND )
        while True:

            print(f"The current order status is {dictionary_to_change['status']}\n")

            new_shipping_status = self.print_available_statuses_and_get_input()

            if new_shipping_status == BACK_CHAR:
                system( CLEAR_COMMAND )
                return dictionary_to_change

            if new_shipping_status != dictionary_to_change["status"]:
                execute_query("UPDATE orders " 
                              f"SET status = {new_shipping_status} "
                              f"WHERE order_id = {item_to_change_index};")
                system( CLEAR_COMMAND )
                print("Status changed succesfully\n")
                return
            else:
                system( CLEAR_COMMAND )
                print("The new status provided is the same as the existing one\n")
    
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

            if len(phone_number) > 15:
                system( CLEAR_COMMAND )
                print("Maximum length of input is 15 characters.\n")
            elif phone_number.isnumeric() == True:
                return phone_number
            else:
                system( CLEAR_COMMAND )
                print("Please input only numbers.\n")
    
    def replace_string_in_dictionary( self,
                                      dictionary_to_change: dict,
                                      item_to_change_index: int,
                                      key_at_index: str,
                                      table_name: str ):
        system( CLEAR_COMMAND )

        value_at_index = dictionary_to_change[ key_at_index ]
        print(f"Current value is {value_at_index}\n")

        new_string = self.get_string_from_user( key_at_index )

        if new_string == BACK_CHAR:
            system( CLEAR_COMMAND )
            return
        print()

        if new_string != value_at_index:
            key_of_id = list( dictionary_to_change.keys() )[0]
            execute_query(f"UPDATE {table_name} " 
                         f"SET {key_at_index} = '{new_string}' "
                         f"WHERE {key_of_id} = {item_to_change_index};")
            system( CLEAR_COMMAND )
            print("Value changed sucessfully.\n")
            return
        else:
            system( CLEAR_COMMAND )
            print("The value inputted is the same as the one currently present.\n")

    def replace_int_or_float_in_dict( self,
                                      dictionary_to_change: dict,
                                      item_to_change_index: int,
                                      key_at_index: str,
                                      table_name: str ):

        system( CLEAR_COMMAND )

        value_at_index = dictionary_to_change[ key_at_index ]
        type_of_value_at_index = type(value_at_index)
        
        print(f"Current value is {str(value_at_index)}\n")

        expected_number = self.get_number_of_same_type( type_of_value_at_index, key_at_index )

        if expected_number == BACK_CHAR:
            system( CLEAR_COMMAND )
            return

        if value_at_index != expected_number:
            key_of_id = list( dictionary_to_change.keys() )[0]
            execute_query(f"UPDATE {table_name} " 
                         f"SET {key_at_index} = '{expected_number}' "
                         f"WHERE {key_of_id} = {item_to_change_index};")
            system( CLEAR_COMMAND )
            print("Value changed sucessfully.\n")
            return
        else:
            system( CLEAR_COMMAND )
            print("The value inputted is the same as the one currently present.\n")
    
    def replace_phone_number_in_dict( self,
                                      dictionary_to_change: dict,
                                      item_to_change_index: int,
                                      key_at_index: str,
                                      table_name: str ):
        system( CLEAR_COMMAND )

        value_at_index = dictionary_to_change[ key_at_index ]

        print(f"Current value is {value_at_index}\n")

        new_phone_number = self.get_phone_number( value_at_index )

        if new_phone_number == BACK_CHAR:
            system( CLEAR_COMMAND )
            return
        print()

        if new_phone_number != value_at_index:
            key_of_id = list( dictionary_to_change.keys() )[0]
            execute_query(f"UPDATE {table_name} " 
                         f"SET {key_at_index} = '{new_phone_number}' "
                         f"WHERE {key_of_id} = {item_to_change_index};")
            system( CLEAR_COMMAND )
            print("Value changed sucessfully.\n")
            return
        else:
            system( CLEAR_COMMAND )
            print("The value inputted is the same as the one currently present.\n")

    def change_content( self,
                        table_name: str
                      ):
        system( CLEAR_COMMAND )

        while True:
            item_to_change_index, content = self.print_content_and_get_single_id_to_change (table_name)
            if table_name == "orders":
                content = self.create_list_of_products(content)
            
            if item_to_change_index == BACK_CHAR:
                system( CLEAR_COMMAND )
                return

            item_to_change_index = check_if_int(item_to_change_index)
            maybe_back = self.change_dictionary( item_to_change_index, table_name )
            if maybe_back == BACK_CHAR:
                return

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
            
            user_input = self.validate_user_input( user_input, [1,2])

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

                user_input = self.validate_user_input( user_input, range( idx + 1 ) )

                if user_input == -1:
                    system( CLEAR_COMMAND )
                    print("The given value is not a number or not in the list.\n")
                    continue
                else:
                    return lines[ user_input ]

    def print_line_with_nice_spacing( self, list_of_items: List):
        space_until_next = 20
        start_string = ""
        for item in list_of_items:
            item = str(item)
            start_string += item
            start_string += " " * (20 - len(item))
        print( start_string )
    
    def create_column_names_and_values_strings_for_use_in_query( self,
                                                                 keys: List,
                                                                 values: List):
        column_names_string = ""

        for key in keys:
            column_names_string += key + ", "
        
        column_names_string = column_names_string[:-2]

        values_string = ""

        for value in values:
            if type(value) == str:
                value = f"'{value}'"
            values_string += str(value) + ", "

        values_string = values_string[:-2]

        return column_names_string, values_string

    def create_list_of_products( self, orders_content: dict ):
        orders_map_content = get_all_content( "orders_map" )
        list_of_ids = []
        for element in orders_map_content:
            if element["order_id"] not in list_of_ids:
                list_of_ids.append(element["order_id"])
        
        list_of_lists_of_products = []

        for id_number in list_of_ids:
            temp_list = [id_number, []]
            for element in orders_map_content:
                if element["order_id"] == id_number:
                    temp_list[1].append(element["product_id"])
            list_of_lists_of_products.append(temp_list)
        
        for order in orders_content:
            for list_of_products in list_of_lists_of_products:
                if order["order_id"] == list_of_products[0]:
                    order["list_of_products"] = list_of_products[1]
                    break
        
        return orders_content
    
    def create_values_string_for_orders_map_insertion( self, order_id: int, list_of_products: List):
        values_string = ""
        for product in list_of_products:
            values_string += f"({str(order_id)}, {str(product)}),"
        values_string = values_string[:-1] + ";"

        return values_string

start = App()