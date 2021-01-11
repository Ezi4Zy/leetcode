#
# @lc app=leetcode.cn id=628 lang=python
#
# [628] 三个数的最大乘积
#

# @lc code=start
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        negative_nums = [num for num in nums if num < 0]
        positive_nums = [num for num in nums if num > 0]
        positive_nums.sort()
        negative_nums.sort()
        is_zero = 0 in nums
        if len(negative_nums) >= 2:
            max_negative_nums = negative_nums[0] * negative_nums[1]
            min_negative_nums = negative_nums[-1] * negative_nums[-2]
        elif len(negative_nums) == 1:
            max_negative_nums = 0 if is_zero else negative_nums[0]
            min_negative_nums = 0 if is_zero else negative_nums[-1]
        else:
            max_negative_nums = 0
            min_negative_nums = 0
        if len(positive_nums) > 2:
            return positive_nums[-1] * max(positive_nums[-2]*positive_nums[-3], max_negative_nums)
        elif len(positive_nums) > 0:
            return positive_nums[-1] * max_negative_nums
        else:
            return 0 if is_zero else min_negative_nums * negative_nums[-3]
# @lc code=end

