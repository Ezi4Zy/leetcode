#
# @lc app=leetcode.cn id=27 lang=python
#
# [27] 移除元素
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        begin = 0
        end = 0
        while end < len(nums):
            if nums[end] != val:
                nums[begin] = nums[end]
                begin += 1
            end += 1
        return begin
                    
# @lc code=end

