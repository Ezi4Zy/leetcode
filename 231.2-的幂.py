#
# @lc app=leetcode.cn id=231 lang=python
#
# [231] 2的幂
#

# @lc code=start
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 1:
            return (n % 2 == 0) and self.isPowerOfTwo(n/2)
        else:
            return n == 1
# @lc code=end

