#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[0]*2 for _ in range(len(nums))]
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for index in range(1, len(nums)):
            dp[index][0] = max(dp[index-1])
            dp[index][1] = dp[index-1][0] + nums[index]
        return max(dp[len(nums)-1])

# @lc code=end

