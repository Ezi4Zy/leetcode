#
# @lc app=leetcode.cn id=788 lang=python
#
# [788] 旋转数字
#

# @lc code=start

def good(num, flag):
    if num == 0:
        return flag
    d = num % 10
    if d in (3, 4, 7):
        return False
    if d in (0, 1, 8):
        return good(num / 10, flag)
    return good(num / 10, True)
            

class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        for i in range(1, n+1):
            if good(i, False):
                ret += 1
        return ret

# @lc code=end

