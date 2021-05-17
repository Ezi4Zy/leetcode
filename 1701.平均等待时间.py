#
# @lc app=leetcode.cn id=1701 lang=python
#
# [1701] 平均等待时间
#

# @lc code=start
class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        cur = customers[0][0]
        waiting_time = 0
        for arrival_time, cook_time in customers:
            cur = max(cur, arrival_time) + cook_time
            waiting_time += cur - arrival_time
        
        return float(waiting_time) / len(customers)



# @lc code=end

