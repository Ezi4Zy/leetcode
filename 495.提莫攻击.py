#
# @lc app=leetcode.cn id=495 lang=python
#
# [495] 提莫攻击
#

# @lc code=start
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        ret = 0
        cur = 0
        for s in timeSeries:
            ret += duration if s >= cur else s - cur + duration
            cur = s + duration
        return ret

# @lc code=end

