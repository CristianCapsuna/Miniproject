from typing import List
import json
from os.path import getsize

def write_to_file(my_file:str, file_content:dict, next_index:int):
    content_length = len(file_content["content"])
    if content_length > 0:
        with open(my_file, 'w') as f:
            f.write(str(file_content["indexes"][0]) + ', ' + str(file_content["content"][0]))
            for idx in range(1, content_length):
                f.write('\n' + str(file_content["indexes"][idx]) + ', ' + str(file_content["content"][idx]))
    write_new_indexes(my_file, next_index)
    

# def append_to_file(my_file:str, dict_of_additions:dict):
#     try:
#         my_file_size = getsize(my_file)
#     except FileNotFoundError:
#         my_file_size = 0
#     with open(my_file, 'a') as f:
#         if my_file_size > 0:
#             f.write('\n' + str(dict_of_additions["indexes"][0]) + ', ' + str(dict_of_additions["content"][0]))
#         else:
#             f.write(str(dict_of_additions["indexes"][0]) + ', ' + str(dict_of_additions["content"][0]))
#         if len(dict_of_additions["content"]) > 1:
#             for idx in range(1, len(dict_of_additions["content"])):
#                 f.write(str(dict_of_additions["indexes"][idx]) + ', ' + str(dict_of_additions["content"][idx]))
#     write_new_indexes(my_file, 'increment')
          
def process_lines(f) -> dict:
    try:
        lines = f.readlines()
        json.loads(lines[0].replace('\n','').split(', ', maxsplit = 1)[1])
        my_operation = return_dict_of_input
    except:
        my_operation = just_return
    file_content = {"indexes":[], "content":[]}
    for line in lines:
        split_line = line.replace('\n','').split(', ', maxsplit = 1)
        index = int(split_line[0])
        line_content = my_operation(split_line[1])
        file_content["indexes"].append(index)
        file_content["content"].append(line_content)
    return file_content

def read_file(my_file:str) -> dict:
    try:
        with open(my_file) as f:
            file_content = process_lines(f)
            return file_content
    except FileNotFoundError:
        return {"indexes":[], "content":[]}

def load_indexes_json() -> dict:
    try:
        with open('Indexes.json') as f:
            next_indexes = json.load(f)
    except FileNotFoundError:
        next_product_index = check_file_for_max_index('Products.txt')
        next_courier_index = check_file_for_max_index('Couriers.txt')
        next_order_index = check_file_for_max_index('Orders.txt')
        next_indexes = {"next product index": next_product_index,
                        "next courier index": next_courier_index,
                        "next order index": next_order_index
        }
        with open('Indexes.json', 'w') as f:
            json.dump(next_indexes, f)
    return next_indexes

def get_specific_index(my_file):
    next_indexes = load_indexes_json()
    
    if my_file == "Products.txt":
        return next_indexes["next product index"]
    elif my_file == "Couriers.txt":
        return next_indexes["next courier index"]
    elif my_file == "Orders.txt":
        return next_indexes["next order index"]

def check_file_for_max_index(my_file:str) -> int:
    try:
        with open(my_file) as f:
            file_content = process_lines(f)
            if len(file_content["indexes"]) > 0:
                return (max(file_content["indexes"]) + 1)
            else:
                return 1
    except FileNotFoundError: 
        return 1

def write_new_indexes(my_file:str, next_index):
    next_indexes = load_indexes_json()
    if my_file == "Products.txt":
        next_indexes['next product index'] = next_index
    elif my_file == "Couriers.txt":
        next_indexes['next courier index'] = next_index
    else:
        next_indexes['next order index'] = next_index
    with open("Indexes.json", "w") as f:
        json.dump(next_indexes, f)

def just_return(my_input:str) -> str:
    return my_input

def return_dict_of_input(my_input: str) -> dict:
    return json.loads(my_input)

# file_content = return_file_string_content_in_a_list('test.txt')
# print(file_content)