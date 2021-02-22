#
# @lc app=leetcode.cn id=6 lang=python
#
# [6] Z 字形变换
#

# @lc code=start
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = [""] * numRows
        current_row = 0
        direction = 0
        for c in s:
            rows[current_row] = rows[current_row] + c
            if (current_row == 0 and direction == 1) or (current_row == numRows-1 and direction == 0):
                direction = 0 if direction else 1
            if direction:
                current_row -=1
            else:
                current_row += 1
        return reduce(lambda a, b : a + b, rows)
        
# @lc code=end

