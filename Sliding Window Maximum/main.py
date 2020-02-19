# https://leetcode.com/problems/sliding-window-maximum/

from bisect import insort_left, bisect_left


class Solution:
    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        def remove_val(val):
            nonlocal maxs
            i = bisect_left(maxs, val)
            maxs = maxs[:i] + maxs[i + 1:]

        if not nums or k <= 0:
            return []
        result = []
        maxs = []

        for num in nums[:k]:
            insort_left(maxs, num)

        result.append(maxs[-1])
        for i in range(k, len(nums)):
            remove_val(nums[i - k])
            insort_left(maxs, nums[i])
            result.append(maxs[-1])

        return result
