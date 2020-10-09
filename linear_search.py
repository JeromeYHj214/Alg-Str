# -*- coding: utf-8 -*-
"""
顺序查找法
"""
from cal_time import *
@cal_time #计时用
def linear_search(li,val):
    for ind, v in enumerate(li):
        if val == v:
            return ind
    else:
        return None

    
import random
li = list(range(101))
random.shuffle(li)
print(li)
ind = linear_search(li,30)
print(ind)