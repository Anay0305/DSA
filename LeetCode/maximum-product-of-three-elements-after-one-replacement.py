class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        non_zeros = []
        for i in nums:
            if i != 0:
                non_zeros.append(abs(i))
        non_zeros.sort()
        if len(non_zeros) >= 2:
            return non_zeros[-1] * non_zeros[-2] * 10**5
        else:
            return 0