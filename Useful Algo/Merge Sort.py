from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        def sort(n1, n2: None):
            n1 = self.sortArray(n1)
            if n2:
                n2 = self.sortArray(n2)
            ls = [0] * (len(n1) + len(n2))
            count1 = count2 = 0
            for i in range(len(ls)):
                if count1 == len(n1):
                    ls[i] = n2[count2]
                    count2 += 1
                    continue
                elif count2 == len(n2):
                    ls[i] = n1[count1]
                    count1 += 1
                    continue

                if n2[count2] <= n1[count1]:
                    ls[i] = n2[count2]
                    count2 += 1
                elif n1[count1] <= n2[count2]:
                    ls[i] = n1[count1]
                    count1 += 1

            return ls
        return sort(nums[:n//2], nums[n//2:])