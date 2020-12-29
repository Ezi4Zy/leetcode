#
# @lc app=leetcode.cn id=283 lang=python
#
# [283] 移动零
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        cur_index = 0
        index = 0
        while index < len(nums):
            if nums[index] == 0:
                zero_count += 1
            else:
                nums[cur_index] = nums[index]
                cur_index += 1
            index += 1
        while cur_index < len(nums):
            nums[cur_index] = 0
            cur_index += 1
# @lc code=end

