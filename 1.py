# 题目：用伪代码描述一个二分查找算法的完整过程

# a 必须是一个有序的列表
a = [index for index in range(1, 100, 2)]

target = int(input())     # 需要查找的数值
head = 0                # 头指针
tail = len(a)-1           # 尾指针

while tail >= head:
    mid = int((head + tail)/2)   # mid为中间指针
    if target == a[mid]:
        print(mid)
        exit(0)
    elif target < a[mid]:
        # 表明在左边
        tail = mid-1
    else:
        head = mid+1

exit(-1)
