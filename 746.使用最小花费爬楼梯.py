#
# @lc app=leetcode.cn id=746 lang=python
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * (len(cost) + 1)
        dp[0] = dp[1] = 0
        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[len(dp)-1]
        
# @lc code=end

