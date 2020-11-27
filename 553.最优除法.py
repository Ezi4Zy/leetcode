#
# @lc app=leetcode.cn id=553 lang=python
#
# [553] 最优除法
#

# @lc code=start
class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) < 3:
            return '/'.join([str(num) for num in nums])
        else:
            return str(nums[0]) + '/(' + '/'.join([str(num) for num in nums[1:]]) + ')'
        
        
# @lc code=end

