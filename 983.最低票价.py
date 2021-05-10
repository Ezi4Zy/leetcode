#
# @lc app=leetcode.cn id=983 lang=python
#
# [983] 最低票价
#

# @lc code=start
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [0] * (days[-1] + 31)
        index = -1
        for day in range(days[-1], days[0]-1, -1):
            if day == days[index]:
                dp[day] = min(dp[day+1] + costs[0], dp[day+7] + costs[1], dp[day+30] + costs[2])
                index -= 1
            else:
                dp[day] = dp[day+1]
        return dp[days[0]]

            
# @lc code=end

