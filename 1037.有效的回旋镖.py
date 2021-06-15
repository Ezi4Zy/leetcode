#
# @lc app=leetcode.cn id=1037 lang=python
#
# [1037] 有效的回旋镖
#

# @lc code=start
class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        return not (points[2][0] - points[1][0]) * (points[1][1] - points[0][1]) == (points[1][0] - points[0][0]) * (points[2][1] - points[1][1])

# @lc code=end

