#
# @lc app=leetcode.cn id=704 lang=python
#
# [704] 二分查找
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin, end = 0, len(nums) - 1
        while begin <= end:
            mid = (begin + end) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                begin = mid + 1
            else:
                end = mid - 1
        return -1

# @lc code=end

