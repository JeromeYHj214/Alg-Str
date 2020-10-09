"""
桶排序，针对整数
"""
def bucket_sort(li,n=100,max_num=10000):
    buckets = [[] for _ in range(n)]
    for val in li:
        i = min(val // (max_num // n), n-1) # 防止最大值溢出
        buckets[i].append(val)
        for j in range(len(buckets[i])-1,0,-1): # 直接对桶进行排序
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:  # 防止多余的运算                     
                break
    li.clear()
    for bucket in buckets:
        #li += bucket
        li.extend(bucket)



import random
li = list(range(21))
random.shuffle(li)
print(li)
bucket_sort(li,4,20)
print(li)