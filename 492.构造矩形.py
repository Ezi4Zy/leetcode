#
# @lc app=leetcode.cn id=492 lang=python
#
# [492] 构造矩形
#

# @lc code=start
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        W = int(math.sqrt(area))
        while True:
            if area % W == 0:
                return [area / W, W]
            W -= 1
# @lc code=end

