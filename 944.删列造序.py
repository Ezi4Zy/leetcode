#
# @lc app=leetcode.cn id=944 lang=python
#
# [944] 删列造序
#

# @lc code=start
class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        ret = 0
        for j in range(len(A[0])):
            for i in range(len(A))[1:]:
                if A[i][j] < A[i-1][j]:
                    ret += 1
                    break
        return ret          
# @lc code=end

