#
# @lc app=leetcode.cn id=322 lang=python
#
# [322] 零钱兑换
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 0
        for index in range(1, amount + 1):
            if index in coins:
                dp[index] = 1
            else:
                pre_dp = [dp[index - coin] for coin in coins if coin < index and dp[index - coin] != -1]
                if pre_dp:
                    dp[index] = min(pre_dp) + 1
                else:
                    dp[index] = -1
        return dp[amount]

# @lc code=end

