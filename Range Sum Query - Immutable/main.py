# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: [int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        if not self.nums:
            return 0
        return sum(self.nums[i:j + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
print(NumArray([1, 2]).sumRange(10, 20))
