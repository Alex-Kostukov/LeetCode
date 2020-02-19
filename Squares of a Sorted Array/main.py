# https://leetcode.com/problems/squares-of-a-sorted-array/

from bisect import insort_left


class Solution:
    def sortedSquares(self, nums: [int]) -> [int]:
        result = []
        for num in nums:
            insort_left(result, num ** 2)

        return result
