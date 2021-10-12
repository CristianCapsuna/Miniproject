from typing import List
import json

def check_if_input_is_a_menu_option(choices:List[int]) -> int:
    try:
        user_input = int(input("Please select a choice: "))
        print('')
        if user_input not in(choices):
            return -1
        return user_input
    except ValueError:
        return -1

def write_to_file(file:str, file_content:List[str] = [], product_to_add:str = ''):
    with open(file, 'w') as f:
        if len(file_content) > 0:
            f.write(file_content[0])
            for x in range(1, len(file_content)):
                f.write('\n' + file_content[x])

def append_to_file(file:str, file_content:List[str] = [], product_to_add:str = ''):
    with open(file, 'a') as f:
        if len(file_content) != 0:
            f.write('\n')
        f.write(product_to_add)

def check_if_file_exists_and_load_content(file:str) -> List:
    try:
        with open(file) as f:
            if file != 'Orders.txt':
                file_content = [x.replace('\n','') for x in f.readlines()]
            else:
                file_content = [json.loads(x) for x in f.readlines()]
        return file_content
    except (NameError, FileNotFoundError):
        return []

file_content = check_if_file_exists_and_load_content('Orders.txt')

for element in file_content:
    test = list(element.values())[0]
    print(type(test))