import bisect
from typing import List

def comp_pre(ls: List[int]):
    pre = [0]
    for i in ls:
        pre.append(pre[-1] + i)
    return pre

def func(ls: List[int], pre, b):
    if b > ls[-1]:
        return -1
    n = len(ls)
    idx = bisect.bisect_left(ls, b)
    right_left = n - idx
    res = pre[idx] + (right_left * (b - 1)) + 1
    return res

if __name__ == "__main__":
    temp = (input()).split()
    n, q = int(temp[0]), int(temp[1])
    temp = input().split(" ")
    ls = [int(i) for i in temp]
    ls.sort()
    pre = comp_pre(ls)
    lss = []
    for i in range(q):
        b = int(input())
        lss.append(func(ls, pre, b))
    for i in lss:
        print(i)