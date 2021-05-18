#
# @lc app=leetcode.cn id=343 lang=python
#
# [343] 整数拆分
#

# @lc code=start
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = max([(i-j) * max(dp[j], j)  for j in range(2, i)])
        return dp[n]

# @lc code=end

