from typing import List
from file_handling_functions import read_file
from os import system

def check_if_int(user_input) -> int:
    try:
        my_int = int(user_input)
        return my_int
    except ValueError:
        return -1

def check_if_valid_choice(user_input, choices:List[int]) -> int:
    if user_input in choices:
        return user_input
    else:
        return -1

def get_courier_input(clear_command, customer_name = None, customer_address = None, customer_phone = None):
    list_of_couriers = read_file("Couriers.txt")
    while True:
        print("\nList of available couriers:\n")
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
            if customer_name !=  None:
                print(f"Customer name given: {customer_name}\n\
Customer address given: {customer_address}\n\
Customer phone number given: {customer_phone}\n\n")
            print("Please input a valid number corresponding to one of the couriers.\n")
    
    return courier_number

def get_new_value(key_word, file_content, product_to_replace_index, clear_command):
    while True:
        new_value = input(f"Please provide the new {key_word}: ")
        print()
        if new_value.lower() not in [file_content["content"][file_content["indexes"].index(product_to_replace_index)][key_word.replace(' ', '_')].lower()]:
            file_content["content"][file_content["indexes"].index(product_to_replace_index)][key_word.replace(' ', '_')] = new_value
            break
        else:
            system(clear_command)
            print("The new value provided is the same as the value currently present. Please input another\n")
            
    return file_content