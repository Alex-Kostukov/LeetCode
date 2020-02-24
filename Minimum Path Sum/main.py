# https://leetcode.com/problems/minimum-path-sum/


class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        if not grid:
            return 0

        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
                elif i > 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                elif j > 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]

        return dp[-1][-1]


print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
