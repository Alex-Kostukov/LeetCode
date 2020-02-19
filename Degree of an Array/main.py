# https://leetcode.com/problems/degree-of-an-array/

from collections import defaultdict

class Solution(object):
    def findShortestSubArray(self, nums):
        first_pos = dict()
        last_pos = dict()
        count = defaultdict(int)
        for i, num in enumerate(nums):
            if num not in first_pos:
                first_pos[num] = i

            last_pos[num] = i
            count[num] += 1

        shortest = len(nums)
        degree = max(count.values())
        for num in count:
            if count[num] == degree:
                shortest = min(shortest, last_pos[num] - first_pos[num] + 1)

        return shortest
