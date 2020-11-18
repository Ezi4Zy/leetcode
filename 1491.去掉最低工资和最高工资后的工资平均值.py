#
# @lc app=leetcode.cn id=1491 lang=python
#
# [1491] 去掉最低工资和最高工资后的工资平均值
#

# @lc code=start
class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        high = max(salary[:2])
        low = min(salary[:2])
        count = 0
        total = 0
        for s in salary[2:]:
            if s > high:
                high, s = s, high
            if s < low:
                low, s = s, low
            total += s
            count += 1
        return float(total) / count
# @lc code=end

