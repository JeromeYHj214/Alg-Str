
"""
基数排序，个位排序，十位排序，...
"""

from cal_time import *
@cal_time
def radix_sort(li):
     max_num = max(li)
     it = 0
     while 10**it <= max_num:
         buckets = [[] for _ in range(10)]
         for val in li:
        # 987 it=1 987//10->98 98%10=8; it=2 987//100=9 9%10=9
             digit = (val // 10 ** it) % 10
             buckets[digit].append(val)
        #分桶完成
         li.clear()
         for bucket in buckets:
             li.extend(bucket)
        #重新把数写会桶里
         it += 1

import random
li = list((range(10000)))
random.shuffle(li)
#print(li)
radix_sort(li)
#print(li)