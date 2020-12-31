#
# @lc app=leetcode.cn id=441 lang=python
#
# [441] 排列硬币
#

# @lc code=start
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        begin = 0
        end = n
        while begin < end:
            mid = (begin + end) / 2
            sum_ = mid * (mid + 1) / 2
            if sum_ == n:
                return mid
            elif sum_ < n:
                begin = mid + 1
            else:
                end = mid - 1
        return begin - 1 if n < (begin * (begin + 1) / 2) else begin
# @lc code=end

