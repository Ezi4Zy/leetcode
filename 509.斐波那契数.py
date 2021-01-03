#
# @lc app=leetcode.cn id=509 lang=python
#
# [509] 斐波那契数
#

# @lc code=start
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
# @lc code=end

