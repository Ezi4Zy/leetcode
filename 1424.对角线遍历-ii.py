#
# @lc app=leetcode.cn id=1424 lang=python
#
# [1424] 对角线遍历 II
#

# @lc code=start
class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        ret = {}
        for i , num in enumerate(nums):
            for j, n in enumerate(num):
                ret.setdefault(i+j, []).append(nums[i][j])
        result = []
        for i in range(len(ret.keys())):
            result += ret[i][::-1]
        return result
# @lc code=end

