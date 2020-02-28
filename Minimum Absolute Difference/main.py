# https://leetcode.com/problems/minimum-absolute-difference/
class Solution:
    def minimumAbsDifference(self, nums: [int]) -> [[int]]:
        min_diff = float('inf')
        result = []
        nums.sort()
        for i in range(len(nums)-1):
            diff = abs(nums[i] - nums[i + 1])

            if diff < min_diff:
                min_diff = diff
                result = []

            if diff == min_diff:
                result.append([min(nums[i], nums[i+1]), max(nums[i], nums[i+1])])

        return sorted(result, key=lambda x: x[0])


print(Solution().minimumAbsDifference([6, 4, 2, 56, 78, 191, 190]))
