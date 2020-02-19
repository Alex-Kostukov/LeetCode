# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        def remove(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'

                remove(i + 1, j)
                remove(i, j + 1)
                remove(i - 1, j)
                remove(i, j - 1)

        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    remove(i, j)
                    counter += 1
        return counter
