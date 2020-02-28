# https://leetcode.com/problems/unique-number-of-occurrences/
from collections import Counter


class Solution:
    def uniqueOccurrences(self, nums: [int]) -> bool:
        freq = Counter(nums)
        freq2 = Counter(freq.values())

        for value in freq2.values():
            if value != 1:
                return False
        return True


