# https://leetcode.com/problems/shortest-distance-to-a-character/
class Solution:
    def shortestToChar(self, string: str, target: str) -> [int]:

        result = [float('inf')] * len(string)

        def _shortest(start, end, shift):
            distance = float('inf')
            for i in range(start, end, shift):
                char = string[i]
                if char == target:
                    distance = 0
                else:
                    distance += 1
                result[i] = min(result[i], distance)

        _shortest(0, len(string), 1)
        _shortest(len(string) - 1, -1, -1)

        return result


print(Solution().shortestToChar('abbcdcbba', 'a'))
