class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        pre = [0]
        for i, val in enumerate(nums):
            pre.append(pre[i] + val)

        total = pre[-1]
        half_sum = total // 2
        res = 0

        if total % 2 == 0:
            l = bisect.bisect_left(pre, half_sum)
            r = bisect.bisect_right(pre, half_sum)
            if r > l:
                res += (r - l - 1) * 2
        else:
            for target in (half_sum, half_sum + 1):
                l = bisect.bisect_left(pre, target)
                r = bisect.bisect_right(pre, target)
                if r > l:
                    res += (r - l - 1)
        return res