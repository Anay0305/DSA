class Solution:
    def smallestNumber(self, n: int) -> int:
        check = False
        i = 0
        while i <= 9:
            if 2**i == n:
                check = True
                break
            elif 2**i > n:
                check = False
                break
            i += 1
        if check:
            return 2**(i+1) - 1
        else:
            return 2**i - 1