import bisect
from typing import List

def func(ls: List[int], n, x, k):
    ls.sort()
    final = x + 100*k
    rank = bisect.bisect_right(ls, final)
    rank = n - rank
    if rank <= k:
        return 1
    else:
        return rank - k + 1

if __name__ == "__main__":
    num = int(input())
    lss = []
    for i in range(num):
        temp = input().split(" ")
        n, x, k = int(temp[0]), int(temp[1]), int(temp[2])
        temp = input().split(" ")
        ls = [int(i) for i in temp]
        lss.append(func(ls, n, x, k))
    for i in lss:
        print(i)