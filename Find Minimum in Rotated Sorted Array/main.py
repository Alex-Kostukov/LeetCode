# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: [int]) -> int:
        if not nums:
            return None

        result = nums[0]
        last = nums[0]
        for num in nums:

            result = min(result, num)
            if last > num:
                break

            last = num

        return result


print(Solution().findMin([0,3,4,5,6]))
