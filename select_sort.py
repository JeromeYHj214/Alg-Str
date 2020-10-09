# -*- coding: utf-8 -*-
"""
选择排序
"""
from cal_time import *

@cal_time
def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    print(li_new)
    return li_new

@cal_time
def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
    print(li)
        
import random,copy
li = list(range(101))
random.shuffle(li)
print(li)
li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)
select_sort_simple(li1)
select_sort(li)