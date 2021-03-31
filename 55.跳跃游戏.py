#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = 0
        for index, num in enumerate(nums):
            if index > m:
                return False
            m = max(m, index + num)
        return True
# @lc code=end

