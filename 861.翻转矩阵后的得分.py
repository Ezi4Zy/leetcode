#
# @lc app=leetcode.cn id=861 lang=python
#
# [861] 翻转矩阵后的得分
#

# @lc code=start
class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for a in A:
            if a[0] == 0:
                for index in range(len(a)):
                    a[index] ^= 1
        for i in range(len(A[0])):
            if sum([a[i] for a in A]) < (len(A)+1) / 2:
                for a in A:
                    a[i] ^= 1
        return sum([sum([2 ** (len(a)-index-1) * n for index, n in enumerate(a)]) for a in A])
           
# @lc code=end

