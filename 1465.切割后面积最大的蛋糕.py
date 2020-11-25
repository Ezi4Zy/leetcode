#
# @lc app=leetcode.cn id=1465 lang=python
#
# [1465] 切割后面积最大的蛋糕
#

# @lc code=start
class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        max_h = 0
        max_w = 0
        begin = 0
        end = 1
        while end < len(horizontalCuts):
            max_h = max(max_h, horizontalCuts[end]-horizontalCuts[begin])
            begin += 1
            end += 1
        begin = 0
        end = 1
        while end < len(verticalCuts):
            max_w = max(max_w, verticalCuts[end]-verticalCuts[begin])
            begin += 1
            end += 1
        return (max_h * max_w) % (10**9+7)
# @lc code=end

