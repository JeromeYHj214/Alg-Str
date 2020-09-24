"""""
归并排序
"""""
def merge(li, low, mid, high):
    """

    :param li:列表
    :param low:起点
    :param mid:第一个有序数列的尾
    :param high:终点
    :return:
    """
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append((li[j]))
        j += 1
    li[low:high+1] = ltmp

"""""
li = [1,3,4,5,2,6,7,8,9]
merge(li,0,3,8)
print(li)
"""""

def merge_sort(li, low, high):
    mid = (low + high) // 2
    if low < high:
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high) # mid+1 需要注意
        #print(li[low:high + 1])
        merge(li, low, mid, high)
        #print(li[low:high+1])

import random
li = list(range(16))
random.shuffle(li)
print(li)
merge_sort(li, 0, len(li)-1)
print(li)
