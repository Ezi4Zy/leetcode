#
# @lc app=leetcode.cn id=1518 lang=python
#
# [1518] 换酒问题
#

# @lc code=start
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange, emptyBottles=0):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        allBottles = numBottles + emptyBottles
        if allBottles < numExchange:
            return numBottles
        else:
            return numBottles + self.numWaterBottles(allBottles / numExchange, 
                                                     numExchange, 
                                                     allBottles % numExchange)

# @lc code=end

