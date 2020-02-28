# https://leetcode.com/problems/maximum-number-of-balloons/

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = Counter(text)
        balloon = Counter('balloon')
        balloon.subtract(balloon)
        balloon.subtract(freq)

        min_count = float('inf')
        for key in 'balloon':
            current = abs(balloon[key])
            if key == 'l' or key == 'o':
                current //= 2
            min_count = min(min_count, current)

        return min_count if min_count != float('inf') else 0

print(Solution().maxNumberOfBalloons("xxxx"))