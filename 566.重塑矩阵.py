#
# @lc app=leetcode.cn id=566 lang=python
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if nums:
            if len(nums) * len(nums[0]) != r * c:
                return nums
            ret = []
            for num in nums:
                ret.extend(num)
            return [ret[k:k+c] for k in range(0, len(ret), c)]
        return nums
# @lc code=end

