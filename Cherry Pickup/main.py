# https://leetcode.com/problems/cherry-pickup/

# TODO: Solve
class Solution:
    def cherryPickup(self, grid: [[int]]) -> int:
        if not grid or grid[0][0] == -1:
            return 0

        def calculate_dp():
            # 3d for value, path memoization
            dp = [[[0, []] for _ in range(len(grid[0]))] for _ in range(len(grid))]
            dp[0][0][0] = grid[0][0]
            # grid[0][0] = 0
            dp[0][0][1].append((0, 0))

            for i in range(len(grid)):

                for j in range(len(grid[i])):
                    if grid[i][j] == -1:
                        grid[i][j] = float('-inf')

                    if i > 0 and j > 0:
                        # best path save
                        if dp[i - 1][j][0] > dp[i][j - 1][0]:
                            dp[i][j][1] = dp[i - 1][j][1] + [(i, j)]
                        else:
                            dp[i][j][1] = dp[i][j - 1][1] + [(i, j)]

                        dp[i][j][0] = max(dp[i - 1][j][0], dp[i][j - 1][0]) + grid[i][j]

                    elif i > 0:
                        dp[i][j][0] = dp[i - 1][j][0] + grid[i][j]
                        # path save
                        dp[i][j][1] = dp[i - 1][j][1] + [(i, j)]

                    elif j > 0:
                        dp[i][j][0] = dp[i][j - 1][0] + grid[i][j]
                        # path dave
                        dp[i][j][1] = dp[i][j - 1][1] + [(i, j)]

            return dp[-1][-1]

        def delete(index_list):
            for i, j in index_list:
                grid[i][j] = 0

        # first run from start to end
        first_run, index_list = calculate_dp()

        # set all visited cell to 0
        delete(index_list)

        # second run from end to start (order is not important)
        second_run, index_list = calculate_dp()

        result = first_run + second_run
        if result == float('-inf'):
            return 0

        return result


"""
0   1  -1
1   0  -1
1   1   1 
"""

print(Solution().cherryPickup([[0, 1, -1], [1, 0, -1], [1, 1, 1]]))

"""
1   1   1
1   1   1
"""
print(Solution().cherryPickup([[1, 1, 1],
                               [1, 1, 1]]))

print(Solution().cherryPickup([[1, -1, 1, -1, 1],
                               [1, 0, 1, 0, 1],
                               [1, 0, 1, 0, 1],
                               [1, 0, 1, 0, 1],
                               [1, 0, 1, 0, 1]]))
"""
              

"""

print(Solution().cherryPickup([[1, 1, 1, 1, 0, 0, 0],
                               [0, 0, 0, 1, 0, 0, 0],
                               [0, 0, 0, 1, 0, 0, 1],
                               [1, 0, 0, 1, 0, 0, 0],
                               [0, 0, 0, 1, 0, 0, 0],
                               [0, 0, 0, 1, 0, 0, 0],
                               [0, 0, 0, 1, 1, 1, 1]]))


a = [[1,1,1,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,1],[1,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,1,1]]
print(len(a))
print(len(a[0]))