#
# @lc app=leetcode.cn id=287 lang=python
#
# [287] 寻找重复数
#

# @lc code=start
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (sum(nums) - sum(set(nums))) / (len(nums) - len(set(nums)))
# @lc code=end

