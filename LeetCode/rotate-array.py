class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        if k == 0:
            return
        temp = nums[:n - k]
        for i in range(0, n):
            if i < k:
                nums[i] = nums[n - k + i]
            else:
                nums[i] = temp[i - k]