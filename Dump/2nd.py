from typing import List

def func(ls: List[str], n):
    odd = even = 0
    for i in ls:
        x = int(i)
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd == 1:
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    num = int(input())
    lss = []
    for i in range(num):
        n = int(input())
        temp = input().split(" ")
        lss.append(func(temp, n))
    for i in lss:
        print(i)