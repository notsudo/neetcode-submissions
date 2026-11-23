from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    new_list = []
    
    for sub_list in nested_arr:
        max_ele = sub_list[0]
        for element in sub_list:
            max_ele = max(max_ele,element)
        new_list.append(max_ele)
    return new_list


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
