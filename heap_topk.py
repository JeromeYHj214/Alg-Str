"""
堆排序
"""
def sift(li,low,high):
    i = low     # i指向根节点
    j = 2 * i + 1  # j指向孩子结点
    tmp = li[low]  #保存堆顶
    while j <= high: #只要j节点有效
        if j + 1 <= high and li[j+1] < li[j]: #右孩子存在且比较大
            j = j + 1 #指向右孩子
        if li[j] < tmp:
            li[i] = li[j]
            i = j #往下一层
            j = 2 * i +1
        else:       #tmp值更大，放在位置i
            li[i] = tmp
            break

    # 当while因为条件跳出循环会去执行else，若因为break跳出循环，则不执行else。

    else:
        li[i] = tmp   #tmp查到最底层，跳出while，tmp还未放回，所有加一步放回

def topk(li,k):
    heap = li[0:k]
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k-1)
    for i in range(k,len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)
    for i in range(k-1, -1, -1):
        heap[i], heap[0] = heap[0], heap[i]
        sift(heap, 0, i-1)
    return heap

import random
li  = list(range(100))
random.shuffle(li)
print(topk(li,10))
ki = [1,0,2,4,7,9,8,5,6,3,17,15,20,16,22,100]
print(topk(ki,6))