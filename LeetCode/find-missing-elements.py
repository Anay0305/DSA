class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_ = 101
        max_ = 0
        for i in nums:
            min_ = min(min_, i)
            max_ = max(max_, i)
        uni = set(nums)
        res = []
        for i in range(min_, max_+1):
            if i not in uni:
                res.append(i)
        return res