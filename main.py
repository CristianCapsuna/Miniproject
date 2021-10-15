from os import system
from os_checker import clear_command
from products_and_couriers_menu import *
from orders_menu import *
from auxiliary_functions import check_if_input_is_a_menu_option
from file_handling_functions import write_to_file

clear_command = clear_command()
system(clear_command)

class App:
    
    def __init__(self):
        self.operation_mode = 'fast'
        while True:
            print(f'Main menu:\n\
[0] Quit\n\
[1] Switch to {self.operation_mode} operation\n\
[2] Product menu\n\
[3] Couriers menu\n\
[4] Orders menu\n')
            
            user_input = check_if_input_is_a_menu_option([0, 1, 2, 3, 4])

            if user_input == -1:
                system(clear_command)
                print('Inappropriate input. Please input a positive single digit number, as per the menu\n')
            elif user_input == 0:
                if self.operation_mode == 'fast':
                    if 'products_file_content' in locals():
                        write_to_file('Products.txt', products_file_content, next_index)
                    if 'couriers_file_content' in locals():
                        write_to_file('Couriers.txt', couriers_file_content, next_index)
                exit()
            elif user_input == 1:
                if self.operation_mode == 'fast':
                    self.operation_mode = 'safe'
                elif self.operation_mode == 'safe':
                    self.operation_mode = 'fast'
                system(clear_command)
            elif user_input == 2:
                system(clear_command)
                products_file_content, next_index = products_and_couriers_menu(clear_command, 'products', self.operation_mode)
            elif user_input == 3:
                system(clear_command)
                couriers_file_content, next_index = products_and_couriers_menu(clear_command, 'couriers', self.operation_mode)
            elif user_input == 4:
                system(clear_command)
                couriers_file_content, next_index = orders_menu(clear_command, 'orders', self.operation_mode)

initiate = App()