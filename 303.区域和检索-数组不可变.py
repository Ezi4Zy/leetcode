#
# @lc app=leetcode.cn id=303 lang=python
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.cache_sum = {}
        for i in range(len(nums)):
            self.cache_sum[i] = self.cache_sum.get(i-1, 0) + nums[i]
            


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.cache_sum[j] - self.cache_sum.get(i-1, 0)
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

