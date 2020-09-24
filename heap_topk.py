def sift(li,low,high):
    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= high:
        if j + 1 <= high and li[j+1] < li[j]:
            j = j + 1
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i +1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp

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