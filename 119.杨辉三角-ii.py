#
# @lc app=leetcode.cn id=119 lang=python
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution(object):

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex += 1
        ret = [0] * rowIndex
        ret[0] = 1
        for cur_index in range(rowIndex):
            j = cur_index
            while j > 0:
                ret[j] = ret[j-1] + ret[j]
                j -= 1
        ret[-1] = 1
        return ret
        
# @lc code=end

