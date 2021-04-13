#
# @lc app=leetcode.cn id=279 lang=python
#
# [279] 完全平方数
#


# @lc code=start
import math
class Solution(object):
    
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]
        dp = [5] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
        return dp[n]

# @lc code=end

