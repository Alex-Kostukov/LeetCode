# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        visited = set()
        last_length = 0
        for num in nums:
            visited.add(num)
            if last_length == len(visited):
                return num
            last_length += 1
