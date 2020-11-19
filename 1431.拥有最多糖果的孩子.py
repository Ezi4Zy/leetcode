#
# @lc app=leetcode.cn id=1431 lang=python
#
# [1431] 拥有最多糖果的孩子
#

# @lc code=start
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candy = max(candies) - extraCandies
        for i, candy in enumerate(candies):
            candies[i] = candy >= max_candy
        return candies
# @lc code=end

