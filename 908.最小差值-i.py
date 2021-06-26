#
# @lc app=leetcode.cn id=908 lang=python
#
# [908] 最小差值 I
#

# @lc code=start
class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        diff = max(nums) - min(nums)
        return diff - 2 * k if diff > 2 * k else 0


# @lc code=end

