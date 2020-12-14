#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子序和
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = 0
        ans = nums[0]
        for num in nums:
            pre = max(pre + num, num)
            ans = max(ans, pre)
        return ans
# @lc code=end

