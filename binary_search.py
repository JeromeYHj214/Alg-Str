# -*- coding: utf-8 -*-
"""
二分查找法，li必须排好序
"""
from cal_time import *
#li必须排好序
@cal_time #计时用
def binary_search(li,val):  
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if val == li[mid]:
            return mid
        elif val < li[mid]:
            right = mid - 1
        else:
            left = right + 1
    else:
        return None
    
    
import random,copy
li = list(range(101))
binary_search(li,30)