# from ..main import *
# from unittest.mock import Mock, patch

# @patch("builtins.input")
# def test_validate_user_input(mock_input: Mock()):
    
#     # assemble
#     mock_list = [0,1,2]
#     mock_input.side_effect = 2
#     # expected = mock_input.side_effect
#     expected = 2

#     # act
#     actual = aux_fun.check_if_input_is_a_menu_option(mock_list)
    
#     # assert
#     assert actual == expected

# @patch("builtins.input")
# def test_check_if_input_is_a_menu_option_edge_case(mock_input: Mock()):
    
#     # assemble
#     mock_list = [0,1,2]
#     mock_input.side_effect = 3
#     expected = -1

#     # act
#     actual = aux_fun.check_if_input_is_a_menu_option(mock_list)
    
#     # assert
#     assert actual == expected

# @patch("builtins.input")
# def test_check_if_input_is_a_menu_option_corner_case(mock_input: Mock()):
    
#     # assemble
#     mock_list = [0,1,2]
#     mock_input.side_effect = "Pete"
#     expected = -1

#     # act
#     actual = aux_fun.check_if_input_is_a_menu_option(mock_list)
    
#     # assert
#     assert actual == expected