# -*- coding: utf-8 -*-
"""
快速排序法
"""
from cal_time import *

def partition(data,left,right):
    #ind = random.randint(left,right)
    #data[left], data[ind] = data[ind], data[left] #防止最坏情况 data倒序排序 导致世间复杂度为O(n^2)
    temp = data[left]
    while left < right:
        while left < right and data[right] >= temp: #left > right是为了防止超出索引 使right为-1
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= temp:
            left += 1
        data[right] = data[left]
    data[left] = temp
    return left

def _quick_sort(data,left,right):
    if left < right:
        mid = partition(data,left,right)
        _quick_sort(data,left,mid-1)
        _quick_sort(data,mid+1,right)
        
@cal_time
def quick_sort(data):
    _quick_sort(data,0,len(data)-1)
    

import random,copy
li = list(range(101))
random.shuffle(li)
print(li)
quick_sort(li)
print(li)