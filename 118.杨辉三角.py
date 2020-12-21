#
# @lc app=leetcode.cn id=118 lang=python
#
# [118] 杨辉三角
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        for row in range(numRows):
            l = [1]
            index = 1
            while index < row + 1:
                up_row = ret[row-1]
                l.append(up_row[index-1] + (up_row[index] if index < row else 0))
                index += 1
            ret.append(l)
        return ret
# @lc code=end

