# https://leetcode.com/problems/relative-sort-array/
class Solution:
    def relativeSortArray(self, arr1: [int], arr2: [int]) -> [int]:
        if not arr1:
            return []
        order = dict()
        max_ = arr1[0]
        for i, num in enumerate(arr2):
            order[num] = i
            max_ = max(max_, num)

        arr1.sort(key=lambda x: order.get(x, max_ + x))
        return arr1


print(Solution().relativeSortArray([26,26, 21, 11, 20, 50, 34, 1, 18], [21, 11, 26, 20]))


print((1,) > (1,))