from os import system
from os_checker import clear_command
from edit_menu import edit_menu
from auxiliary_functions import check_if_input_is_a_menu_option, write_to_file

clear_command = clear_command()
system(clear_command)

class App:
    def __init__(self):
        self.operation_mode = 'fast'
        while True:
            if self.operation_mode == 'fast':
                print('Main menu:\n\
[0] Quit\n\
[1] Product menu\n\
[2] Couriers menu\n\
[3] Switch to safe operation\n')
            elif self.operation_mode == 'safe':
                print('Main menu:\n\
[0] Quit\n\
[1] Product menu\n\
[2] Couriers menu\n\
[3] Switch to fast operation\n')
            
            user_input = check_if_input_is_a_menu_option([0, 1, 2, 3])

            if user_input == -1:
                system(clear_command)
                print('Inappropriate input. Please input a pozitive single digit number, as per the menu\n')
            elif user_input == 0:
                if self.operation_mode == 'fast':
                    if 'products_file_content' in locals():
                        write_to_file('Products.txt', products_file_content)
                    if 'curiers_file_content' in locals():
                        write_to_file('Curiers.txt', curiers_file_content)
                exit()
            elif user_input == 1:
                system(clear_command)
                products_file_content = edit_menu(clear_command, 'products', self.operation_mode)
            elif user_input == 2:
                system(clear_command)
                curiers_file_content = edit_menu(clear_command, 'curiers', self.operation_mode)
            elif user_input == 3:
                if self.operation_mode == 'fast':
                    self.operation_mode = 'safe'
                elif self.operation_mode == 'safe':
                    self.operation_mode = 'fast'
                system(clear_command)

initiate = App()