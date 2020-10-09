"""
插入排序法
"""
def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i];
        j = i - 1
        while j >= 0:
            if li[j] > tmp:
                li[j+1] = li[j]
                j -= 1
            else:
                break
        li[j+1] = tmp
        print(li)

li = [5,4,7,6,2,3,1]
insert_sort(li)