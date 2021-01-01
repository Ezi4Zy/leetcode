#
# @lc app=leetcode.cn id=453 lang=python
#
# [453] 最小移动次数使数组元素相等
#

# @lc code=start
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = min(nums)
        ret = 0
        for num in nums:
            ret += num - min_num
        return ret
        
# @lc code=end

