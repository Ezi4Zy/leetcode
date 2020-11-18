#
# @lc app=leetcode.cn id=448 lang=python
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for num in nums:
            nums[abs(num)-1] = abs(nums[abs(num)-1]) * -1
        for index in range(len(nums)):
            if nums[index] > 0:
                ret.append(index+1)
        return ret
# @lc code=end

