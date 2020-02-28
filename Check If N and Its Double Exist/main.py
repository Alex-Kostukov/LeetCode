# https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution:
    def checkIfExist(self, nums: [int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if 2 * nums[i] == nums[j] or 2 * nums[j] == nums[i]:
                    return True

        return False
