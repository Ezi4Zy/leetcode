#
# @lc app=leetcode.cn id=581 lang=python
#
# [581] 最短无序连续子数组
#

# @lc code=start
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        start = 0
        end = len(nums) - 1
        while start < len(nums):
            if sorted_nums[start] == nums[start]:
                start += 1
            else:
                break
        if start == len(nums):
            return 0
        while end >=0:
            if sorted_nums[end] == nums[end]:
                end -= 1
            else:
                break
        return end - start + 1
        
# @lc code=end

