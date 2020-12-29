#
# @lc app=leetcode.cn id=263 lang=python
#
# [263] 丑数
#

# @lc code=start
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num > 1:
            flag = False
            if num % 2 == 0:
                num /= 2
                flag = True
            if num % 3 == 0:
                num /= 3
                flag = True
            if num % 5 == 0:
                num /= 5
                flag = True
            if not flag:
                return False
        return True
        
# @lc code=end

