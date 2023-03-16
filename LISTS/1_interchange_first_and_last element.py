# https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-list/
from typing import List
from copy import deepcopy

#
# given_list = [12, 35, 9, 56, 24]
# print(given_list)
# length = len(given_list)
# first_element = given_list[0]
# last_element = given_list[-1]
#
# given_list[0] = last_element
# given_list[-1] = first_element
#
# print(given_list)

given_list = [12, 35, 9, 56, 24]


def swap_list_element(lst: List) -> List:
    lst = deepcopy(lst)
    temp = lst[0]
    size = len(lst)
    lst[0] = lst[size - 1]
    lst[size - 1] = temp
    return lst


new_list = swap_list_element(given_list)
print(new_list)
print(given_list)

assert new_list[0] == given_list[-1]
assert new_list[-1] == given_list[0]


def swap_list_element_2(lst: List) -> List:
    lst = deepcopy(lst)
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


new_list = swap_list_element_2(given_list)
print(new_list)
print(given_list)

assert new_list[0] == given_list[-1]
assert new_list[-1] == given_list[0]
