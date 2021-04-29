#
# @lc app=leetcode.cn id=152 lang=python
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_pre, max_pre, ret = nums[0], nums[0], nums[0]
        for index in range(1, len(nums)):
            min_pre, max_pre = min(min_pre * nums[index], nums[index], max_pre * nums[index]), max(min_pre * nums[index], max_pre * nums[index], nums[index])
            ret = max(max_pre, ret)
        return ret

# @lc code=end

