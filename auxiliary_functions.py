from typing import List

def check_if_input_is_a_menu_option(choices:List[int]) -> int:
    try:
        user_input = int(input("Please select a choice: "))
        print()
        if user_input not in(choices):
            return -1
        return user_input
    except ValueError:
        return -1