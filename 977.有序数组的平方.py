#
# @lc app=leetcode.cn id=977 lang=python
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        begin = 0
        end = len(A) - 1
        ret = []
        while end != begin:
            if abs(A[end]) > abs(A[begin]):
                ret.append(A[end] ** 2)
                end -= 1
            else:
                ret.append(A[begin] ** 2)
                begin += 1
        ret.append(A[begin] ** 2)
        ret.reverse()
        return ret
# @lc code=end

