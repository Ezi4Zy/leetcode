#
# @lc app=leetcode.cn id=79 lang=python
#
# [79] 单词搜索
#

# @lc code=start
class Solution(object):
    
    def _exist(self, board, word, row, column):
        if word:
            for r, c in [(row, column + 1), (row, column - 1), (row + 1, column), (row - 1, column)]:
                if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == word[0]:
                    board[r][c] = 0
                    if self._exist(board, word[1:], r, c):
                        return True
                    board[r][c] = word[0]
            return False
        else:
            return True
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    board[i][j] = 0
                    if self._exist(board, word[1:], i, j):
                        return True
                    board[i][j] = word[0]
        return False


# @lc code=end

