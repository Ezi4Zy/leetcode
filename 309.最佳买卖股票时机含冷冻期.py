#
# @lc app=leetcode.cn id=309 lang=python
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution(object):
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        f0, f1, f2 = -prices[0], 0, 0
        # f0: 手上持有股票的最大收益
        # f1: 手上不持有股票，并且处于冷冻期中的累计最大收益
        # f2: 手上不持有股票，并且不在冷冻期中的累计最大收益
        for i in range(1, n):
            f0, f1, f2 = max(f0, f2 - prices[i]), prices[i] + f0, max(f1, f2)
        return max(f1, f2)
        
        
# @lc code=end

