#
# @lc app=leetcode.cn id=1304 lang=python
#
# [1304] 和为零的N个唯一整数
#

# @lc code=start
class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        mid = n / 2
        ret = []
        if n % 2 == 1:
            ret.append(0)
        while mid > 0:
            ret.extend([mid, -1 * mid])
            mid -= 1
        return ret
# @lc code=end

