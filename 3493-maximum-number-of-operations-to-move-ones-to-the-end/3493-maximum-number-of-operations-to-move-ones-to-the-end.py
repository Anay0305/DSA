class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        res = i = 0
        count = 0
        check = False
        while i < n:
            val = int(s[i])
            if val == 1:
                if check:
                    count += 1
                else:
                    check = True
                    count += 1
            else:
                if check:
                    res += count
                    check = False
            i += 1
        return res