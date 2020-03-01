# https://leetcode.com/problems/k-diff-pairs-in-an-array/
from collections import defaultdict


class Solution:
    def findPairs(self, nums: [int], k: int) -> int:
        if k < 0:
            return 0

        num_map = defaultdict(int)
        for num in nums:
            num_map[num] += 1

        result = 0
        for num in num_map:
            if k != 0:
                if num + k in num_map:
                    result += 1
            else:
                if num in num_map and num_map[num] >= 2:
                    result += 1
        return result

print(Solution().findPairs([3, 1, 4, 1, 5], 2))
a = set()
a.add((1, 2))
a.add((2, 1))
print(a)
