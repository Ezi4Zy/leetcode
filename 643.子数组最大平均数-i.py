#
# @lc app=leetcode.cn id=643 lang=python
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        ret = sum_ = sum(nums[:k])
        for index in range(1, len(nums) - k + 1):
            sum_ = sum_ - nums[index-1] + nums[index+k-1]
            ret = max(ret, sum_)
        return float(ret) / k

# @lc code=end

