#
# @lc app=leetcode.cn id=485 lang=python
#
# [485] 最大连续1的个数
#

# @lc code=start
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        cur = 0
        for num in nums:
            if num:
                cur += 1
            else:
                ret = max(ret, cur)
                cur = 0
        else:
            ret = max(ret, cur)
        return ret
# @lc code=end

