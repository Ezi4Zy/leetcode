#
# @lc app=leetcode.cn id=179 lang=python
#
# [179] 最大数
#

# @lc code=start
class Solution(object):

    def _cmp(self, num1, num2):
        num1, num2 = num1 * (10 ** len(str(num2))) + num2, num2 * (10 ** len(str(num1))) + num1
        if num1 > num2:
            return 1
        elif num1 < num2:
            return -1
        else:
            return 0


    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if sum(nums) == 0:
            return "0"
        largest_number = "".join([str(num) for num in sorted(nums, cmp=self._cmp, reverse=True)])
        return largest_number
# @lc code=end

