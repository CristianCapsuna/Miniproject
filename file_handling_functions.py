from typing import List
import json
from os.path import getsize
import config

def persist_list_of_strings(my_file:str, indexes: List, content: List):
    with open(my_file, 'w') as f:
        f.write( str( indexes[0] ) + ',' + str( content[0] ) )
        for idx in range( 1, len( content ) ):
            f.write('\n' + str( indexes[idx] ) + ',' + str( content[idx] ) )
    
def persist_list_of_dictionaries(my_file:str, indexes: List, content: List):
    with open(my_file, 'w') as f:
        f.write( str( indexes[0] ) + ',' + json.dumps( content[0] ) )
        for idx in range( 1, len( content ) ):
            f.write('\n' + str( indexes[idx] ) + ',' + json.dumps( content[idx] ) )
         
def process_lines(f) -> dict:
    try:
        lines = f.readlines()
        json.loads(lines[0].replace('\n','').split(',', maxsplit = 1)[1])
        my_operation = return_dict_of_input
    except:
        my_operation = just_return
    indexes = []
    content = []
    for line in lines:
        split_line = line.replace('\n','').split(',', maxsplit = 1)
        index = int(split_line[0])
        line_content = my_operation(split_line[1])
        indexes.append(index)
        content.append(line_content)
    return indexes, content

def read_file(my_file:str) -> dict:
    try:
        with open(my_file) as f:
            indexes, content = process_lines(f)
            return indexes, content
    except FileNotFoundError:
        return [], []

def get_current_index(key_word):
    current_indexes = load_indexes_json()
    return current_indexes[f"current {key_word} index"]

def load_indexes_json() -> dict:
    try:
        with open('Indexes.json') as f:
            current_indexes = json.load(f)
    except FileNotFoundError:
        current_indexes = create_initial_index_file_and_return_as_dict()
    return current_indexes

def create_initial_index_file_and_return_as_dict():
    current_product_index = check_file_for_max_index(config.PRODUCTS_FILE)
    current_courier_index = check_file_for_max_index(config.COURIERS_FILE)
    current_order_index = check_file_for_max_index(config.ORDERS_FILE)
    current_indexes = {"current product index": current_product_index,
                    "current courier index": current_courier_index,
                    "current order index": current_order_index
    }
    with open('Indexes.json', 'w') as f:
        json.dump(current_indexes, f)
    return current_indexes

def check_file_for_max_index(my_file:str) -> int:
    try:
        with open(my_file) as f:
            indexes, content = process_lines(f)

            if len( indexes ) > 0:
                return ( max( indexes ) + 1 )
            else:
                return 1
    except FileNotFoundError: 
        return 1

def write_new_indexes(my_file:str, next_index):
    next_indexes = load_indexes_json()
    if my_file == config.PRODUCTS_FILE:
        next_indexes['current product index'] = next_index
    elif my_file == config.COURIERS_FILE:
        next_indexes['current courier index'] = next_index
    elif my_file == config.ORDERS_FILE:
        next_indexes['current order index'] = next_index
    with open("Indexes.json", "w") as f:
        json.dump(next_indexes, f)

def just_return(my_input:str) -> str:
    return my_input

def return_dict_of_input(my_input: str) -> dict:
    return json.loads(my_input)

# file_content = return_file_string_content_in_a_list('test.txt')
# print(file_content)