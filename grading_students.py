'''
    1. if the grade is less than 38... Dont round up.
    2. If the grade is >=38
        2.1 if round(grade) - grade < 3 then round to the next multiple of 5
        2.2 if round(grade) - grade > 3 then dont round
        2.3 if round(grade) - grade == 3 then round to the next multiple of 5

@Algorithm:-
    1. store numbers in list.
    2. iterate over each element
'''

#!/bin/python3

import os
import math


def next_multiple(num):
    return math.ceil(num / 5) * 5

def gradingStudents(grades):
    new_grades = []
    for i in grades:
        if i < 38:
            new_grades.append(i)
        elif i >= 38 and ((next_multiple(i) - i) < 3):
            new_grades.append(next_multiple(i))
        elif i >= 38 and ((next_multiple(i) - i) >= 3):
            new_grades.append(i)
    return  new_grades


if __name__ == '__main__':
    n = int(input())
    grades = []
    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)
    for i in result:
        print(i)
