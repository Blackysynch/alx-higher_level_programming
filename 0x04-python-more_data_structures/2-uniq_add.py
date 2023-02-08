#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uniq = set(my_list)
    new_list = list(uniq)
    for i in new_list:
        sum += i
    return sum
