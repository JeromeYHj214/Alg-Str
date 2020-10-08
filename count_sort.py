# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def count_sort(li,max_count=10):
    count = [0 for i in range(max_count+1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)

import random
li = [random.randint(0,20) for i in range(30)]
print(li)
count_sort(li,20)
print(li)