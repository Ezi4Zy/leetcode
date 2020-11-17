#
# @lc app=leetcode.cn id=1014 lang=python
#
# [1014] 最佳观光组合
#

# @lc code=start
class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_score = 0
        left = A[0]
        i = 1
        while i < len(A):
            max_score = max(max_score, A[i] - i + left)
            left = max(A[i]+i, left)
            i += 1
        return max_score
# @lc code=end

