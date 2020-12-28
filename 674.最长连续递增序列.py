#
# @lc app=leetcode.cn id=674 lang=python
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        begin_index = 0
        if nums:
            for index in range(len(nums)):
                if index != begin_index:
                    if nums[index] <= nums[index-1]:
                        max_length = max(max_length, index - begin_index)
                        begin_index = index
            else:
                max_length = max(max_length, index - begin_index + 1)
        return max_length
# @lc code=end

