#
# @lc app=leetcode.cn id=724 lang=python
#
# [724] 寻找数组的中心索引
#

# @lc code=start
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = sum(nums[1:])
        index = 0
        while left != right and index < len(nums)-1:
            left += nums[index]
            right -= nums[index+1]
            index += 1
        
        return index if left == right else -1
# @lc code=end

