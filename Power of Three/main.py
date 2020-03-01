# https://leetcode.com/problems/power-of-three/
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True

        while n > 1:
            n /= 3

        return n == 1


print(Solution().isPowerOfThree(81))
