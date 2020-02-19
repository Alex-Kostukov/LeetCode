class Solution:
    def numRookCaptures(self, board: [[str]]) -> int:

        def check_direction(i, j, action_i, action_j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board):
                return 0
            if board[i][j] == 'p':
                return 1
            if board[i][j] == 'B':
                return 0

            i, j = action_i(i), action_j(j)
            return check_direction(i, j, action_i, action_j)

        rook_pos = (-1, -1)
        found = False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'R':
                    rook_pos = (i, j)

                if found:
                    break
            if found:
                break

        left = check_direction(*rook_pos, lambda i: i, lambda j: j - 1)
        right = check_direction(*rook_pos, lambda i: i, lambda j: j + 1)
        top = check_direction(*rook_pos, lambda i: i - 1, lambda j: j)
        down = check_direction(*rook_pos, lambda i: i + 1, lambda j: j)

        return left + right + top + down

