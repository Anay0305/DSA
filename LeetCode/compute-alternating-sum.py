class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        res = 0
        check = True
        for i in nums:
            if check:
                res += i
            else:
                res -= i
            check = not check
        return res