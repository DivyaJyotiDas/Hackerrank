"""
@algorithm:- Linear search.
@Time Complexity:- O(n)
@space Complexity:- O(1)

Step 1:- Take input from User and store it in array.
Step 2:- Traverse array from 0 to n-1
step 3:- On each element check if its exists ['a', 'e', 'i', 'o', 'u']
step 4:- construct a Dictionary.
step 5:- pick each elemnet and check if its exists in dictionary or not.
Step 6:- if not exist then add a key and count as 1.
step 7:- If exist then increase only value.

@pseudocode:-
step1: user_inp = list(input().split())
step2:- for(i in user_inp):
            if vowel_exists(i, vowel):
                if isKeyExists(i, vow_dict):
                    vow_dict[i] = 1
                else:
                    vow_dict[i] += 1

        def vowel_exists(i, vowel):
            for entry in vowel:
                if i.lower() == entry:
                    return True
                else:
                    False

        def isKeyExists(i, vow_dict):
            if i in vow_dict.keys():
                return True
            else:
                :return False

@Design:-

@TestCase:-
1. Worst Case:- 'aaaaaaaaaaaaaaaaaeeeeeeeeeeeeeeeeeeeeeeiiiiiiiiiiiiiiiiiiiiiiiiiiiooooooooooooooooooouuuuuuuuuuuuuuuuu'
2. Best Case:- ''
"""
import time

def vowel_exists(i, vowel):
    for entry in vowel:
        if i.lower() == entry:
            return True

    return False


def isKeyExists(i, vow_dict):
    if i in vow_dict.keys():
        return True
    return False

def split(inp):
    return [char for char in inp]


if __name__ == '__main__':
    user_inp = input()
    user_inp = split(user_inp)
    vowel = ['a', 'e', 'i', 'o', 'u']
    vow_dict = {}
    start = time.time()
    for i in user_inp:
        if vowel_exists(i, vowel):
            if isKeyExists(i, vow_dict):
                vow_dict[i] += 1
            else:
                vow_dict[i] = 1
    end = time.time()
    print("Execution Time:: ", end - start)
    print(vow_dict)
