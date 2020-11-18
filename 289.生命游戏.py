#
# @lc app=leetcode.cn id=289 lang=python
#
# [289] 生命游戏
#

# @lc code=start
class Solution(object):

    def calculate_alive_count(self, m, n, board):
        alive_count = 0
        m_length = len(board)
        n_length = len(board[0])
        # left
        if n > 0 and board[m][n-1] in (-1, 1):
            alive_count += 1
        # right
        if n < n_length-1 and board[m][n+1] in (-1, 1):
            alive_count += 1
        # left up
        if m > 0 and n > 0 and board[m-1][n-1] in (-1, 1):
            alive_count += 1
        # up 
        if m > 0 and board[m-1][n] in (-1, 1):
            alive_count += 1
        # right up
        if m > 0 and n < n_length-1 and board[m-1][n+1] in (-1, 1):
            alive_count += 1
        # left down
        if m < m_length-1 and n > 0 and board[m+1][n-1] in (-1, 1):
            alive_count += 1
        # down 
        if m < m_length-1 and board[m+1][n] in (-1, 1):
            alive_count += 1
        # right down
        if m < m_length-1 and n < n_length-1 and board[m+1][n+1] in (-1, 1):
            alive_count += 1
        return alive_count
        

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        for m, m_board in enumerate(board):
            for n, cell in enumerate(m_board):
                if cell == 0:
                    if self.calculate_alive_count(m, n, board) == 3:
                        board[m][n] = 2
                else:
                    if self.calculate_alive_count(m, n, board) not in (2,3):
                        board[m][n] = -1
        for m, m_board in enumerate(board):
            for n, cell in enumerate(m_board):
                if cell == 2:
                    board[m][n] = 1
                elif cell == -1:
                    board[m][n] = 0
# @lc code=end

