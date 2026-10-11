from typing import List

def read_integers() -> List[int]:
    
    read_ = input()
    read_list = read_.split(',')
    lists = []
    for r in read_list:
        lists.append(int(r))

    return lists

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
