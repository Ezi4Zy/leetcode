#
# @lc app=leetcode.cn id=35 lang=python
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin = 0
        end = len(nums) - 1
        while begin < end:
            mid = (begin + end) / 2
            if nums[mid] < target:
                begin = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                end = mid - 1
        return begin + 1 if nums[begin] < target else begin
# @lc code=end

