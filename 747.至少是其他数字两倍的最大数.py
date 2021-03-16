#
# @lc app=leetcode.cn id=747 lang=python
#
# [747] 至少是其他数字两倍的最大数
#

# @lc code=start
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = max(nums)
        index = nums.index(num)
        new_nums = nums[:index] + nums[index+1:]
        if new_nums:
            num_second = max(new_nums)
            if num_second * 2 > num:
                return -1
        return index
# @lc code=end

