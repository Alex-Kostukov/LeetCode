# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, matrix: [[int]], k: int) -> [int]:
        result = []
        strength = []
        for i, row in enumerate(matrix):
            strength.append((sum(row), i))
        strength.sort(key=lambda x: (x[0], x[1]))

        i = 0
        while i < len(strength) and i < k:
            result.append(strength[i][1])
            i += 1

        return result


print(Solution().kWeakestRows(matrix =[[1,0,0,0],
 [1,1,1,1],
 [1,1,1,1],
 [1,0,0,0]],k = 10))