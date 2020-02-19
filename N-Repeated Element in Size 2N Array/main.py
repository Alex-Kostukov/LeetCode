class Solution:
    def repeatedNTimes(self, nums: [int]) -> int:
        if not nums:
            return None
        num_set = set()
        last_len = 0
        for num in nums:
            num_set.add(num)
            if last_len == len(num_set):
                return num
            else:
                last_len += 1
