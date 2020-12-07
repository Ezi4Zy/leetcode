#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#

# @lc code=start

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x % 10 == 0 and x != 0) or x < 0:
            return False
        r = 0
        while r < x:
            r = r * 10 + x % 10
            x = x / 10
        return r == x or r / 10 == x

class Solution1(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            s = str(x)
            begin = 0
            end = len(s) - 1
            while end >= begin:
                if s[begin] != s[end]:
                    return False
                begin += 1
                end -= 1
            return True
# @lc code=end

