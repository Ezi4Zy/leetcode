#
# @lc app=leetcode.cn id=1800 lang=python
#
# [1800] 最大升序子数组和
#

# @lc code=start
class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_nums = [0] * len(nums)
        sum_nums[0] = nums[0]
        for index in range(1, len(nums)):
            if nums[index] > nums[index-1]:
                sum_nums[index] = sum_nums[index-1] + nums[index]
            else:
                sum_nums[index] = nums[index]
        return max(sum_nums)


# @lc code=end

