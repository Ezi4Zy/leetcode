#
# @lc app=leetcode.cn id=130 lang=python
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution(object):

    def dfs(self, board, m, n):
        if m - 1 >= 0 and board[m-1][n] == 'O':
            board[m-1][n] = ''
            self.dfs(board, m-1, n)
        if m + 1 < len(board) and board[m+1][n] == 'O':
            board[m+1][n] = ''
            self.dfs(board, m+1, n)
        if n - 1 >= 0 and board[m][n-1] == 'O':
            board[m][n-1] = ''
            self.dfs(board, m, n-1)
        if n + 1 < len(board[0]) and board[m][n+1] == 'O':
            board[m][n+1] = ''
            self.dfs(board, m, n+1)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        for m in (0, len(board) - 1):
            for n in range(len(board[0])):
                if board[m][n] == 'O':
                    board[m][n] = ''
                    self.dfs(board, m, n)
        for n in (0, len(board[0]) - 1):
            for m in range(len(board)):
                if board[m][n] == 'O':
                    board[m][n] = ''
                    self.dfs(board, m, n)
        for m in range(len(board)):
            for n in range(len(board[0])):
                if board[m][n] == '':
                    board[m][n] = 'O'
                else:
                    board[m][n] = 'X'          
# @lc code=end

