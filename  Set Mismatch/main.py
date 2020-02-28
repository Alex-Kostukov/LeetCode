# https://leetcode.com/problems/set-mismatch/
from collections import defaultdict


class Solution:
    def findErrorNums(self, nums: [int]) -> [int]:
        values = defaultdict(int)
        sum = 0
        doubled = 0
        for num in nums:
            values[num] += 1
            sum += num
            if values[num] > 1:
                doubled = num

        missing = len(nums) * (len(nums) + 1) // 2 - (sum - doubled)
        return [doubled, missing]


print(Solution().findErrorNums([1, 10, 3, 4, 5, 6, 10, 8, 9, 7]))
