from typing import List
from file_handling_functions import read_file
from os import system

def check_if_int(user_input) -> int:
    try:
        my_int = int(user_input)
        return my_int
    except ValueError:
        return -1

def check_if_float(user_input) -> float:
    try:
        my_float = float(user_input)
        return my_float
    except ValueError:
        return -1

def check_if_valid_choice(user_input, choices:List[int]) -> int:
    if user_input in choices:
        return user_input
    else:
        return -1