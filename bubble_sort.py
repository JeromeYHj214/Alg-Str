# -*- coding: utf-8 -*-
"""
冒泡排序法
"""

from cal_time import *
@cal_time
def bubble_sort(li):
    for i in range(len(li)-1):
        exchange = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j+1], li[j] = li[j], li[j+1]
                exchange = True
        #print(li)
        if exchange == False:
            return
        

import random,copy
li = list(range(101))
random.shuffle(li)
print(li)
bubble_sort(li)
print(li)