#
# @lc app=leetcode.cn id=657 lang=python
#
# [657] 机器人能否返回原点
#

# @lc code=start

class Solution1(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        move_counter = collections.Counter()
        for move in moves:
            move_counter[move] += 1
        return move_counter['U'] == move_counter['D'] and move_counter['R'] == move_counter['L']

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        row = column = 0
        for move in moves:
            if move == 'U':
                column += 1
            if move == 'D':
                column -= 1
            if move == 'R':
                row += 1
            if move == 'L':
                row -= 1
        return not (row or column)
# @lc code=end

