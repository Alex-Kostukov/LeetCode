class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        """
        Nice task
        """

        if not nums:
            return 0

        max_current = nums[0]
        max_global = nums[0]
        i = 1
        while i < len(nums):
            max_current = max(nums[i], max_current + nums[i])
            max_global = max(max_current, max_global)
            i += 1

        return max_global

