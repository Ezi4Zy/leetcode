#
# @lc app=leetcode.cn id=693 lang=python
#
# [693] 交替位二进制数
#

# @lc code=start
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 2 == 1:
            n = n / 2
        while n:
            if n % 4 != 2:
                return False
            n = n / 4
        return True
        
# @lc code=end

