#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin = 0
        end = 1
        while end < len(nums):
            if nums[begin] != nums[end]:
                begin += 1
                nums[begin] = nums[end]
            end += 1
        return begin+1
# @lc code=end

