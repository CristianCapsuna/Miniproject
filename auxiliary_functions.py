from typing import List

def check_if_input_is_a_menu_option(choices:List[int]) -> int:
    try:
        user_input = int(input("Please select a choice: "))
        print('')
        if user_input not in(choices):
            return -1
        return user_input
    except ValueError:
        return -1

def write_to_file(file:str, file_content:List[str] = [], write_mode:str = 'complete', product_to_add:str = ''):
    if write_mode == 'complete':
        f = open(file, 'w')
        if len(file_content) > 0:
            f.write(file_content[0])
            for x in range(1, len(file_content)):
                f.write('\n' + file_content[x])
        f.close()
    elif write_mode == 'append':
        f = open(file, 'a')
        if len(file_content) != 0:
            f.write('\n')
        f.write(product_to_add)
        f.close()

def check_if_file_exists_and_load_content(file:str) -> List:
    try:
        f = open(file)
        file_content = [x.replace('\n','') for x in f.readlines()]
        f.close()
        return file_content
    except (NameError, FileNotFoundError):
        return []