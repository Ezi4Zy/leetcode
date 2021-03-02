#
# @lc app=leetcode.cn id=1685 lang=python
#
# [1685] 有序数组中差绝对值之和
#

# @lc code=start
class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum_ = sum([nums[i] - nums[0] for i in range(len(nums))])
        res = [sum_]
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            res.append(res[-1] + i * diff - (len(nums) - i) * diff)
        return res
        
# @lc code=end

