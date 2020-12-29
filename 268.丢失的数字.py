#
# @lc app=leetcode.cn id=268 lang=python
#
# [268] 丢失的数字
#

# @lc code=start
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        begin = 0
        end = len(nums) - 1
        while True:
            if nums[begin] != begin:
                return begin
            if nums[end] != end + 1:
                return end + 1
            mid = (begin + end) / 2
            if mid == nums[mid]:
                begin = mid + 1
            else:
                end = mid - 1
            
# @lc code=end

