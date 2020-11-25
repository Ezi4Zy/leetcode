#
# @lc app=leetcode.cn id=1283 lang=python
#
# [1283] 使结果不超过阈值的最小除数
#

# @lc code=start
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        begin = 1
        end = max(nums)
        while begin <= end:
            divisor = (end + begin) / 2
            sum_ = sum([num / divisor + (1 if num % divisor else 0) for num in nums])
            if sum_ > threshold:
                begin = divisor + 1
            else:
                end = divisor
            if begin == divisor and end == divisor:
                return divisor
        return divisor
# @lc code=end

