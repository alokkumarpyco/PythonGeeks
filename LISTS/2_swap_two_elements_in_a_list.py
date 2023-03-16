# https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list/
from copy import deepcopy
from typing import List


def swap_the_element_at_index(lst, index1, index2):
    lst = deepcopy(lst)
    size = len(lst)
    if index1 < size and index2 < size:
        lst[index1], lst[index2] = lst[index2], lst[index1]
        return lst
    return None


given_list = [12, 35, 9, 56, 24]

new_list = swap_the_element_at_index(given_list, 1, 3)

print(given_list)
print(new_list)


# Approach 5: Using enumerate
def swap_the_elements(lst: List, pos1, pos2) -> List:
    lst = deepcopy(lst)
    for index, value in enumerate(lst):
        if index == pos1:
            elem1 = value
        if index == pos2:
            elem2 = value
    lst[pos2] = elem1
    lst[pos1] = elem2
    return lst


List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
lst = swap_the_elements(List, pos1-1, pos2-1)
print(lst)