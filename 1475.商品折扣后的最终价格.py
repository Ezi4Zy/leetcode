#
# @lc app=leetcode.cn id=1475 lang=python
#
# [1475] 商品折扣后的最终价格
#

# @lc code=start
class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        for index in range(len(prices)):
            for j in range(index+1, len(prices)):
                if prices[index] >= prices[j]:
                    prices[index] -= prices[j]
                    break
        return prices


# @lc code=end

