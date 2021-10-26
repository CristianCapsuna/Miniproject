from typing import List
import json
from os.path import getsize
import config
import csv


def persist_list_of_dictionaries(my_file:str, content: List):
    try:
        fieldnames = list( content[0].keys() )
    except IndexError:
        fieldnames = ""
    with open(my_file, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for dict_line in content:
            writer.writerow( dict_line )
         
def process_lines(csvfile) -> dict:
    reader = csv.DictReader(csvfile)

    content = []
    indexes = []
    for dict_item in reader:
        for key in dict_item.keys():
            if key == "id":
                dict_item[key] = int(dict_item[key])
                indexes.append(dict_item[key])
            elif key == "list of products":
                convert_to_list = list(dict_item[key].replace('[','').replace(']','').split(','))
                list_of_ints = [int(x) for x in convert_to_list]
                dict_item[key] = list_of_ints
            elif "phone" not in key:
                try:
                    dict_item[key] = int(dict_item[key])
                    continue
                except ValueError:
                    pass
                try:
                    dict_item[key] = float(dict_item[key])
                except ValueError:
                    pass

        content.append(dict_item)

    return indexes, content

def read_file(my_file:str) -> dict:
    try:
        with open(my_file, newline = "") as f:
            indexes, content = process_lines(f)
            return indexes, content
    except FileNotFoundError:
        return [], []

def get_current_index(key_word):
    current_indexes = load_indexes_csv()
    return current_indexes[f"current {key_word} index"]

def load_indexes_csv() -> dict:
    try:
        with open('Indexes.csv') as csvfile:
            _, current_indexes = process_lines(csvfile)
            current_indexes = current_indexes[0]
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
    persist_list_of_dictionaries("Indexes.csv", [current_indexes])
    return current_indexes

def check_file_for_max_index(my_file:str) -> int:
    try:
        with open(my_file, newline = "") as csvfile:
            indexes, _ = process_lines(csvfile)

            if len( indexes ) > 0:
                return ( max( indexes ) + 1 )
            else:
                return 1
    except FileNotFoundError: 
        return 1

def write_new_indexes(my_file:str, next_index):
    next_indexes = load_indexes_csv()
    if my_file == config.PRODUCTS_FILE:
        if next_index != None:
            next_indexes['current product index'] = next_index
    elif my_file == config.COURIERS_FILE:
        if next_index != None:
            next_indexes['current courier index'] = next_index
    elif my_file == config.ORDERS_FILE:
        if next_index != None:
            next_indexes['current order index'] = next_index
    persist_list_of_dictionaries("Indexes.csv", [next_indexes])