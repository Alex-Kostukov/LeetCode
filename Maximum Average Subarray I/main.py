# https://leetcode.com/problems/maximum-average-subarray-i/
class Solution:
    def findMaxAverage(self, nums: [int], k: int) -> float:
        if not nums:
            return 0

        total = sum(nums[:k])
        best = total/k
        for i in range(k, len(nums)):
            total -= nums[i - k]
            total += nums[i]
            best = max(best,total/k)

        return best

print(Solution().findMaxAverage([3,3,4,3,0]
,3))