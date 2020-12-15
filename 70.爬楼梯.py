#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#

# @lc code=start
class Solution(object):
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        n_1 = 2
        n_2 = 1
        ret = 0
        for _ in range(3, n+1):
            ret = n_1 + n_2
            n_2, n_1 = n_1, ret
        return ret
# @lc code=end

