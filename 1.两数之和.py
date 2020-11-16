#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for index, num in enumerate(nums):
            other_num = target - num
            if other_num in num_map:
                return [num_map[other_num], index]
            num_map[num] = index
# @lc code=end


