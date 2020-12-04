#
# @lc app=leetcode.cn id=154 lang=python
#
# [154] 寻找旋转排序数组中的最小值 II
#


# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin = 0
        end = len(nums) - 1
        while begin < end:
            if nums[begin] < nums[end]:
                break
            mid = (begin + end) / 2
            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] > nums[end]:
                begin = mid + 1
            else:
                end -= 1
        return nums[begin]
        
# @lc code=end

